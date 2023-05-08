import glob
import os
import pprint
import time

data_dir = '/Users/machaoyang/Desktop/Projects/post_hand_with_location/data/processed_video'
pattern = '*'  # 目录下所有文件
# pattern = '*.mp4'  # 文件后缀名为mp4
sort_rule = lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x)))  # 按文件创建时间
h_time_path_list = sorted(glob.glob(os.path.join(data_dir, pattern)), key=sort_rule, reverse=True)
pprint.pprint(h_time_path_list)
