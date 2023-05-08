# -*- coding: UTF-8 -*
import os
import sys
from typing import List, Dict, Set, Tuple, Any, Optional, Union
import json
import time

# 第三方库
import pandas as pd
from loguru import logger

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# 载入自定义模块

if __name__ == '__main__':
    # 读写excel###########################################################################################################
    current_file_dir = os.path.dirname(__file__)
    current_read_path: str = os.path.join(current_file_dir, 'data/excel_read.xlsx')
    current_write_path: str = os.path.join(current_file_dir, 'data/excel_write.xlsx')
    dataframe: pd.DataFrame = pd.read_excel(current_read_path, sheet_name='检验')
    # 'list' : dict like {column -> [values]}
    # 'records' : list like [{column -> value}, ... , {column -> value}]
    # 使用pandas读取excel为dataframe,然后转成熟悉的字典列表,经过处理之后再写入excel
    data_dict_list: List[Dict] = dataframe.to_dict(orient='records')
    dataframe = dataframe.sort_values(by=['编号'], ascending=[False])
    dataframe.to_excel(current_write_path, sheet_name='检验', index=False)

    # 读写csv#############################################################################################################
    current_file_dir = os.path.dirname(__file__)
    current_read_path: str = os.path.join(current_file_dir, 'data/csv_read.csv')
    current_write_path: str = os.path.join(current_file_dir, 'data/csv.write.csv')
    dataframe: pd.DataFrame = pd.read_csv(current_read_path)
    # 'list' : dict like {column -> [values]}
    # 'records' : list like [{column -> value}, ... , {column -> value}]
    # 使用pandas读取excel为dataframe,然后转成熟悉的字典列表,经过处理之后再写入excel
    data_dict_list: List[Dict] = dataframe.to_dict(orient='records')
    dataframe.to_csv(current_write_path, index=False)
