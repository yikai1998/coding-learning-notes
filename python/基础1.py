# coding=gbk

"""
python魔法函数
公众文章：手把手PythonAI编程 2024-06-23
"""


# map 对iterable中的每个元素应用该函数，返回一个迭代器
def add_five(x):
    return x+5


numbers = [12, 43, 889, 1235]
numbers = map(add_five, numbers)
print(list(numbers))


# filter 仅保留使函数返回True的元素
def div_five(x):
    return x % 5 == 0


numbers = [15, 213, 24, 50, 93, 98, 85]
div_result = filter(div_five, numbers)
print(list(div_result))


# 列表推导式
numbers = [2, 5, 8, 10]
numbers = [x**2 for x in numbers if x % 2 == 0]
print(numbers)


# 字典推导式
fruits = ['apple', 'strawberry', 'peach', 'banana']
fruits = {x: len(x) for x in fruits}
print(fruits)


# 函数本身作为参数
def f_apply(func, m):
    return func(m)


print(f_apply(lambda x: x**2, 9))


# zip 同时遍历多个列表[截取公共最短长度]
names = ['alice', 'thomas', 'angela', 'someone']
age = [24, 43, 39]
info = zip(names, age)
for x, y in info:
    print(x, y)


# enumerate 遍历的同时返回当前的索引和值
fruits = ['apple', 'banana', 'orange']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)


# set 快速去重 集合支持并集(union)、交集(intersection)、差集等操作，适用于去重和集合逻辑处理
a = [1, 2, 4, 4, 8]
b = [4, 2, 4, 8, 100, 108]
dist_a = set(a)
dist_union = set(a).union(b)
dist_itsx = set(a).intersection(b)
dist_gapA = set(a).difference(b)
dist_gapB = set(b).difference(a)
print(dist_a, dist_union, dist_itsx, dist_gapA, dist_gapB)


# 装饰器 让你可以在不修改原函数代码的情况下，给函数添加新功能
# 装饰器本质上是一个函数，它接收一个函数作为参数，并返回一个新的函数
def my_decorator(func):
    # method1
    # print('something is happening before the function is called')
    # func()
    # print('something is happening after the function is called')

    # method2
    def wrapper():
        print('something is happening before the function is called')
        func()
        print('something is happening after the function is called')
    return wrapper


@my_decorator
def say_hello():
    print('Hello World!')


say_hello()


# yield 生成器 懒加载
# 每当迭代时，生成器的代码只执行到下一个yield语句，暂停并返回值
def count_up_to(n):
    count = 1
    while count <= n:
        yield 'nmd'+str(count)
        count += 1


print(list(count_up_to(5)))


# assert 断言 用于测试某个条件是否为真，如果条件为假，则引发AssertionError异常
def divide(ax, by):
    assert by != 0, '你他妈的不知道除数不能为0啊？'
    return ax / by
# print(divide(10, 0))  # AssertionError: 你他妈的不知道除数不能为0啊？


print(divide(10, 5))


# 解包 星号解包收集剩余元素
a, b, c = [1, 2, 3]
print(a, b, c)
a, *x = [1, 2, 3]
print(a, x)
a, *y, b, c = [1, 2, 3, 49, 18, 3]
print(a, y, b, c)
