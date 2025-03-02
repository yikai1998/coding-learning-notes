# coding=gbk

"""
公众号文章：法纳斯特 2022-01-01
python字符串格式化语法较多，不便记忆，可以在具体需要使用的时候再查询即可；
推荐使用str.format()或f-string格式化处理字符串；
目录：
    1. %格式化
    2. str.format()格式化
    3. f-string格式化
    4. format()
"""


# %格式化

# 简单示例
print("%040.8f 是%s" % (-34.125, '刚学的数字'))  # output: -000000000000000000000000000034.12500000 是刚学的数字

'''  
"%[(name)][flags][width][.precision]type" % 待格式化数据  
%是占位符  
(name)可以用来命名占位符 
flags选填  
    +, 右对齐 正数加正号 负数加负号  
    -, 左对齐 正数无正号 负数加负号  
    空格, 右对齐 正数无正号 负数加负号  
    0, 右对齐 用0填充 正数无正号 负数加负号 负号在0的最左侧  
  

width是你希望这个占位符的占位宽度 如果指定的宽度小于原始宽度则按照原长度输出；如果大于 则可以结合flags里的对齐规则  
.precision是小数点后保留的位数 或字符串切片  
s string 字符串  
d decimal integer 十进制数  
i integer 同d  
u unsigned integer 无符号的十进制数  
f/F float 浮点数 默认6位小数  
e/E exponent 科学计数 默认6位小数  
c character 将十进制数转换为对应的Unicode值 如97转换为a  
%% 转义%从而输出%  
%r representation 调用__repr__魔法方法输出；和%s的差别是 %r会在字符串数据的两侧另外加上''  
** 涉及四舍五入 可以使用python标准模块decimal模块下的Decimal类进行处理 [防止 四舍六入五双, 二进制53位强行截断, ...]  
from decimal import Decimal, ROUND_HALF_UP  
print(Decimal("1.125").quantize(Decimal(".00"), rounding=ROUND_HALF_UP))  >>> 1.13  
'''

# 其他示例
print('my name is %(name)s, l am %(age)d years old' % {'name': 'Yikai Chen', 'age': 25})  # output: my name is Yikai Chen, l am 25 years old
print('repeat my name, %(name)s %(name)s %(name)s' % {'name': 'Yikai Chen'})  # output: repeat my name, Yikai Chen Yikai Chen Yikai Chen


# str.format()格式化

# 简单示例
print('|我叫{}, 今年{}岁.|'.format('汤姆', 18))  # output: |我叫汤姆, 今年18岁.|

''' 
"{[index][:[[fill]align][sign][#][0][width][grouping_option][.precision][type]]}".format() 
index 待格式化的键/索引 如果占位符数量和参数数量不一样，则必须指定索引 
fill 用作填充的字符 可以是任何字符 
align 对齐方式【一般和width互相配合使用】 
    < 左对齐 
    > 右对齐 
    ^ 居中 
    = 右对齐 将符号(+或-)放置在填充字符的左侧，仅对数字类型有效 
sign 有无符号 
    + 正负数都有符号 
    - 正数无符号 负数有符号 
    空格 正数加空格 负数有符号 
width 字段总宽度 
.precision 
    整数型是不允许设置precision的，如果设置了 会被强制转换成浮点数 
    浮点型表示小数点后面显示几位小数 
    字符型表示截取几个字符 
'''

# 其他示例
print('My name is {0}, and my age is {1}.'.format('Zack', 28))  # output: My name is Zack, and my age is 28.
print('My name is {0[0]}, and my age is {0[2]}. My best friend is {0[1]}, who is {1[0]} years old. l love {1[1]}.'.format(('Zack', 'Tom', 28,), (12, 'Jane')))  # output: My name is Zack, and my age is 28. My best friend is Tom, who is 12 years old. l love Jane.
info = {'name': 'Tom', 'age': 100}
print('My name is {name}, and l am {age} years old.'.format(**info))  # output: My name is Tom, and l am 100 years old.
print('|{0:&^10}|'.format('奇迹暖暖'))  # output: |&&&奇迹暖暖&&&|
print('|{0:&=10}|'.format(-296.996))  # output: |-&&296.996|
print('|{0:,}|'.format(31441232334.53))  # output: |31,441,232,334.53|
print('{{{0}}}'.format('1, 2, 3'))  # output: {1, 2, 3}


# f-string格式化
# python3.6之后开始支持f-string字符串，他是str.format()的一个变种，可以有效减少代码量，更加清晰易懂

# 示例
name, age = 'Tom', 18
print(f'My name is {name}, and my age is {age}.')  # output: My name is Tom, and my age is 18.

for p in range(3):
    url = f'https://www.baidu.com/s?wd=python&pn={p*10}&oq=python'
    print(url)

# output:
# https://www.baidu.com/s?wd=python&pn=0&oq=python
# https://www.baidu.com/s?wd=python&pn=10&oq=python
# https://www.baidu.com/s?wd=python&pn=20&oq=python

channel = 'ted'
print(f'l usually watch {channel.upper()} to learn English.')  # output: l usually watch TED to learn English.


# format()
''' 
format()是python的一个内置函数，其使用频率不高，语法和str.format()大同小异，可以结合lambda函数使用或在其它一些特定情况下使用 
# x是需要格式化的数据， formatter是格式化表达式 不需要加{} 
format(X, formatter) 
'''

# 简单示例
nums = [1, 2, 3]
print([format(x, '0>8') for x in nums])  # output: ['00000001', '00000002', '00000003']
