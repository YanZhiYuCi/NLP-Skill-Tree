# -*- coding: UTF-8 -*
import os
import sys

# 第三方库

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# 载入自定义模块

c = [1, 2, 3]
# c[3] = []  # list assignment index out of range
c1 = list(range(2, 2))  # []
