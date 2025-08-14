# coding=gbk

"""
公众号：科学随想录 2023-08-13

**kwargs的原理
**kwargs是python中的一种语法，它允许函数接受任意数量的关键字参数，这些参数在函数内部作为字典dic处理，字典的键是参数名，值是传递给函数的参数值；
"""


# 简单示例
def greet(**kwargs):
    print(kwargs.items())
    for key, value in kwargs.items():
        print(f'{key}: {value}')


greet(name='Alice', age=29, height=160.9, male=False, mailbox=None)
# output
# dict_items([('name', 'Alice'), ('age', 29), ('height', 160.9), ('male', False), ('mailbox', None)])
# name: Alice
# age: 29
# height: 160.9
# male: False
# mailbox: None


# **kwargs的应用场景
# **kwargs在各种场景下都非常有用，尤其是在处理复杂的函数参数和创建灵活的api时

# 动态处理参数
# 当你不确定函数要接受多少参数，或者参数的数量会随着时间的推移而变化时，可以使用**kwargs，你可以随时添加新的参数，而无需修改函数定义
def create_user(**kwargs):
    d = {}
    for key, value in kwargs.items():
        d[key] = value
    return d


user = create_user(name='Tom', age=29, country='USA', occupation='Engineer')
print(user)
# output: {'name': 'Tom', 'age': 29, 'country': 'USA', 'occupation': 'Engineer'}


# 扩展现有函数
# 假设你有一个函数，该函数已经接受了一些参数，但现在你想要扩展这个函数，以便它可以接受更多的参数
def employee_details(name, age, **kwargs):
    print(f'Name: {name}')
    print(f'Age: {age}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')


employee_details('Alice', 33, country='China', height=192)
# output
# Name: Alice
# Age: 33
# country: China
# height: 192


# 与*args一起使用
# 可以同时使用*args和**kwargs，以接受任意数量的位置参数和关键字参数
def func(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        
        
func('arg1', 'arg2', 3, weather='spring', time='a.m', speed=5)
# output
# arg1
# arg2
# 3
# weather: spring
# time: a.m
# speed: 5


# temp sample
def build_model(blood, magic, gender, name='dead king', *args, **kwargs):
    sp = kwargs.get('speed')
    print(blood)
    print(magic)
    print(gender)
    print(name)
    print(args)
    print(kwargs)
    print(sp)
    return 0


build_model(300,  150, 'M', 'mountain king', 'apple', 'work work', speed=100, attack=999)
# 300
# 150
# M
# mountain king
# ('apple', 'work work')
# {'speed': 100, 'attack': 999}
# 100
