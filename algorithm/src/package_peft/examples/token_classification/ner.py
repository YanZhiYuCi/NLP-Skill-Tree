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
    logger.debug("debug message")
    logger.info("info level message")
    logger.warning("warning level message")
    logger.error("error level message")
    logger.critical("critical level message")
