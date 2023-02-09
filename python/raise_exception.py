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

def raise_temp():
    raise Exception('123')


def c1():
    raise_temp()
    print('456')


c1()
