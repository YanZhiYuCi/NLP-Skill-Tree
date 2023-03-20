# -*- coding: UTF-8 -*
import os
import sys
import random
from typing import List, Dict, Set, Tuple, Any, Optional, Union
import json
import time

# 第三方库
import jsonlines
from loguru import logger as train_log
import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), './'))

from util import convert_data, ner_eval

current_file_dir = os.path.dirname(__file__)
jsonl_train_path: str = os.path.join(current_file_dir, 'cluener_public/train.jsonl')
jsonl_dev_path: str = os.path.join(current_file_dir, 'cluener_public/dev.jsonl')
raw_train_data: List[Dict] = [per_data for per_data in jsonlines.open(jsonl_train_path)]
raw_dev_data: List[Dict] = [per_data for per_data in jsonlines.open(jsonl_dev_path)]
train_data = convert_data(raw_train_data)
dev_data = convert_data(raw_dev_data)

# train_data, dev_data = split_by_ratio(train_data, 0.8, train_log)

train_log.info("模型训练---切分训练与验证数据集完成!")

# todo 处理增量训练
incremental_training = False
if incremental_training is True:
    train_log.info("模型训练---进行模型增量训练!")
    train_log.info("模型训练---加载增量训练模型...")
    # todo 下载旧的模型
    nlp = spacy.load('')
    train_log.info("模型训练---加载增量训练模型完成!")
else:
    train_log.info("模型训练---训练新的实体抽取模型!")
    nlp = spacy.blank('zh')

# 初始化模型，即模型创建
train_log.info("模型训练---初始化实体抽取模型...")
if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe('ner', last=True)
else:
    ner = nlp.get_pipe('ner')

for _, annotations in train_data:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

train_log.info("模型训练---初始化实体抽取模型完成!")

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
train_log.info("模型训练---训练任务进行中...")

epochs = 100
train_data_size = len(train_data)
dev_data_size = len(dev_data)

loss = []
precession = []
recall = []
f1 = []
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training()
    eval_p, eval_r, eval_f = [], [], []
    for itn in range(epochs):
        random.shuffle(train_data)
        losses = {}
        sizes = 32
        batches = minibatch(train_data, size=sizes)
        for batch in batches:
            """
            ValueError: [E103] Trying to set conflicting doc.ents: '(15, 35, 'book')' and '(16, 20, 'company')'. 
            A token can only be part of one entity, so make sure the entities you're setting don't overlap. 
            To work with overlapping entities, consider using doc.spans instead.
            """
            try:
                example_batch = [Example.from_dict(nlp.make_doc(sample[0]), sample[1]) for sample in batch]
            except:
                continue
            nlp.update(example_batch, sgd=optimizer, drop=0.5, losses=losses)

        loss.append(losses["ner"])

        for i in range(len(dev_data)):
            i_doc = nlp(dev_data[i][0])
            true_entities = dev_data[i][1]["entities"]
            predict_entities = [(_.start, _.end, _.label_, _.text) for _ in i_doc.ents]

            p, r, f = ner_eval(true_entities, predict_entities)
            eval_p.append(p)
            eval_r.append(r)
            eval_f.append(f)

        precession.append(np.mean(eval_p))
        recall.append(np.mean(eval_r))
        f1.append(np.mean(eval_f))
        train_log.info("模型训练---保存训练过程信息,迭代次数:%s!" % (itn + 1))

        train_log.info("模型训练---第%s次训练评估---" % (itn + 1) + "\n" +
                       "训练损失: %s" % loss + "\n" +
                       "精准率: %s" % precession + "\n" +
                       "召回率: %s" % recall + "\n" +
                       "f1: %s" % f1)
        # 模型保存
        output_dir = 'model/model_{}'.format(itn)
        nlp.to_disk(output_dir)
train_log.info("模型训练---训练任务完成!")

# 模型保存
output_dir = 'model'
nlp.to_disk(output_dir)
# FileProcess.save_json(labels_map, model_path + "/labels_map.json")
train_log.info("模型训练---模型保存本地成功，模型路径: %s!" % output_dir)
