# -*- coding: UTF-8 -*
import copy
import os
import sys
from typing import List, Dict, Set, Tuple, Any, Optional, Union
import json
import time

# 第三方库
from loguru import logger
import tqdm
import jsonlines

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


# 载入自定义模块

def json_dir_read_write():
    """
    读取data/json_read目录下的所有json文件,每个文件是一个数据,然后经过某种处理,将每一条数据存放于data/json_write
    :return:
    """
    logger.info('===========处理开始==========')
    current_file_dir = os.path.dirname(__file__)
    file_read_dir: str = os.path.join(current_file_dir, 'data/json_read')
    file_write_dir: str = os.path.join(current_file_dir, 'data/json_write')
    if not os.path.exists(file_write_dir): logger.info('写入目录:{}不存在,新建'.format(file_write_dir)); os.makedirs(
        file_write_dir)
    file_name_list: List[str] = os.listdir(file_read_dir)  # 只是文件名,不包含任何路径
    for file_name in tqdm.tqdm(file_name_list, desc='处理中...'):
        file_read_path = os.path.join(file_read_dir, file_name)
        data_str: str = open(file_read_path).read()
        if not data_str: logger.warning('当前json数据:{}为空,跳过'.format(file_name)); continue
        data: Dict = json.loads(data_str)
        # todo 某种处理,这里直接将输入深拷贝后作为处理的结果
        data_processed = copy.deepcopy(data)
        data_processed_str: str = json.dumps(data_processed, ensure_ascii=False)
        data_processed_str: str = json.dumps(data_processed, ensure_ascii=False, indent=4)  # 直接将数据展开而不是压缩到一行
        file_write_path = os.path.join(file_write_dir, file_name)
        open(file_write_path, 'w').write(data_processed_str)
    logger.info('===========处理结束==========')


if __name__ == '__main__':
    json_dir_read_write()
