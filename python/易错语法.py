# -*- coding: UTF-8 -*
import os
import sys

# 第三方库

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# 载入自定义模块

# 列表元素访问越界##########################################################################################################
c = [1, 2, 3]
# c[3] = []  # list assignment index out of range
c1 = list(range(2, 2))  # []

# 二维排序################################################################################################################
list_1 = [['Angle', '0121701100106', 99], ['Jack', '0121701100107', 86], ['Tom', '0121701100109', 65],
          ['Smith', '0121701100111', 100], ['Bob', '0121701100115', 77], ['Lily', '0121701100117', 59]]
new_list_2 = sorted(list_1, key=(lambda x: x[0]), reverse=False)  # 按第一个元素
new_list_3 = sorted(list_1, key=(lambda x: x[2]), reverse=True)  # 按第三个元素
print(new_list_2)
print(new_list_3)
list_1.sort(key=(lambda x: x[0]), reverse=False)  # 按第一个元素
print(list_1)

# 二维数组，按照第一个元素升序排序，当第一个元素相同时，按第二个元素升序
arr = [('d', 3), ('a', 5), ('d', 1), ('c', 2), ('d', 2)]
res = sorted(arr, key=lambda x: (x[0], x[1]))
arr.sort(key=lambda x: (x[0], x[1]))
print(arr)
print(res)

# 二维数组，第一个元素升序，当第一个元素相同时，按第二个元素降序
arr = [('d', 3), ('a', 5), ('d', 1), ('c', 2), ('d', 2)]
res = sorted(arr, key=lambda x: (x[0], -int(x[1])))
arr.sort(key=lambda x: (x[0], -int(x[1])))
print(arr)
print(res)
