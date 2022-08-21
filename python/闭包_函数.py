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
