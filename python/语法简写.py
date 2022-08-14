# -*- coding: UTF-8 -*
import os
import sys

# 第三方库
from loguru import logger

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# 载入自定义模块

"""代码简写的目的是尽量用较少的行数实现相同的功能，因为眼睛一下子能看到的行数有限，充分利用了屏幕的宽度，整体表现上代码的行数减少了，方便调试"""

temp = [['Hello World'] * 4 for _ in range(2)]
logger.info('Hello World矩阵:\n{}'.format(temp))

# 一行代码写for循环和if条件判断#############################################################################################
data = [1, 2, 3, 4, 5]
temp = [per for per in data if per % 2 == 0]
logger.info('偶数:\n{}'.format(temp))

# 一行代码写for循环和if else语句############################################################################################
all_labels = [1, 0, 1]
all_predicts = [1, 0, 0]
temp = [1 if per_label == per_pred else 0 for per_label, per_pred in zip(all_labels, all_predicts)]
logger.info('判断对应位置是否相等:\n{}'.format(temp))

temp = [1 if (i + j) % 2 == 0 else 0 for i in range(2) for j in range(4)]
logger.info('输出一维列表:\n{}'.format(temp))

temp = [[1 if (i + j) % 2 == 0 else 0 for i in range(2)] for j in range(4)]
logger.info('输出二维列表:\n{}'.format(temp))

# 一行代码以字典形式写两层for循环和if-else#######################################################################################################################
c = {'脉搏': [100100, 100],
     '体温': '36.5',
     '一般情况': '营养发育正常，表情自然，神志清楚，反应好，面色红润，唇周无发绀，无脱水貌。  ',
     '颈部': '颈项无强直，颈动脉搏动正常，气管居中。',
     }
temp = {k: (''.join([str(p_str) for p_str in v]) if isinstance(v, list) else v) for k, v in c.items()}
logger.info('合并后的字符串序列:\n{}'.format(temp))
