
# 在使用argparse定义程序参数时，常规用法如下：
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type=int, default=5000, help='Train epochs.')
parser.add_argument('--batchSize', type=int, default=15, help='Train batch size.')
configs = parser.parse_args()
# 此时得到的configs为Namespace类型，它包含了__dict__属性，因此可以使用vars将configs转换为字典dic（只要变量包含了__dict__属性就可以使用vars转换为字典）
dic = vars(configs)
