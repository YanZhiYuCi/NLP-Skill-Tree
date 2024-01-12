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

# 字典排序 按照value排序
similarity_dict = {'a': 1, 'c': 3, 'b': 2}
sorted_similarity_dict = sorted(similarity_dict.items(), reverse=True, key=lambda x: x[1])
print('similarity_dict:{}'.format(sorted_similarity_dict))  # [('c', 3), ('b', 2), ('a', 1)]

# 字典的值是字典 按照字典的值中某个键对应的值进行排序
my_dict = {
    "a": {"age": 30, "name": "Alice"},
    "b": {"age": 25, "name": "Bob"},
    "c": {"age": 35, "name": "Charlie"},
}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]["age"], reverse=True))
print(sorted_dict)

# 对字典列表排序
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)

lst = [
    {'name': 'Tom', 'age': 22, 'score': 85},
    {'name': 'Jerry', 'age': 20, 'score': 90},
    {'name': 'Bob', 'age': 21, 'score': 85},
    {'name': 'Alice', 'age': 20, 'score': 95},
]

# 首先按照'score'排序，然后在'score'相同的情况下按照'age'排序
sorted_lst = sorted(lst, key=lambda x: (x['score'], x['age']), reverse=True)
print(sorted_lst)
