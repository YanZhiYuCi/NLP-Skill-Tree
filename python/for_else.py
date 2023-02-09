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

n = 10
for x in range(2, n):
    if x % 2 == 0:
        print('//')
        break
    elif x % 3 == 0:
        print('///')
        break
else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')
