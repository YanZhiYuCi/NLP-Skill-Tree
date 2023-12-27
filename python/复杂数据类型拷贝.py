# -*- coding: UTF-8 -*
import os
import sys
from typing import List, Dict, Set, Tuple, Any, Optional, Union
import json
import time

# 第三方库
from loguru import logger

a = [1, 2]
a1 = [a, 'a']
a2 = [a, 'b']
print('a1:{}'.format(a1))
print('a2:{}'.format(a2))
print('=' * 80)
a = [1, 3]
print('a1:{}'.format(a1))
print('a2:{}'.format(a2))
print('=' * 80)
a1 = [a, 'a']
a2 = [a, 'b']
print('a1:{}'.format(a1))
print('a2:{}'.format(a2))

'''
所以鉴于此问题，不要使用上述形式定义变量
'''