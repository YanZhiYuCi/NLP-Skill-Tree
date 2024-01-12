# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/2/21 5:19 下午
import copy
import json
import os
from typing import Dict, List

import requests
from loguru import logger
import tqdm

url = "http://fanyi.youdao.com/translate"

line = '安徽省亳州市漆园街道花园村，排列有序的光伏成为乡村一道靓丽的风景。近年来，安徽省亳州市蒙城县漆园街道通过与光伏发电企业及农业企业合作，建成运行40MW光伏发电项目，并建设290栋农业设施大棚，将太阳能发电与设施农业有机结合，实现棚顶光伏发电、棚内设施种植蔬菜、中药材等，最大限度发挥光伏电站的效益，不仅为当地农民增加收入，壮大村级集体经济，助力乡村振兴。'


def backtranslate(line):
    data = {
        'doctype': 'json',
        'type': 'AUTO',
        'i': line
    }
    r = requests.get(url, params=data)
    english_result = r.json()
    english_str_list = [p['tgt'] for p in english_result['translateResult'][0]]
    english_str = ''.join(english_str_list)

    data_en2cn = {
        'doctype': 'json',
        'type': 'AUTO',
        'i': english_str
    }
    print(english_result)
    r = requests.get(url, params=data_en2cn)
    zh_result = r.json()
    zh_str_list = [p['tgt'] for p in zh_result['translateResult'][0]]
    zh_str = ''.join(zh_str_list)
    return zh_str


logger.info('===========处理开始==========')
current_file_dir = os.path.dirname(__file__)
file_read_dir: str = os.path.join(current_file_dir, '分类数据')
file_write_dir: str = os.path.join(current_file_dir, '分类数据_反向翻译')
if not os.path.exists(file_write_dir):
    logger.info('写入目录:{}不存在,新建'.format(file_write_dir))
    os.makedirs(file_write_dir)

file_name_list: List[str] = os.listdir(file_read_dir)  # 只是文件名,不包含任何路径
for file_name in tqdm.tqdm(file_name_list, desc='处理中...'):
    file_read_path = os.path.join(file_read_dir, file_name)
    data_str: str = open(file_read_path, encoding='utf-8').read()
    backtranslate_data = backtranslate(data_str)
    file_write_path = os.path.join(file_write_dir, file_name)
    open(file_write_path, 'w', encoding='utf-8').write(backtranslate_data)
logger.info('===========处理结束==========')
