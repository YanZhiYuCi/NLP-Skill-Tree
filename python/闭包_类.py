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

class ParallelTransformer:
    def __init__(self):
        self.data = [1, 2]

    def my_function(self):
        self.sum = 1.0
        def custom_1():
            self.sum = 1.0 + 2
            temp = self.data  # 虽然在pycharm中这里的self没有再显示成紫色,仍然可以用
            logger.info('custom_1:{}'.format(temp))
            logger.info('custom_1_sum:{}'.format(self.sum))

            def custom_2():
                temp1 = self.data
                logger.info('custom_2:{}'.format(temp))  # 即使再第二层闭包里仍然可以用
                return temp1

            return custom_2()

        res = custom_1()
        logger.info('my_function_sum:{}'.format(self.sum))
        return res


if __name__ == '__main__':
    c = ParallelTransformer()
    temp_ = c.my_function()
    logger.info('out:{}'.format(temp_))
