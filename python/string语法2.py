# coding=gbk
import re

"""
公众号文章：法纳斯特 2022-01-16
31个最重要的内置字符串方法
"""

# slicing切片 按照一定条件从列表或元组中取出部分元素
wording = ' hello '
print(wording[:])  # hello
print(wording[1:6])  # hello

# strip()方法用于一处字符串头尾指定的字符或字符序列，默认是空格和换行符
print(' hello '.strip())  # hello
print('#hello###'.strip('#'))  # hello
print('### #hello ###'.strip('#'))  # #hello 【指定内容不在头尾部时，不会被去除】
print('\n \t hello man! \n'.strip())  # hello man!
print('\n \t hello man! \n'.strip('\n'))  #  	 hello man!

# strip()方法还可以剥离参数值的所有组合，从最外层的头尾开始被剥离，直到到达一个不包含在字符集中的字符串字符为止
print('www.baidu.com!!'.strip('m!o.cw'))  # baidu
# rstrip, lstrip 同上原理

# removeprefix() 移除前缀，但不会把字符集中的字符串进行逐个匹配
print('python hello python'.removeprefix('py'))  # thon hello python
# removesuffix() 同上原理，移除后缀

# replace() 将字符串中的内容替换成指定内容
print('string methods in python'.replace(' ', '-'))  # string-methods-in-python

# re.sub()
print(re.sub('\s+', '-', 'substitution    methods in python'))  # substitution-methods-in-python

# split() 对字符串做分隔处理，返回一个列表，默认按照空格
print('string in python'.split())  # ['string', 'in', 'python']
print('string in python'.split(','))  # ['string in python']
print('string in python'.split(' ', maxsplit=1))  # ['string', 'in python']
# rsplit()是从右侧开始对字符串进行分隔

# string.join(seq) 是以string作为分隔符 将seq中所有的元素合并为一个新的字符串，必须是字符
print('-'.join(['my', 'age', 'is', '19']))  # my-age-is-19

# upper(), lower(), capitalize()
# 将字符串中的字母全部转换为 大写、小写、仅首字母大写
print('aApLE'.capitalize())  # Apple

# swapcase() 颠倒字符串中的字母大小写
print('Hello World'.swapcase())  # hELLO wORLD

# islower(), isupper() 判断字符串中的所有字母是否都为小写或大写
print('hello worlD'.islower())  # False
print('hello world!'.islower())  # True

# isalpha() 字符串中至少有一个字符，且所有字符都是字母
print('hello'.isalpha())  # True
print('hello13'.isalpha())  # False
print('hello '.isalpha())  # False
print(''.isalpha())  # False

# 同理，isnumeric() 字符串中至少有一个字符，且字符串中只包含数字字符
print('12323'.isnumeric())  # True
print('12323 '.isnumeric())  # False
print('12323a'.isnumeric())  # False
print(''.isnumeric())  # False

# 同理，isalnum() 字符串中至少有一个字符并且所有字符都是字母或数字
print('hello123'.isalnum())  # True
print('hello 123'.isalnum())  # False
print(''.isalnum())  # False

# count() 返回指定内容在字符串中出现的次数
print('hello world'.count('l'))  # 3
print('hello world'.count('ll'))  # 1
print('machine learning A'.count('A'))  # 1

# find() 检测指定内容是否被包含在字符串中，可以自定义开始的范围；如果包含，则返回开始的索引值，否则直接返回-1
print('machine learning A'.find('A'))  # 17
print('machine learning A'.find('a', 2))  # 10
print('machine learning A'.find('a', 11))  # -1

# rfind() 同理，从右边开始找，即 返回字符串最后一次出现匹配的位置，如果没有找到就返回-1
print('machine learning A'.find('a', 1))  # 1
print('machine learning A'.rfind('a', 1))  # 10

# startswith(), endswith() 检查字符串是否以指定内容开头或结束
print('Ben'.startswith('b'))  # False

# partition 强制将字符串拆成3元素元组；填入的参数被作为中间元素；如果填的str不被包含，则string本身将被作为第一个参数

print('hello world today is my birthday'.partition('is'))  # ('hello world today ', 'is', ' my birthday')
print('hello world today is my birthday'.partition('is my'))  # ('hello world today ', 'is my', ' birthday')
print('hello world today is my birthday'.partition('iss'))  # ('hello world today is my birthday', '', '')

# center 返回一个原字符串居中，并填充至规定长度的新字符串
print('Python'.center(20, '~'))  # ~~~~~~~Python~~~~~~~

# 同理，ljust(), rjust() 左对齐 右对齐
print('Python'.rjust(20, '~'))  # ~~~~~~~~~~~~~~Python

# f-string
print(f'9 * 4 = {9 * 4}')  # 9 * 4 = 36

# zfill() 返回长度为width的字符串，右对齐，左侧填充0
print('apple'.zfill(3))  # apple
print('apple'.zfill(13))  # 00000000apple
