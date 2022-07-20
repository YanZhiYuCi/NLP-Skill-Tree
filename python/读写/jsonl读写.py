# -*- coding: UTF-8 -*
import os
import sys
from typing import List, Dict, Set, Tuple, Any, Optional, Union
import json
import time

# 第三方库
import jsonlines
from loguru import logger

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# 载入自定义模块

if __name__ == '__main__':
    current_file_dir = os.path.dirname(__file__)
    jsonl_read_path: str = os.path.join(current_file_dir, 'data/jsonl_read.jsonl')
    jsonl_write_path: str = os.path.join(current_file_dir, 'data/jsonl_write.jsonl')
    data: List[Dict] = [per_data for per_data in jsonlines.open(jsonl_read_path)]
    # 写入:方法一
    # jsonlines.open(jsonl_write_path, 'w').write_all(data)
    # 写入:方法二
    """
    不可写成这种, 在每个per_data时,都会重新新建jsonl_write,文件只会写入最后一个数据
    for per_data in data: jsonlines.open(jsonl_write_path, 'w').write(per_data)
    """
    jsonl_write = jsonlines.open(jsonl_write_path, 'w')
    for per_data in data: jsonl_write.write(per_data)
