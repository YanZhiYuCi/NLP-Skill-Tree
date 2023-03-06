# -*- coding: UTF-8 -*
import os
import sys
from typing import List, Dict, Set, Tuple, Any, Optional, Union
import json
import time

# 第三方库
from loguru import logger

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# 载入自定义模块


from abc import ABC, abstractmethod


# ex0713.py 子类重写父类的方法
class Animal:
    def __init__(self, isAnimal):
        self.isAnimal = isAnimal

    def run(self):
        print("父类 Animal 通用的 run()方法")

    def show(self):
        print("父类 Animal 的 show() 成员方法")


class Cat(Animal):
    a = 1
    b = 2

    def __init__(self, isAnimal, age, gender):
        super().__init__(isAnimal)
        print("子类的构造方法")
        self.age = age
        self.gender = gender

    def run(self):  # 方法重写
        super().run()  # 使用 super() 方法调用父类方法
        print("子类 Cat 重写 run() 成员方法")

    def __repr__(self):
        # 默认情况下print(cat) 返回的 类名+object at+内存地址 ” <__main__.Animal object at 0x0000028E288D8940>
        # 通过重写类的 __repr__() 方法即可。事实上，当我们输出某个实例化对象时，其调用的就是该对象的 __repr__() 方法，输出的是该方法的返回值
        # return {1:False} 必须返回的是字符串
        return "Cat[age={}; gender={}]".format(self.age, self.gender)


ani = Animal(False)
print(ani)
ani.show()

cat = Cat(True, age=1, gender='female')
print(cat)
cat.run()
object_variation: Dict = cat.__dict__
print(object_variation)
class_variation: Dict = Animal.__dict__
print(class_variation)
print(hasattr(cat, 'age'))  # hasattr() 函数用来判断某个类实例对象是否包含指定名称的属性或方法
print(hasattr(cat, 'run'))
# getattr() 函数获取某个类实例对象中指定属性的值。没错，和 hasattr() 函数不同，该函数只会从类对象包含的所有属性中进行查找
print(getattr(cat, "age", None))
print(getattr(cat, "nation", None))

print('=' * 80)


class Shape(ABC):
    @abstractmethod
    def getArea(self): pass  # 定义获取面积的抽象方法

    def __init__(self, area):  # 定义shape的构造方法
        print("In ShapeInit")
        self.area1 = area  # 定义基类的实例变量area1，子类中直接继承

    def getArea2(self): return self.area1  # 定义getArea2方法，该方法有抽象基类实现，子类继承


class Output(ABC):
    def __init__(self):
        print("In OutputInit")

    def output(self): print('output')  # 输出实例自定义属性


# 多继承
class Circle(Shape, Output):
    def __init__(self, radius):
        # super().__init__(9)  # 调用超类方法的构造函数
        Shape.__init__(self, 1)
        Output.__init__(self)
        self.radius = radius
        self.area = 3.14 * self.radius * self.radius
        self.girth = 6.28 * self.radius

    def getArea(self): return self.area

    def getGirth(self): return self.girth

    def output(self):  # 输出实例的内容
        print("area={:.2f},girth={:.2f}".format(self.area, self.girth))
        Output.output(self)


cir = Circle(10)
cir.getArea2()
cir.output()
