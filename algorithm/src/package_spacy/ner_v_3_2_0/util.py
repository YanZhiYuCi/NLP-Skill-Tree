# -*- coding: UTF-8 -*
import os
import sys
from typing import List, Dict, Set, Tuple, Any, Optional, Union
import json
import time

# 第三方库
from loguru import logger

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


# 载入自定义模块

def convert_data(raw_data: List[Dict]) -> List[Tuple[str, Dict]]:
    res = []
    for per_raw_data in raw_data:
        entity_list = []
        # {'name': {'叶老桂': [[9, 11]]}, 'company': {'浙商银行': [[0, 3]]}}
        for entity_type, entity_value_dict in per_raw_data['label'].items():
            for entity_value, entity_value_index_List in entity_value_dict.items():
                for entity_value_index in entity_value_index_List:
                    entity_list.append((entity_value_index[0], entity_value_index[1] + 1, entity_type))
        per_res: Tuple = (per_raw_data['text'], {"entities": entity_list})
        res.append(per_res)
    return res


def ner_eval(true_entities, predict_entities):
    if len(predict_entities) < 1:
        return 0.0, 0.0, 0.0
    else:
        TP = 0
        for t in true_entities:
            for p in predict_entities:
                if t[0] == p[0] and t[1] == p[1] and t[2] == p[2]:
                    TP += 1
        precession = TP / len(predict_entities)
        recall = TP / len(true_entities)
        f1 = 0.0 if TP == 0 else 2 * precession * recall / (precession + recall)
        return precession, recall, f1
