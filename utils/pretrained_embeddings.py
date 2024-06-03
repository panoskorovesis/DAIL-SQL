import abc
import functools
import os
import time

import bpemb
import torch
import torchtext

import stanza

class Embedder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def tokenize(self, sentence):
        '''Given a string, return a list of tokens suitable for lookup.'''
        pass

    @abc.abstractmethod
    def untokenize(self, tokens):
        '''Undo tokenize.'''
        pass

    @abc.abstractmethod
    def lookup(self, token):
        '''Given a token, return a vector embedding if token is in vocabulary.
        If token is not in the vocabulary, then return None.'''
        pass

    @abc.abstractmethod
    def contains(self, token):
        pass

    @abc.abstractmethod
    def to(self, device):
        '''Transfer the pretrained embeddings to the given device.'''
        pass


class GloVe(Embedder):

    def __init__(self, kind, lemmatize=False, use_stanza=False, language='en'):
        cache = os.path.join(os.environ.get('CACHE_DIR', os.getcwd()), 'vector_cache')
        self.glove = torchtext.vocab.GloVe(name=kind, cache=cache)
        self.dim = self.glove.dim
        self.vectors = self.glove.vectors
        self.lemmatize = lemmatize
        self.stanza = use_stanza
        self.language = language
        self.nlp = None

        if not use_stanza:
            
            self.corenlp_annotators = ['tokenize', 'ssplit']
        else:
            self.stanza_annotators = ['tokenize']
        if lemmatize:
            if not use_stanza:
                self.corenlp_annotators.append('lemma')
            else:
                self.stanza_annotators.append('lemma')

        # In the case of stanza we have to initialize the NLP and download the languages
        if use_stanza:
            stanza.download('el')
            stanza.download('en')
            self.nlp = stanza.Pipeline(language, use_gpu=False, processors=["tokenize", "lemma"])

    @functools.lru_cache(maxsize=1024)
    def tokenize(self, text):
        if not self.stanza:
            from utils.linking_utils import corenlp
            ann = corenlp.annotate(text, self.corenlp_annotators)
            if self.lemmatize:
                return [tok.lemma.lower() for sent in ann.sentence for tok in sent.token]
            else:
                return [tok.word.lower() for sent in ann.sentence for tok in sent.token]
            
        else:

            doc = self.nlp(text, self.stanza_annotators)
            if self.lemmatize:
                return [word.lemma.lower() for sent in doc.sentences for word in sent.words]
            else:
                [word.text.lower() for sent in doc.sentences for word in sent.words]


    @functools.lru_cache(maxsize=1024)
    def tokenize_for_copying(self, text):
        if not self.stanza:
            from utils.linking_utils import corenlp
            ann = corenlp.annotate(text, self.corenlp_annotators)
            text_for_copying = [tok.originalText.lower() for sent in ann.sentence for tok in sent.token]
            if self.lemmatize:
                text = [tok.lemma.lower() for sent in ann.sentence for tok in sent.token]
            else:
                text = [tok.word.lower() for sent in ann.sentence for tok in sent.token]

        else:
            doc = self.nlp(text, self.stanza_annotators)
            text_for_copying = [word.text.lower() for sent in doc.sentences for word in sent.words]
            if self.lemmatize:
                text = [word.lemma.lower() for sent in doc.sentences for word in sent.words]
            else:
                text = [word.text.lower() for sent in doc.sentences for word in sent.words]

        return text, text_for_copying


    def untokenize(self, tokens):
        return ' '.join(tokens)

    def lookup(self, token):
        i = self.glove.stoi.get(token)
        if i is None:
            return None
        return self.vectors[i]

    def contains(self, token):
        return token in self.glove.stoi

    def to(self, device):
        self.vectors = self.vectors.to(device)