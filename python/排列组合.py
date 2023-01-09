import itertools as it

# 使用两个序列进行排列组合
for e in it.product('AB', 'CD'):
    print(''.join(e), end=', ')  # AC, AD, BC, BD,
print('\n---------')
# 使用一个序列、重复2次进行全排列
for e in it.product('AB', repeat=2):
    print(''.join(e), end=', ')  # AA, AB, BA, BB,
print('\n---------')
# 从序列中取2个元素进行排列
for e in it.permutations('ABCD', 2):
    print(''.join(e), end=', ')  # AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC,
print('\n---------')
# 从序列中取2个元素进行组合、元素不允许重复
for e in it.combinations('ABCD', 2):
    print(''.join(e), end=', ')  # AB, AC, AD, BC, BD, CD,
print('\n---------')
# 从序列中取2个元素进行组合、元素允许重复
for e in it.combinations_with_replacement('ABCD', 2):
    print(''.join(e), end=', ')  # AA, AB, AC, AD, BB, BC, BD, CC, CD, DD,

# 列表 排列
c = ['1', '2', '3', '4']
for p in it.permutations(c, 2):
    print(p)
print('\n---------')

# 列表 组合
c = ['1', '2', '3', '4']
for p in it.combinations(c, 2):
    print(p)
