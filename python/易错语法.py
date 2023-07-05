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

# 使用heapq模块，获取列表中n个最大或最小的元素#################################################################################
import heapq

scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]

print(heapq.nlargest(3, scores))  # [91, 87, 82]
print(heapq.nsmallest(5, scores))  # [15, 33, 33, 49, 51]

# 将列表中的所有元素作为参数传递给函数#########################################################################################
my_list = [1, 2, 3, 4]

print(my_list)  # [1, 2, 3, 4]
print(*my_list)  # 1 2 3 4


def sum_of_elements(*arg):
    total = 0
    for i in arg:
        total += i

    return total


result = sum_of_elements(*[1, 2, 3, 4])
print(result)  # 10

# 使用filter()，获得一个新对象##############################################################################################
my_list = [1, 2, 3, 4]
odd = filter(lambda x: x % 2 == 1, my_list)
print(list(odd))  # [1, 3]
print(my_list)  # [1, 2, 3, 4]

# map()函数将给定函数应用于可迭代对象(列表、元组等)，然后返回结果(map对象)#########################################################
my_list = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, my_list)
print(list(squared))  # [1, 4, 9, 16]
print(my_list)  # [1, 2, 3, 4]


# 可以在同一个作用域内多次定义一个方法#########################################################################################
def get_address():
    return "First address"


def get_address():
    return "Second address"


def get_address():
    return "Third address"


print(get_address())  # Third address


# 在外部直接访问私有属性####################################################################################################
class Engineer:
    def __init__(self, name):
        self.name = name
        self.__starting_salary = 62000


dain = Engineer('Dain')
print(dain._Engineer__starting_salary)  # 62000


# 在类中使用 + 操作符######################################################################################################
class Expenses:
    def __init__(self, rent, groceries):
        self.rent = rent
        self.groceries = groceries

    def __add__(self, other):
        return Expenses(self.rent + other.rent,
                        self.groceries + other.groceries)


april_expenses = Expenses(1000, 200)
may_expenses = Expenses(1000, 300)

total_expenses = april_expenses + may_expenses
print(total_expenses.rent)  # 2000
print(total_expenses.groceries)  # 500


# 同样的，== 操作符使用__eq__方法###########################################################################################
class Journey:
    def __init__(self, location, destination, duration):
        self.location = location
        self.destination = destination
        self.duration = duration

    def __eq__(self, other):
        return ((self.location == other.location) and
                (self.destination == other.destination) and
                (self.duration == other.duration))


first = Journey('Location A', 'Destination A', '30min')
second = Journey('Location B', 'Destination B', '30min')

print(first == second)


# 为类的对象定义自定义的可打印版本############################################################################################
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return repr('Rectangle with area=' + str(self.a * self.b))


print(Rectangle(3, 4))  # 'Rectangle with area=12'

# 检查字符串是否都是字母或数字###############################################################################################
name = "Password"
print(name.isalnum())  # True

name = "Secure Password "
print(name.isalnum())  # False

name = "S3cur3P4ssw0rd"
print(name.isalnum())  # True

name = "133"
print(name.isalnum())  # True
# 检查字符串是否都是字母####################################################################################################
string = "Name"
print(string.isalpha())  # True

string = "Firstname Lastname"
print(string.isalpha())  # False

string = "P4ssw0rd"
print(string.isalpha())  # False
# 检查字符串是否为数字######################################################################################################
string = "seven"
print(string.isdigit())  # False

string = "1337"
print(string.isdigit())  # True

string = "5a"
print(string.isdigit())  # False

string = "2**5"
print(string.isdigit())  # False
# 检查字符串是否为中文数字##################################################################################################
# 42673
string = "四二六七三"

print(string.isdigit())  # False
print(string.isnumeric())  # True
# 在元组中嵌套列表和元组####################################################################################################
mixed_tuple = (("a" * 10, 3, 4), ['first', 'second', 'third'])

print(mixed_tuple[1])  # ['first', 'second', 'third']
print(mixed_tuple[0])  # ('aaaaaaaaaa', 3, 4)
# if语句中的多个条件#######################################################################################################
math_points = 51
biology_points = 78
physics_points = 56
history_points = 72

my_conditions = [math_points > 50, biology_points > 50,
                 physics_points > 50, history_points > 50]

if all(my_conditions):
    print("Congratulations! You have passed all of the exams.")
else:
    print("I am sorry, but it seems that you have to repeat at least one exam.")
# Congratulations! You have passed all of the exams.

# 在函数中使用全局变量######################################################################################################
string = "string"


def do_nothing():
    global string
    string = "inside a method"


do_nothing()

print(string)  # inside a method
# 可以通过使用defaultdict()，代码将不会报错##################################################################################
from collections import defaultdict

my_dictonary = defaultdict(str)
my_dictonary['name'] = "Name"
my_dictonary['surname'] = "Surname"

print(my_dictonary["age"])
# 打印模块的安装位置#######################################################################################################
import pandas

print(pandas)  # <module 'torch' from '/Users/...'
# 使用uuid模块生成唯一ID###################################################################################################
import uuid

# 根据主机ID、序列号和当前时间生成UUID 是基于mac地址，时间戳，随机数来生成唯一的uuid，可以保证全球唯一性
print(uuid.uuid1())  # 308490b6-afe4-11eb-95f7-0c4de9a0c5af
# 生成一个随机UUID 通过伪随机数得到uuid，具有一定的概率重复（开发使用最多）
print(uuid.uuid4())  # 93bc700b-253e-4081-a358-24b60591076a

# 全局变量################################################################################################################
b = {'1': 1}
c = 0


def change1():
    b['2'] = 2
    # global c
    c = 1


def change2():
    b['2'] = 3


print(b)
print(c)
change1()
print(b)
print(c)
change2()
print(b)
print(c)

# 元组
a = {(1, 2), (3, 4)}
b = {(1, 2), (5, 6)}
a1 = a & b
