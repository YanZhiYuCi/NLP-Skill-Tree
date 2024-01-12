# -*- coding: UTF-8 -*
import copy

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

a30 = [1, 2, 3]
a30_1 = a30
a30_2 = a30[:]
a30_3 = copy.deepcopy(a30)
a30.append(4)
print('a30_1:{}'.format(a30_1))
print('a30_2:{}'.format(a30_2))
print('a30_3:{}'.format(a30_3))

a10 = 5


def change_a_simple(a10):
    a10 = 10
    print('a10_inner:{}'.format(a10))


change_a_simple(a10)
print('a10_out:{}'.format(a10))


def change_a(a20):
    a20[0] = 20
    print('a20_inner:{}'.format(a20))


a20 = [0, 1, 2]
change_a(a20)
print('a20_out:{}'.format(a20))


def fonc(list1):
    list1.append(3)
    list1 = [21, 43, 5]
    print('inner:{}'.format(list1))


list1 = [1, 2, 4, 6, 2]
fonc(list1)
print('out:{}'.format(list1))

c = {1: 2}
c1 = []
c2 = c in c1
d = {1: 2}
c1.append(d)
c5 = c in c1
