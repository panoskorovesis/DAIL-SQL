## Train Embeddings

At the [prompt/ExampleSelectorTemplate.py](prompt/ExampleSelectorTemplate.py) we can see the embedding generation of the 
train set.

The model used is [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)

The produced embeddings for each sentence have a shape of 768 (ie Bert size)

## Generate.py

This script does the following:

1) Generates questions based on:

    a) Selected question representation

    b) Selected question similarity search

2) Saves questions under output like `dataset/process/SPIDER-TEST_SQL_9-SHOT_EUCDISQUESTIONMASK_QA-EXAMPLE_CTX-200_ANS-4096`

### Example Qualities:

- **gr spider**: `Example quality: 0.5386646560837339`

- **en spider**: `Example quality: 0.6664819248932345`

### Next Steps:

1) See score with original emb model for en spider
2) Try different embeddings to get better scores
3) Revisit glove importance on schema linking