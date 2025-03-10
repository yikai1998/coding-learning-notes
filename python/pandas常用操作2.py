# coding=gbk

"""
公众号文章:法纳斯特 2022-01-22
整理了90个Pandas案例，强烈建议收藏
"""

import datetime
import pandas as pd
import numpy as np


# 01 如何使用列表和字典创建Series

# 1.1 使用列表创建Series
ser1 = pd.Series([1.5, 2.5, 3, 4.5, 5.0, 6])

# 1.2 使用name参数创建Series
ser2 = pd.Series(['India', 'Canada', 'Germany'], name='Countries')

# 1.3 使用简写的列表创建Series
ser3 = pd.Series(['A']*4 + ['V']*5)

# 1.4 使用字典创建Series
ser4 = pd.Series(
    {'China': 'Beijing',
     'Japan': 'Tokyo',
     'Korea': 'Soul'}
)

# 02 如何使用Numpy函数创建Series
ser5 = pd.Series(np.linspace(1, 100, 5))  # from 1 to 100, totally 5 eqv steps

# 03 如何获取Series的索引和值
ser6 = pd.Series(np.random.normal(size=10))
print(ser6.values)
print(ser6.index)

# 04 如何在创建Series时指定索引
values = ['India', 'Canada', 'Australia', 'Japan', 'Germany', 'France']
ccy_code = ['INR', 'CAD', 'AUD', 'JPY', 'EUR', 'EUR']
ser7 = pd.Series(values, index=ccy_code)
print(ser7)

# 05 如何获取Series的大小和形状
print(ser7.shape)
print(ser7.size)
print(len(ser7))

# 06 如何获取Series开始或末尾几行的数据
print(ser7.head(3))
print(ser7.tail(2))
print(ser7.take([1, 3, 5]))

# 07 使用切片获取Series子集
print(ser7[0:5:2])
print(ser7[5::-1])

# 08 如何创建DataFrame
df = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]
})

# 09 如何设置DataFrame的索引和列信息
df2 = pd.DataFrame(
    data={
        'EmpCode': ['Emp001', 'Emp002'],
        'Name': ['John Doe', 'William Spark'],
        'Occupation': ['Chemist', 'Statistician'],
        'Date of Join': ['2018-01-25', '2018-01-26'],
        'Age': [23, 24]
    },
    index=['first', 'second'],
    columns=['EmpCode', 'Occupation', 'Age', 'Name', 'Date of Join']  # 可以调整顺序，但是名字必须和上面的data内容相符
)

# 10 如何重命名DataFrame的列名称
df.columns = ['Co1', 'Col2', 'Col3', 'Col4', 'Col5']  # 长度必须和df的列数量相等
print(df)

# 11 如何根据Pandas列中的值从DataFrame中选择或过滤行
df = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]
})
print(df.loc[((df['Age'] == 23) & (df.Occupation == 'Chemist')) | (df['Age'] == 24), 'EmpCode':'Occupation'])

# 12 在DataFrame中使用“isin”过滤多行
df3 = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
    'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
    'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
    'Age': [23, 24, 25, 23, 25]
})
print(df3.loc[df3['Age'].isin([24, 25])])
print(df3.loc[~df3['Age'].isin([24, 25])])

# 13 迭代DataFrame的行和列
df3 = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
    'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
    'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
    'Age': [23, 24, 25, 23, 25]
})
for index, col in df3.iterrows():
    # 按行依次输出
    print(index)
    print(col)
    print(col['Occupation'])

# 14 如何通过名称或索引删除DataFrame的列
df3 = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
    'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
    'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
    'Age': [23, 24, 25, 23, 25]
})
df3.drop(['Age', 'Date of Join'], axis=1, inplace=True)  # 基于 列名
df3.drop(df3.columns[[0, 2]], axis=1, inplace=True)  # 基于"列"的index
print(df3)

# 15 向DataFrame中新增列
df3 = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
    'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
    'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
    'Age': [23, 24, 25, 23, 25]
})
df3['City'] = ['London', 'Tokyo', 'Sydney', 'London', 'Toronto']
print(df3)

# 16 如何从DataFrame中获取列标题列表
df3 = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
    'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
    'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
    'Age': [23, 24, 25, 23, 25]
})
print(list(df3))
print(df3.columns.tolist())
print(df3.columns.to_list())

# 17 如何随机生成DataFrame
df_random = pd.DataFrame(np.random.randint(100, size=(10, 6)),
                         columns=list('ABCDEF'),
                         index=['Row-{}'.format(i) for i in range(10)])
print(df_random)

# 18 如何选择DataFrame的多个列
df3 = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
    'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
    'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
    'Age': [23, 24, 25, 23, 25]
})
print(df3[['EmpCode', 'Age', 'Name']])

# 19 如何将字典转换为DataFrame
df3 = {
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
    'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
    'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
    'Age': [23, 24, 25, 23, 25]
}
df3 = pd.DataFrame(df3)
print(df3)

# 20 使用loc进行切片
df3 = pd.DataFrame(
    data={'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
          'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
          'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
          'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
          'Age': [23, 24, 25, 23, 25]},
    index=['first', 'second', 'third', 'fourth', 'fifth']
)
print(df3.loc[['third', 'fifth']])
print(df3.loc['third':'fifth'])

# 21 检查DataFrame中是否为空
df4 = pd.DataFrame()
if df4.empty:
    print('This DataFrame is empty!')

# 22 在创建DataFrame时指定索引和列名称
values = ['Zhabei', 'Hongkou', 'Pudong', 'Putuo']
code = ['ZB', 'HK', 'PD', 'PT']
df5 = pd.DataFrame(
    values,
    index=code,
    columns=['District']
)
print(df5)

# 23 使用iloc进行切片
df3 = pd.DataFrame(
    data={'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
          'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
          'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
          'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
          'Age': [23, 24, 25, 23, 25]},
    index=['first', 'second', 'third', 'fourth', 'fifth']
)
print(df3.iloc[2])
print(df3.iloc[2:4])  # 前闭后开，即第三行 至 第四行
print(df3.iloc[4::-1])  # 从第五行 至 第一行 依次one by one输出

# 24 iloc和loc的区别
# loc索引器可以进行布尔选择；iloc也可以复制他，但不能将它传递给一个布尔系列，必须将布尔系列转换为numpy数组
df3 = pd.DataFrame(
    data={'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
          'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
          'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
          'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
          'Age': [23, 24, 25, 23, 25]},
    index=['first', 'second', 'third', 'fourth', 'fifth']
)
print(df3.loc[df3['Age'] > 24, ['Name', 'Age']])
print(df3.iloc[(df3['Age'] > 24).values, [1, 3]])

# 25 使用时间索引创建空DataFrame
todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date, periods=10, freq='D')
columns = ['A', 'B', 'C']
df5 = pd.DataFrame(index=index, columns=columns)
df5 = df5.fillna(0)
print(df5)

# 26 如何改变DataFrame列的排序
df6 = pd.DataFrame(
    data={
        'Age': [30, 20, 22, 40, 32, 28, 39],
        'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black', 'Red'],
        'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese', 'Melon', 'Beans'],
        'Height': [165, 70, 120, 80, 100, 172, 50],
        'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
        'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']},
    index=['Jane', 'Nick', 'Aaron', 'Penelop', 'Dean', 'Christina', 'Cornelia']
)
df6 = df6.reindex(['State', 'Color', 'Age', 'Food', 'Score', 'Height'], axis=1)
df6 = df6[df6.columns[[3, 2, 1, 4, 5, 0]]]

# 27 检查DataFrame列的数据类型
df3 = pd.DataFrame(
    data={'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
          'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
          'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
          'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
          'Age': [23, 24, 25, 23, 25]},
    index=['first', 'second', 'third', 'fourth', 'fifth']
)
print(df3.dtypes)

# 28 更改DataFrame指定列的数据类型
df3 = pd.DataFrame(
    data={'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
          'Name': ['John Doe', 'William Spark', 'Thomas Edison', 'Mark Johns', 'Harris Mac'],
          'Occupation': ['Chemist', 'Statistician', 'Pilot', 'Teacher', 'Accountant'],
          'Date of Join': ['2018-01-25', '2018-01-26', '2017-06-04', '2019-12-04', '2013-05-30'],
          'Age': [23, 24, 25, 23, 25]},
    index=['first', 'second', 'third', 'fourth', 'fifth']
)
df3['Age'] = df3['Age'].astype(str)
print(df3.dtypes)

# 29 如何将列的数据类型转换为DateTime类型
df7 = pd.DataFrame({
    'Dateofbirth': [
        1349720105,
        1233123123,
        1232343343,
        1254693743,
        1847394574
    ]
})
print(df7.dtypes)
df7['Dateofbirth'] = pd.to_datetime(df7['Dateofbirth'], unit='s')
print(df7)
print(df7.dtypes)

# 30 将DataFrame列从floats转为ints
df8 = pd.DataFrame({
    'DailyExp': [74.5, 25.5, 85.8, 64.3, 78.1]
})
df8['DailyExp'] = df8['DailyExp'].astype(int)
print(df8)

# 31 如何把dates列转换为DateTime类型
# 跳过 .astype('datetime64')

# 32 两个DataFrame相加
df1 = pd.DataFrame({
    'Name': ['张三', '李四', '王五'],
    'Age': [23, 23, 25],
})
df2 = pd.DataFrame({
    'Name': ['赵六'],
    'Job': ['会计']
})
df3 = df1._append(df2, sort=True)
print(df3)

# 33 在DataFrame末尾添加额外的行
df = pd.DataFrame({
    'Name': ['赵六', '董大'],
    'Job': ['会计', '演员']
})
df.loc[len(df)] = ['新人-李四', '自由职业']
print(df)

# 34 为指定索引添加新行
df = pd.DataFrame(
    data={
        'Name': ['赵六', '董大', '赵六'],
        'Job': ['会计', '演员', '杀手'],
    },
    index=['001', '003', '004']
)
df.loc['00'+str(len(df)+2)] = ['新人-李四', '自由职业']
df.loc['002'] = ['新人2-张三', '老师']
print(df.reindex(['001', '003', '004', '005', '002']).sort_index())  # reindex里填的index应当与实际数据index一一对应，从而达到打乱顺序的效果；然后sortindex用来排序

# 35 如何使用for循环添加行
cols = ['zip']
lst = []
zip = 32100

for i in range(10):
    lst.append(zip)
    zip += 1

df = pd.DataFrame(lst, columns=cols)
print(df)

# 36 在DataFrame顶部添加一行
df = pd.DataFrame({
    'Name': ['赵六', '董大'],
    'Job': ['会计', '演员']
})
line = pd.DataFrame({
    'Name': '史蒂夫',
    'Job': '总经理'
}, index=[0])
df = pd.concat([line, df]).reset_index(drop=True)
# df = df.append(line) 不建议这么用，如果是这种场景 pandas官方建议使用concat instead
print(df)

# 37 如何向DataFrame中动态添加行
# 跳过 easy

# 38 在任意位置插入行
# 跳过 easy

# 39 使用时间戳索引向DataFrame中添加行
df = pd.DataFrame(columns=['Name', 'Title'])
df.loc['2014-05-01 18:47:05', 'Name'] = 'Ben Wang'
df.loc['2014-05-01 18:47:05', 'Title'] = 'Manager'
df.loc['2017-12-01 18:47:05', 'Name'] = 'Tom Zhao'
df.loc['2017-12-01 18:47:05', 'Title'] = 'Associate'
line = pd.to_datetime(['2008-09-01 18:23:11', '2018-03-01 18:43:41'], format='%Y-%m-%d %H:%M:%S')
new_rows = pd.DataFrame([['Aaron Fu', 'Director'], ['Ben Chen', 'Analyst']], columns=['Name', 'Title'], index=line)
df = pd.concat([df, new_rows], ignore_index=False)
print(df)

# 40 为不同的行填充缺失值
# 跳过 df.fillna(0)

# 41 append, concat 和 combine_first示例
# 跳过 下面三行语句的执行效果是等价的
df = df1._append(df2).fillna(0)
df = pd.concat([df1, df2]).fillna(0)
df = df.combine_first(df1).combine_first(df2).fillna(0)

# 42 获取行和列的平均值
df = pd.DataFrame([[10, 20, 30, 40], [7, 14,21,28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
print(df.mean()) # 每一列的平均值
print(df.mean(axis=1)) # 每一行的平均值

# 43 计算行和列的总和
# 跳过 df.sum() df.sum(axis=1)

# 44 连接两列
df = pd.DataFrame(columns=['Name', 'Age'])
df.loc[1, 'Name'] = 'Rocky'
df.loc[1, 'Age'] = 21
df.loc[2, 'Name'] = 'Sunny'
df.loc[2, 'Age'] = 22
df.loc[3, 'Name'] = 'Mark'
df.loc[3, 'Age'] = 25
df.loc[4, 'Name'] = 'Taylor'
df.loc[4, 'Age'] = 28
df['Employee'] = df['Name'].map(str) + '-' + df['Age'].map(str)
print(df['Employee'])

# 45 过滤包含某字符串的行
# 跳过 df[df['State'].str.contains('TX')]

# 46 过滤索引中包含某字符串的行
# 跳过 df.index = df.index.astype('str'); df[df.index.str.contains('ane')]

# 47 使用AND运算符过滤包含特定字符串值的行
# 跳过 df.index = df.index.astype('str'); df[df.index.str.contains('ane') & df['State'].str.contains('TX')]

# 48 查找包含某字符串的所有行
# 跳过 同上；  OR的关系用 "|"

# 49 如果行中的值包含字符串，则创建与字符串相等的另一侧 - outdated 20241225
# df = pd.DataFrame({
#     'EmpCode': ['001', '002', '003', '004', '005'],
#     'Name': ['John', 'Doe', 'William', 'Spark', 'Ben'],
#     'Occupation': ['Chemist', 'Accountant', 'Statistician', 'Statistician', 'Programmer'],
#     'Date of Join': ['2018-12-04', '2021-12-12', '2010-09-12', '2010-03-01', '2011-01-03'],
#     'Age': [23, 23, 34, 34, 34]
# })
# df['Department'] = pd.np.where(df.Occupation.str.contains("Chemist"), "化学家",
#                                pd.np.where(df.Occupation.str.contains("Statistician"), "数据分析家",
#                                            pd.np.where(df.Occupation.str.contains("Programmer"), "程序员",
#                                                        "啥都不是")))
# print(df)

# 50 计算pandas group中每组的行数
df = pd.DataFrame([[10, 20, 30, 40],
                   [7, 14, 21, 28],
                   [5, 5, 0, 0],
                   [8, 6, 26, 6],
                   [8, 8, 8, 8],
                   [5, 15, 0, 0]],
                  columns=['Apple', 'Orange', 'Rice', 'Oil'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4', 'Basket5', 'Basket6'])
print(df)
print(df[['Apple', 'Orange', 'Rice', 'Oil']].groupby(['Apple']).agg(['mean', 'count', 'sum']))

# 51 检查字符串是否在DataFrame中
# 跳过 if df['xxx'].str.contains('xx').any()

# 52 从DataFrame列中获取唯一行值
# 跳过 df['xxx'].unique()

# 53 计算DataFrame列的不同值
df = pd.DataFrame({'Age': [30, 30, 29, 29, 23, 22, 12, 33, 23],
                   'Height': [170, 192, 193, 178, 165, 159, 159, 195, 188]})
print(df.Age.value_counts())

# 54 删除具有重复索引的行
df = pd.DataFrame({'Age': [30, 30, 29, 29, 23, 22, 12, 33, 23],
                   'Height': [170, 192, 193, 178, 165, 159, 159, 195, 188]},
                  index=['Female', 'Male', 'Male', 'Unknown', 'Female', 'Male', 'Male', 'Male', 'Female',])
print(df.reset_index().drop_duplicates(subset='index', keep='first').set_index('Height')) # 先基于index做去重，只保留第一次出现的值，然后将height列作为新的index（原index列则自动变成了column）

# 55 删除某些列具有重复值的列
df = pd.DataFrame({'Age': [30, 30, 29, 29, 23, 22, 23, 33, 23],
                   'Height': [170, 192, 178, 178, 165, 159, 159, 195, 188]},
                  index=['Female', 'Male', 'Male', 'Unknown', 'Female', 'Male', 'Female', 'Male', 'Female',])
print(df.reset_index().drop_duplicates(subset=['Age','Height'], keep='last').set_index('index'))

# 56 从DataFrame单元格中获取值
# 跳过 df.loc['行(index名)', '列(column名)']

# 57 使用DataFrame中的条件索引获取单元格上的标量值
df = pd.DataFrame({'Age': [30, 30, 29, 29, 23, 22, 23, 33, 23],
                   'Height': [170, 192, 178, 178, 165, 159, 159, 195, 188]},
                  index=['Female', 'Male', 'Male', 'Unknown', 'Female', 'Male', 'Female', 'Male', 'Female',])
print(df.loc[df['Age']==23, 'Height'].values[2]) #获取符合条件的第三个人的身高

# 58 设置DataFrame的特定单元格值
# 跳过 df.iat[从0开始的第几行, 从0开始的第几列] = 某个你想设定的新值

# 59 从DataFrame行获取单元格值
# 跳过 df.loc[df['Age]==30, 'Height'].tolist()

# 60 用字典替换DataFrame列中的值
df_0 = pd.DataFrame({'Location': ['Shanghai', 'Beijing', 'Jiangsu', 'Shandong', 'Guangdong']},
                    index=['Jane', 'Tom', 'Alex', 'Thomas', 'Bella'])
print(df_0)
helper_dic = {
    'Shanghai': 'Shanghai',
    'Beijing': 'Beijing',
    'Jiangsu': 'Nanjing',
    'Shandong': 'Qingdao',
    'Guangdong': 'Shenzhen'
}
df_1 = df_0.replace(
    {'Location': helper_dic}
)
print(df_1)

# 62 处理DataFrame中的缺失值
# 跳过 df.isnull() // df.notnull()

# 63 64 删除包含任何缺失数据的行、列
# 跳过 df.dropna() // df.dropna(1)

# 65 按降序对索引值进行排序
# 跳过 df.sort_index(ascending=False)

# 66 按降序对列进行排序
# 跳过 df.sort_index(axis=1. ascending=False) # 效果是各列将按照列名从左至右降序排列

# 67 使用 rank方法查找DataFrame中元素的排名
df = pd.DataFrame([[10, 120, 30, 40], [7, 14, 221, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
print(df)
print(df.rank(axis=1, ascending=False)) # 详细方法可以参考内置的使用手册

# 68 在多列上设置索引 [将多列设置为索引]
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
df = employees.set_index(['Occupation', 'Age'])
print(df[2:5])
print(df.sort_index(ascending=True))

# 69 确定DataFrame的周期索引和列
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
# pidx = pd.period_range('2015-01-01', periods=6, freq='w')
pidx = pd.period_range('2015-01-01', periods=6, freq='+8d')
df = pd.DataFrame(values, index=pidx, columns=['Country'])
print(df)

# 70 导入 CSV 指定特定索引
# 简单 跳过

# 71 将 DataFrame 写入 csv
# 跳过 df.to_csv('test.csv', encoding='utf-8', index=True)

# 72 使用 Pandas 读取 csv 文件的特定列
# 跳过

# 73 Pandas 获取 CSV 列的列表
# 跳过

# 74 找到列值最大的行
df = pd.DataFrame([[100, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])
print(df)
tt = df['Apple'].idxmax()
print(df.loc[tt])

# 75 使用查询方法进行复杂条件选择
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print(df)
print(df.query('Apple > 8 & Banana > 20').index.values)

# 76 检查 Pandas 中是否存在列
# 跳过 if 'Apple' in df.columns:

# 77 为特定列从 DataFrame 中查找 n-smallest 和 n-largest 值
# 跳过 print(df.nsmallest(2, ['Apple']))
# 跳过 print(df.nlargest(2, ['Apple']))

# 78 从 DataFrame 中查找所有列的最小值和最大值 （不一定是源自同一行）
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
print(df[['Apple', 'Orange', 'Banana', 'Pear']].min())
print(df[['Apple', 'Orange', 'Banana', 'Pear']].max())

# 79 在 DataFrame 中找到最小值和最大值所在的索引位置
# 跳过 和74重复

# 80 计算 DataFrame Columns 的累积乘积和累积总和
# 跳过 print(df[['Apple', 'Orange', 'Banana', 'Pear']].cumprod())
# 跳过 print(df[['Apple', 'Orange', 'Banana', 'Pear']].cumsum())

# 81 汇总统计
# 跳过 .describe()

# 82 查找 DataFrame 的均值、中值和众数
# 跳过

# 83 测量 DataFrame 列的方差和标准偏差
# 跳过

# 84 计算 DataFrame 列之间的协方差
# 跳过

# 85 计算 Pandas 中两个 DataFrame 对象之间的相关性
# df1.corr() # calculating the correlation of one dataframe columns
# df2.corrwith(other=df1) # calculating the correlation between two dataframe

# 86 计算 DataFrame 列的每个单元格的百分比变化
print(df[['Apple']].pct_change()[:3]) # Percent change at each cell of a Column
print(df.pct_change()[:5]) # Percent change at each cell of a DataFrame

# 87 在 Pandas 中向前和向后填充 DataFrame 列的缺失值
# 跳过 df.ffill()
# 跳过 df.bfill()

# 88 在 Pandas 中使用非分层索引使用 Stacking
# 89 使用分层索引对 Pandas 进行拆分
df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])
print(df)
print(df.stack(level=-1))  # Because the Index here has only 1 level，n_th; 等于是把列的维度塞到index的“栈”里
print(df.stack(level=-1).unstack(level=-1))
print(df.stack(level=-1).unstack(level=-2))

# 90 Pandas 获取 HTML 页面上 table 数据
# 跳过 Pandas 获取 HTML 页面上 table 数据
