# 当前项目名:machaoyangNLP
# 当前文件名:闭包_函数 
# 当前集成开发环境:PyCharm	
# 当前用户的登录名:Administrator
# 当前作者:马朝阳
# 当前系统日期:2022/8/21
# 当前系统时间:15:44

"""
基本数据类型如int，float,字符串在闭包中不报错UnboundLocalError: local variable 'c11' referenced before assignment
字符串时因为字符串为不可修改类型，一旦赋值不可修改，直接将修改后的结果赋值给原变量
其实是基本数据类型一般使用时，都是sum = 1.0 这样直接赋值的，而不是像列表一样追加元素后者删除元素，所以即使时列表，在内层闭包内直接赋值，也会
在外层不起作用
"""


# def c1():
#     c11 = 0
#
#     def c2():
#         c11 = max(c11, 2)
#         print('inner:{}'.format(c11))
#
#     c2()
#     print('out:{}'.format(c11))
#     return c11
#
#
# c1()

# 当在闭包内重新赋值后UI然可以使用，但是其实是局部变量，没有起到全局变量的作用
def c1():
    c11 = 0

    def c2():
        c11 = 1
        print('inner:{}'.format(c11))

    c2()
    print('out:{}'.format(c11))
    return c11


c1()


# 当为列表,字典，自定义类等复杂数据类型时可以使用
def c1():
    c11 = [1, 3]

    def c2():
        c11.append(5)
        print('inner:{}'.format(c11))

    c2()
    print('out:{}'.format(c11))
    return c11


c1()


# 二次赋值
def c1():
    c11 = [1, 3]

    def c2():
        c11 = [1, 3, 5]
        print('inner:{}'.format(c11))

    c2()
    print('out:{}'.format(c11))
    return c11


print('二次赋值')
c1()


# 当需要在外层函数维护一个int或者float，可以使用1个列表，列表元素个数为1
def c1():
    c11 = [1]

    def c2():
        c11[0] = 5
        print('inner:{}'.format(c11))

    c2()
    print('out:{}'.format(c11))
    return c11


c1()

# 形参实参一样不影响，但是假如说他们的值是复杂数据类型，例如列表、字典、集合、class(不包括整int、float、string、Tuple)##################
# 在函数内修改在函数外同样有效，因为复杂数据类型是对同一内存地址的别名所以改一个其他名字也会改变，可以使用d_c=copy.deepcopy(d)来避免
c = [1, 2, 3]


def f(c):
    print(c)
    c.append(4)
    print(c)
    return c


print(c)
c1 = f(c)
print(c1)  # c1 和c均变化了
print(c)

c = [1, 2, 3]


def f_1(c_):
    print(c_)
    c_.append(4)
    print(c_)
    return c_


print(c)
c1 = f_1(c)
print(c1)  # c1 和c均变化了
print(c)

c = [1, 2, 3]
c_2 = [1, 2, 3, 4]


def f_2(c):
    print(c)
    c.append(5)  # 此时函数内的c为[1,2,3,4,5],但是函数外的c依然为[1,2,3],这个函数返回后这个函数内的c消失，函数外的c依然为[1,2,3]
    print(c)
    return c


print(c)
c1 = f_2(c_2)
print(c1)  # c1 和c均变化了
print(c)

c_10 = [1, 2, 3]
c_11 = [1, 2, 3, 4]


def f_3(c_12):
    print(c_12)
    c_12.append(5)  # 此时函数内的c为[1,2,3,4,5],但是函数外的c依然为[1,2,3],这个函数返回后这个函数内的c消失，函数外的c依然为[1,2,3]
    print(c_12)
    return c_12


c_13 = f_3(c_10)  # 不进入f_3的话根本看不到c_12这个变量
c_14 = ''


a = [1, 2, 3]
e = a
c = a[:]  # 切片是重新在内存增加了空间，新建了变量等价于copy.deepcopy
d = a[:]
a_id = id(a)
c_id = id(c)
d_id = id(d)
e_id = id(e)
print(a == c)
print(a is c)

b = [a, a]  # b [[1, 2, 3], [1, 2, 3]]
a.append(4)  # b [[1, 2, 3, 4], [1, 2, 3, 4]]
