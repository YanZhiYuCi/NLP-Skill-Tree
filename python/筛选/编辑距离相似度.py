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

import pandas as pd
from fuzzywuzzy import fuzz
import tqdm


if __name__ == '__main__':
    current_file_dir = os.path.dirname(__file__)
    current_read_path: str = os.path.join(current_file_dir, 'df_remove_key.csv')
    current_write_path: str = os.path.join(current_file_dir, 'res.txt')
    write_data = open(current_write_path, 'w', encoding='utf-8')
    dataframe: pd.DataFrame = pd.read_csv(current_read_path)
    will_process_word_list = dataframe['值'].tolist()  # 要处理的词
    current_key_word_path: str = os.path.join(current_file_dir, 'select_key.txt')
    truth_key_word_list = [p.strip() for p in open(current_key_word_path, 'r', encoding='utf-8')]  # 已经人工确定过的词
    res: List[str] = []
    res_set: Set = set()
    truth_key_word_set = set(truth_key_word_list)
    will_process_word_list = [p for p in will_process_word_list if p not in truth_key_word_set]  # 在候选列表中排除真实词
    for p_word in tqdm.tqdm(truth_key_word_list, desc='doing', disable=True):
        per_word_res = []
        for p_will_process_word in will_process_word_list:
            similarity_ratio = fuzz.ratio(p_word, p_will_process_word)
            # 相似度 0-100 大于70 且候选词不在之前的结果集合中出现过
            if similarity_ratio > 70 and p_will_process_word not in res_set:
                per_word_res.append(p_will_process_word)
        print('当前词：{}'.format(p_word))
        print(per_word_res)
        res.extend(per_word_res)
    for p in res:
        write_data.write(p + '\n')

