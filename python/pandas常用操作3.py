# coding=gbk

"""
pandas文本处理

公众号文章：法纳斯特 2022-03-02
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'name': ['jordon', 'MIKE@', 'Kelvin', 'xiaoLi', 'qiqi', 'Amei', '99'],
                   'Age': [18, 30, 45, 23, 45, 62, 78],
                   'level': ['high', 'Low', 'M', 'L', 'middle', np.nan, 'low'],
                   'Email': ['jordon@sohu.com', 'Mike@126.cn', 'KelvinChai@gmail.com', 'xiaoli@163.com', np.nan, 'amei@qq.com', 'gg@mail.com']
                   })
print(df)

# 全部小写
df['level'] = df['level'].str.lower()

# 全部大写
df['name'] = df['name'].str.upper()

# 仅首字母大写
df['Email'] = df['Email'].str.title()

# 大小写互换
df['Email'] = df['Email'].str.swapcase()

# 是否为纯字母
df['check'] = df['name'].str.isalpha()

# 是否为纯数字
df['check'] = df['name'].str.isnumeric()
# .str.isdigit()
# str.isdigit() is more restrictive and only checks for strings composed exclusively of digit characters,
# while str.isnumeric() is broader and checks for strings that include any kind of numeric characters, making it suitable for validating more complex numeric formats.

# 是否为字母数字组合
df['check'] = df['name'].str.isalnum()

# 右对齐，宽度为40，其余用*填充
df['name'] = df['name'].str.rjust(40, fillchar='*')

# 居中对齐，宽度为40，其余用*填充
df['name'] = df['name'].str.center(40, fillchar='*')

# 指定字母的数量
df['char'] = df['Email'].str.count('O')

# 字符串长度
df['len'] = df['Email'].str.len()

# 利用正则进行复杂拆分，expand参数可以让拆分的内容展开 形成单独的列；n参数可以指定拆分的位置来控制形成几列
print(df['Email'].str.split(r'[@\.]', expand=True, n=2))

# 文本替换 replace
df['Email'] = df.Email.str.replace('(.*?)@', 'xxx@', regex=True)
df['Email'] = df.Email.str.replace('(.*?)@', lambda x: x.group().upper(), regex=True)
#  When you perform a regular expression search or match, the resulting object contains information about the match. The group method returns the string that was matched by the pattern.
df['Email'] = df.Email.str.slice_replace(start=1, stop=2, repl='###')
df['Email'] = df.Email.str.repeat(repeats=3)

# 文本拼接 cat
print(df.Email.str.cat(sep='-', na_rep='None'))
print(df.name.str.cat(['###']*7).str.cat(df.Email, na_rep='NoEmail'))
print(df.name.str.cat([df.level, df.Email], na_rep='*', sep=' '))

# 文本提取 extract
print(df.Email.str.extract(pat='(.*)@(.*).com'))

# 文本查询 find findall
print(df.Email.str.find('@'))
print(df.Email.str.findall('(.*?)@(.*).com'))

# 文本包含 contains，回布尔值，一般和loc查询功能配合使用
print(df.Email.str.contains('jordon|Com', na='*', case=True))
print(df.loc[df.Email.str.contains('jordon|Com', case=True, na=True)])
# 这里需要注意一下，如果和loc配合使用，注意不能有缺失值，否则会报错。可以通过设置na=False忽略缺失值完成查询
