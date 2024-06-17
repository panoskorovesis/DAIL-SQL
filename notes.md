## Train Embeddings

At the [prompt/ExampleSelectorTemplate.py](prompt/ExampleSelectorTemplate.py) we can see the embedding generation of the 
train set.

The model used is [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)

The produced embeddings for each sentence have a shape of 768 (ie Bert size)

## Preprocess.py

### En - Spider (Stanza)

1) test_schema_linking: 

    a) q_col_match:  109 / 110

    b) q_tab_match: 101 / 110

2) train_schema_linking: 

    a) q_col_match:  913 / 924

    b) q_tab_match: 829  / 924

### Gr - Spider (Stanza)

1) test_schema_linking: 

    a) q_col_match:  70 / 110

    b) q_tab_match: 62 / 110

2) train_schema_linking: 

    a) q_col_match:  644 / 924

    b) q_tab_match: 458  / 924

__Notes__:

1) Glove text embeddings are not used for the schema linking process. It's done by lemmatizing + searching for similarities

## Generate.py

This script does the following:

1) Generates questions based on:

    a) Selected question representation

    b) Selected question similarity search

2) Saves questions under output like `dataset/process/SPIDER-TEST_SQL_9-SHOT_EUCDISQUESTIONMASK_QA-EXAMPLE_CTX-200_ANS-4096`

### Example Qualities:

#### example_type: QA | selector_type: COSSIMILAR

- **en spider**: `Example quality: 0.5762885356725053`

- **gr spider**: `Example quality: 0.5750991359942765`

#### example_type: QA | selector_type: RANDOM

- **en spider**: `Example quality: 0.43791817715720815`

- **gr spider**: `Example quality: 0.43791817715720815`

#### example_type: QA | selector_type: EUCDISTANCE

- **en spider**: `Example quality: 0.5723197812137516`

- **gr spider**: `Example quality: 0.5792297453761447`

#### example_type: QA | selector_type: EUCDISTANCETHRESHOLD

- **en spider**: `Example quality: nan`

- **gr spider**: `Example quality: 1`

#### example_type: QA | selector_type: EUCDISSKLSIMTHR

- **en spider**: `Example quality: 0.8852581454244959`

- **gr spider**: `Example quality: 0.8747716283180217`

#### example_type: QA | selector_type: EUCDISQUESTIONMASK

- **en spider**: `Example quality: 0.6664819248932345`

- **gr spider**: `Example quality: 0.5386646560837339`

#### example_type: QA | selector_type: EUCDISPRESKLSIMTHR

- **en spider**: `Example quality: ?`

- **gr spider**: `Example quality: ?`

This case cause a `KeyError "pre_skeleton"`



__Changing Bert__ model between `sentence-transformers/all-mpnet-base-v2` and `sentence-transformers/bert-base-nli-mean-tokens`:

1) Does not affect the score for english

2) Same thing goes for the greek

### Next Steps:

1) See score with original emb model for en spider
2) Try different embeddings to get better scores