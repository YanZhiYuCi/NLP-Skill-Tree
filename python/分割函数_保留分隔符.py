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

def chunk_with_separator(content: str, separator: str) -> List[str]:
    """
    :param content: 原始文本,字符串
    :param separator: 分割符,字符串
    :return: 分割后的字符串列表
    """
    chunk_list: List[str] = []
    current_chunk: str = ''
    for c in content:
        current_chunk += c
        if c == separator:
            chunk_list.append(current_chunk)
            current_chunk = ''

    if current_chunk:
        chunk_list.append(current_chunk)
    return chunk_list


if __name__ == '__main__':
    separator_str = '。'
    content_str = '今天天气真好。但是昨天晚上的雨下得很大。'
    logger.info(chunk_with_separator(content=content_str, separator=separator_str))
    content_str = '今天天气真好。但是昨天晚上的雨下得很大。。'
    logger.info(chunk_with_separator(content=content_str, separator=separator_str))
    content_str = '。今天天气真好。但是昨天晚上的雨下得很大。'
    logger.info(chunk_with_separator(content=content_str, separator=separator_str))
    content_str = '。今天天气真好。但是昨天晚上的雨下得很大'
    logger.info(chunk_with_separator(content=content_str, separator=separator_str))
    content_str = '今天天气真好但是昨天晚上的雨下得很大'
    logger.info(chunk_with_separator(content=content_str, separator=separator_str))

