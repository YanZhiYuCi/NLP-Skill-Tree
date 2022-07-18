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


def find_all_sub_string_index(sub_string: str, raw_string: str) -> List[int]:
    """查询子串在字符串中的所有开始位置,找不到则返回空列表"""
    sub_string_index: List[int] = []
    for each in range(len(raw_string) - len(sub_string) + 1):
        if raw_string[each:each + len(sub_string)] == sub_string:  # 找出与子字符串首字符相同的字符位置
            sub_string_index.append(each)
    return sub_string_index


if __name__ == '__main__':
    raw_string_ = '利达李大国李小国李大国大果子通天紫金锤李大国李da国'
    sub_string_ = '李大国'
    logger.info(raw_string_.find(sub_string_))  # 只会返回第一个,找不到则返回-1
    logger.info(raw_string_.rfind(sub_string_))  # 只会返回最后一个,找不到则返回-1
    t = find_all_sub_string_index(sub_string_, raw_string_)  # 返回所有的,找不到则返回空列表
    print('子字符串{0}在字符串{1}中的位置为：'.format('sub_string', 'raw_string'), t)
