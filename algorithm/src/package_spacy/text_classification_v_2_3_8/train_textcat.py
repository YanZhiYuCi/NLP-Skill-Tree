#!/usr/bin/env python
# coding: utf8
"""Train a convolutional neural network text classifier on the
IMDB dataset, using the TextCategorizer component. The dataset will be loaded
automatically via Thinc's built-in dataset loader. The model is added to
spacy.pipeline, and predictions are available via `doc.cats`. For more details,
see the documentation:
* Training: https://spacy.io/usage/training
Compatible with: spaCy v2.0.0+
本代码是v2.3.8的代码的示例 可以运行在spacy==2.3.8环境
"""
from __future__ import unicode_literals, print_function

import os
from typing import List, Dict, Set, Tuple, Any, Optional, Union
import random
from pathlib import Path

import jsonlines
import plac
import spacy
from spacy.util import minibatch, compounding
from sklearn.metrics import classification_report


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_texts=("Number of texts to train from", "option", "t", int),
    n_iter=("Number of training iterations", "option", "n", int),
    init_tok2vec=("Pretrained tok2vec weights", "option", "t2v", Path),
)
def main(model=None, output_dir=None, n_iter=20, n_texts=2000, init_tok2vec=None):
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()

    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("zh")  # create blank Language class
        print("Created blank 'zh' model")

    # add the text classifier to the pipeline if it doesn't exist
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "textcat" not in nlp.pipe_names:
        textcat = nlp.create_pipe(
            "textcat", config={"exclusive_classes": True, "architecture": "simple_cnn"}
        )
        nlp.add_pipe(textcat, last=True)
    # otherwise, get it, so we can add labels to it
    else:
        textcat = nlp.get_pipe("textcat")

    # load the IMDB dataset
    print("Loading custom data...")
    (train_texts, train_cats), (dev_texts, dev_cats), label_list = load_data(limit=1000, split=0.8)
    train_texts = train_texts[:n_texts]
    train_cats = train_cats[:n_texts]
    # add label to text classifier
    for p_label in label_list:
        textcat.add_label(p_label)
    train_data = list(zip(train_texts, [{"cats": cats} for cats in train_cats]))
    # get names of other pipes to disable them during training
    pipe_exceptions = ["textcat", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    with nlp.disable_pipes(*other_pipes):  # only train textcat
        optimizer = nlp.begin_training()
        if init_tok2vec is not None:
            with init_tok2vec.open("rb") as file_:
                textcat.model.tok2vec.from_bytes(file_.read())
        print("Training the model...")
        batch_sizes = compounding(4.0, 32.0, 1.001)
        batch_sizes = 8
        for i in range(n_iter):
            losses = {}
            # batch up the examples using spaCy's minibatch
            random.shuffle(train_data)
            batches = minibatch(train_data, size=batch_sizes)
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.2, losses=losses)
            print("train dataset loss:{}".format(losses["textcat"]))
            with textcat.model.use_params(optimizer.averages):
                # evaluate on the dev data split off in load_data()
                evaluate(nlp.tokenizer, textcat, dev_texts, dev_cats, label_list)

    # test the trained model
    test_text = "This movie sucked"
    doc = nlp(test_text)
    print(test_text, doc.cats)

    if output_dir is not None:
        with nlp.use_params(optimizer.averages):
            nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(test_text)
        print(test_text, doc2.cats)


def load_data(limit=0, split=0.8):
    """Load data from the IMDB dataset."""
    # Partition off part of the train data for evaluation
    # train_data, _ = thinc.extra.datasets.imdb()
    current_file_dir = os.path.dirname(__file__)
    jsonl_train_path: str = os.path.join(current_file_dir, 'tnews_public/train.jsonl')
    jsonl_dev_path: str = os.path.join(current_file_dir, 'tnews_public/dev.jsonl')
    raw_train_data: List[Dict] = [per_data for per_data in jsonlines.open(jsonl_train_path)]
    raw_dev_data: List[Dict] = [per_data for per_data in jsonlines.open(jsonl_dev_path)]
    train_data = [(p['sentence'], p['label_desc']) for p in raw_train_data]
    dev_data = [(p['sentence'], p['label_desc']) for p in raw_dev_data]
    train_data += dev_data
    label_list = list({p[1] for p in train_data + dev_data})
    # train_data = [('hello world', 'news')]
    random.shuffle(train_data)
    train_data = train_data[-limit:]
    texts, labels = zip(*train_data)
    cats = [{p_label: (1 if p_label == y else 0) for p_label in label_list} for y in labels]
    split = int(len(train_data) * split)
    return (texts[:split], cats[:split]), (texts[split:], cats[split:]), label_list


def evaluate(tokenizer, textcat, texts, cats, label_list):
    labels = [k for p in cats for k, v in p.items() if v]
    docs = (tokenizer(text) for text in texts)
    predict = [max(doc.cats, key=doc.cats.get) for i, doc in enumerate(textcat.pipe(docs))]
    print(classification_report(labels, predict, labels=label_list))


if __name__ == "__main__":
    plac.call(main)
