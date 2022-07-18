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

if __name__ == '__main__':
    # ##################################################################################################################
    sep_str_1 = '123\n456\n789\n\n000\n'
    sep_str_2 = r'123\n456\n789\n\n000\n'
    string_writer = open('data.txt', 'w')
    string_writer.write(sep_str_1)
    string_writer.write('===============\n')  # 加\n是因为文件写入函数不会需要手动加\n
    string_writer.write(sep_str_2)
    # ##################################################################################################################
    temp_string_0 = '123   456'
    temp_string_1 = '123\t456'
    # 虽然在打印时\t等于4个空格,但是本质上两者是完全不一样的字符串,所以temp_string_0的空格可以被替换,
    # 但是\t的不可以被替换,虽然\t打印时也是显示成了空格
    res_0 = temp_string_0.replace(' ', '')
    res_1 = temp_string_1.replace(' ', '')
    logger.info('res_0:{}'.format(res_0))
    logger.info('res_1:{}'.format(res_1))
