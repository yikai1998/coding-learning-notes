# coding=gbk

"""
公众号：法纳斯特 2023-03-18
"""

# 列表stepping
# step参数可以分割你的列表，也可以用来反转列表
data = [10, 20, 30, 50, '90', 999]
print(data[::2])  # [10, 30, '90']
print(data[::-1])  # [999, '90', 50, 30, 20, 10]

# find方法可以查找字符串中任何字符的任何起始索引号
x = 'python'
print(x.find('thon'))  # 2
print(x.find('ton'))  # -1

# iter()方法对于没有任何循环帮助的迭代列表有很多用
x = [1, 3, 5, 6, 0, 25]
y = iter(x)
print(next(y))  # 1
print(next(y))  # 3
print(next(y))  # 5

# 文档测试
# doctest可以让你测试你的功能并显示你的测试报告，比如你想检查下面的示例，需要在三引号中编写一个测试参数
# from doctest import testmod
# def Mul(x, y) -> int:
#     """
#     this function is used  for calcultion xxxx
#     >>> Mul(14, 5)
#     10
#
#     >>> Mul(4, 5)
#     20
#
#     >>> Mul(20, 100)
#     40
#     """
#     return x * y
#
# testmod(name='Mul', verbose=True)


# Yield声明
# 工作方式类似于return语句，但他不会终止函数并返回，而是返回到它返回给调用者的点
def yield_func():
    print('first yield...')
    yield 'one'

    print('second yield...')
    yield 'two'

    print('third yield...')
    yield 3


print(list(yield_func()))
# first yield...
# second yield...
# third yield...
# ['one', 'two', 3]
for i in yield_func():
    print('>>', i)
# first yield...
# >> one
# second yield...
# >> two
# third yield...
# >> 3

# 处理字典的缺失值 - 如果访问的键并不存在于字典中，这会导致报错；为了解决这个问题，我们可以使用get()来替代括号方法
dic_1 = {
    'x_factor': 10,
    'y_factor': 100
}
# print(dic_1['z_factor']) # KeyError: 'z_factor'
print(dic_1.get('z_factor'))  # None

# Python是支持含有for和while循环的else的，当循环完成其迭代 且没有任何中断时，将执行此else语句
for x in range(10):
    print(x)
else:
    print('Loop completed with no exceptions.')  # 被执行

for x in range(10):
    print(x)
    if x == 5:
        break
else:
    print('Loop completed with no exceptions.')  # 未被执行

# 设置递归限制
# import sys
# sys.setrecursionlimit(50)
# print(sys.getrecursionlimit())  # 50
# def foo(n):
#     print(n)
#     n += 1
#     foo(n)
# foo(1)  # RecursionError: maximum recursion depth exceeded

# 条件参数 - 条件赋值功能用三元运算符，可以根据特定条件在变量中赋值
x = 'True' if 6 > 4 else 'False'
print(x)  # True
x = 'True' if 6 < 4 else 'False'
print(x)  # False


# 参数拆包
def pac_func(a, b):
    print(a, b)
    
    
list_1 = [100, 200]
dic_1 = {
    'x': 100,
    'y': 101,
}
pac_func(*list_1)  # 100 200
pac_func(*dic_1)  # x y
pac_func(**dic_1)  # 100 101

# 多行字符串
words = "锄禾日当午" \
        "汗滴禾下土" \
        "谁之盘中餐" \
        "粒粒皆辛苦"
print(words)  # 锄禾日当午汗滴禾下土谁之盘中餐粒粒皆辛苦
