# coding=gbk

"""
公众号文章:早起python 2023-04-14

在数据分析和数据建模的过程中需要对数据进行清洗和整理等工作，有时需要对数据增删字段。下面为大家介绍pandas对数据的复杂查询、数据类型转换、数据排序、数据的修改、数据迭代 以及 函数的使用
"""

import pandas as pd

# 源数据
df = pd.read_excel('模拟数据.xlsx', sheet_name='期末考试')
print(df)

# 01 复杂查询

# 1.1逻辑运算
'''
Q1成绩大于36 --> df.Q1 > 36
Q1成绩不小于60分且为C组成员 --> ~(df.Q1<60) & (df['team']=='C')
切片[], .loc[], iloc[] 均支持上文所介绍的逻辑表达式
'''

# 1.2逻辑筛选数据
print(df[df.分数 > 98])  # 分数大于98的所有记录
print(df[~(df['班级'] == '2班')])  # 班级不为2班的所有记录
print(df[df['分数'] > df['生涯平均分']])  # 分数大于生涯平均分的所有记录
print(df.loc[(df.分数 > 95) & (df['班级'] == '1班'), '生日':'科目'])  # 分数大于95且班级是1班的生日至科目字段

# 1.3函数筛选
print(df.姓名[lambda s: min(s.index)])  # 最小索引位置对应的姓名
print(max(df.分数.index))  # 最大索引值
print(df.姓名[df.index == 20])  # 索引=20对应的姓名
print(df[df.index == 20])  # 索引=20对应的所有记录

# 1.4比较函数
print(df[df.班级.eq('4班')])  # 相当于df[df.班级 == '4班']
print(df[(df.班级.eq('4班')) & (df.科目.eq('英文'))])
# df.ne() #!=
# df.le() #<=
# df.lt() #<
# df.ge() #>=
# df.gt() #>

# 1.5查询df.query()
print(df.query("分数>90 and (班级=='1班' or 班级=='2班')"))  # 直接写sql里的where语句
print(df.query("分数>90 and 班级 in ('1班','8班')"))  # 直接写sql里的where语句
# 支持使用@符引入变量，如：a=df.分数.mean(); df.query('分数>@a+1')
# 使用isin()方法检查'分数'列中的值是否在列表a中

# 1.6筛选df.filter()
print(df.filter(items=['姓名', '班级', '科目']))  # 选择特定某三列
print(df.filter(regex='分', axis=1))  # 列名里含有"分"的列
print(df.filter(regex='分$', axis='columns'))  # 列名里以"分"结尾的列
print(df.filter(regex='2$', axis=0))  # 索引index以2结尾的行
print(df.filter(items=['班级']).filter(like='2', axis=0))  # 索引index里含2的 且只输出”班级“列
print(df.filter(items=['姓名']).filter(regex='^2', axis=0))  # 索引index以2开头的 且只输出”姓名“列

# 1.7按数据类型查询
print(df.select_dtypes(include=['int', 'datetime']))  # 只取整数型和日期型
print(df.select_dtypes(exclude=['int', 'datetime']))  # 不取整数型和日期型


# 02 数据类型转换

# 2.1推断类型
print(df.infer_objects().dtypes)  # 目前dataframe下被自动转换的数据类型

# 2.2指定类型 #跳过

# 2.3类型转换astype()
df2 = df.年龄.astype(float)  # 将年龄该列变成浮点型数据，此法下打印只会针对该列
df3 = df.astype({'年龄': 'float', '班级MVP': 'int32'})  # 将年龄该列变成浮点型数据，并将MVP字段从T/F转为整数型数据，此法下打印会输出所有的列

# 2.3转为时间类型 #跳过


# 03 数据排序

# 3.1索引排序 #跳过

# 3.2数值排序 sort_values()
print(df.分数.sort_values(ascending=False))  # 默认升序 依照降序输出“分数”列
print(df.sort_values('生日'))  # 默认升序 依照生日列的升序输出所有记录
print(df.sort_values('生日')[['班级', '姓名', '分数']])  # 默认升序 依照生日列的升序输出特定字段
print(df.sort_values(by=['班级', '分数'], ascending=[True, False])[['班级', '姓名', '分数']])  # 多重排序，输出特定字段

# 3.3混合排序 #跳过

# 3.4按值大小排序nsmallest()和nlargest()
print(df.nlargest(2, '分数'))  # 分数最高的两位的全部记录
print(df.nlargest(2, ['分数', '生涯平均分']))  # 多重排序


# 04 添加修改

# 4.1修改数值
print(df.loc[6, '姓名'])  # 输出为 杜兰特
df.loc[6, '姓名'] = '奥尼尔'
print(df.loc[6, '姓名'])  # 输出为 奥尼尔
df[df.分数 == 100] = 40  # 分数为100的记录，其整行全部替换成40

# 4.2替换数据
print(df.replace(90, 99.99))  # 将整个表中的90全部替换成99.99
print(df.replace(['语文', '英文'], '地理'))  # 将整个表中的【语文，英文】全部替换成 地理
print(df.replace(['语文', '英文'], ['体育', '政治']))  # 将整个表中的【语文，英文】相应替换成【体育，政治】
print(df.replace({'分数': [100, 90], '期中分数': 100}, 150))  # 将分数列中的100,90 以及 期中分数列中的100 均替换成150
print(df.replace({'分数': {100: 150, 90: 120}}))  # 将分数列中的100替换成150， 90替换成120

# 4.3填充空值
print(df.fillna('none'))  # 将空值全部改成'none'
print(df.fillna(method='ffill'))  # 将空值全部用前一行的值填充; ffill为前向填充，bfill是后向填充

valuemap = {'分数': 60, '期中分数': 80, '生涯平均分': 80}
print(df.fillna(value=valuemap))  # 自定义为各列空值填充不同的缺失值
print(df.fillna(value=valuemap, limit=2))  # 只填充两次(行)

# 4.4修改索引名
print(df.rename(columns={'分数': '期末得分', '入学时间': '选秀日期'}))  # 方法1：对列名进行修改
print(df.rename(mapper={'班级': '队名', '科目': '选课'}, axis='columns'))  # 方法2：对列名进行修改
print(df.rename(index={0: 'No.1', 1: 'No.2'}))  # 对行的索引名称进行修改
print(df.rename(index=float))  # 对索引的数据类型进行修改

# 4.5增加列
df['性别'] = '男'
print(df)  # 增加一列性别，都是“男”
df['进步或退步'] = df['分数'] - df['期中分数']
print(df)  # 增加一列，结算过程是两列相减
df['total'] = df.loc[:,  '分数':'期中分数'].apply(lambda x: sum(x), axis='columns')
print(df)  # 增加一列，结算过程是两列相加

df.loc[df.生涯平均分 >= 95, ['评价']] = '巨星'
print(df)  # 增加一列，叫“评价”，展现逻辑是 如果生涯平均分列大于等于95 则标记“巨星”；不满足的会自动标记NaN

# 4.6插入列
df.insert(3, '性别2', '男')
print(df)  # 在第四列左边插入一列"性别"，值为“男”
df.insert(3, '文科', (df.科目 == '语文') | (df.科目 == '英文'))
df.loc[df['文科'], '文科'] = '是'
df.loc[df['文科'] == False, '文科'] = '否'
print(df)  # 在第四列左边插入一列"文科"，如果科目是语文或英文 则显示“是”， 否则显示“否”

# 4.7指定列
df = df.assign(期望成绩=lambda d: d.期中分数*1.01+1)
print(df)  # 使用lambda函数新增列

df = df.assign(状态标记=(df.期中分数 <= df.分数).map({True: '不错，保持了/进步了', False: '退步了'}))
print(df)  # 新增一列，基于字段的比较，然后映射文案
# df.assign里可以写多个=，实现多列的增加

# 4.8执行表达式 跳过

# 4.9增加行
df.loc[40] = ['9班', '1996-01-25', '2014-05-23', '韦德', '历史', 100, 100, 92, 24, True]  # 新增一条索引为40的数据
df.loc[50] = {'姓名': '纳什', '分数': 96}  # 指定列和行索引添加数据，如果没有列名数据则值为NaN
df.loc[len(df)] = {'姓名': '罗伊', '分数': 96}  # 方法1 自动在尾索引按序添加一条新记录
df.loc[df.shape[0]] = {'姓名': '本内特', '分数': 97}  # 方法2 自动在尾索引按序添加一条新记录

# 4.10追加合并
df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[101, 102, 103], [103, 104, 105]], columns=list('ABC'))
print(df.append(df2).reset_index())  # 类似UNION ALL的向下拼接，如果值有缺失则显示NaN

# 4.11删除
print(df.pop('姓名'))
print(df)  # 删除了“姓名”列

# 4.12删除空值
print(df.dropna())  # 一行中只要有至少一个NaN，就会删掉这行
print(df.dropna(axis='columns'))  # 一列中只要有至少一个NaN，就会删掉这列
print(df.dropna(how='all', axis=1))  # 将全为NaN的列删除
print(df.dropna(thresh=9))  # Keep only the rows with at least 9 non-NA values.


# 05 高级过滤 跳过


# 06 数据迭代

# 6.1迭代series
for i in df.姓名:
    print(i)  # 循环打印指定的某列

for i, n, q, t in zip(df.index, df.班级, df.姓名, df.年龄):
    print(i, n, q, t)  # 循环打印指定的几列

# 6.2df.itertuples()
for i in df.itertuples():
    print(i, i[2], i[4])  # 以行为维度循环输出，形式为元组tuple

# 6.3df.iterrows()
for index, i in df.iterrows():
    print(index, i['姓名'])  # 以行为维度循环输出，可以指定相应的列字段值

# 6.4df.items()
for label, i in df.items():
    print(label)  # 列名
    print(i[:3], end='\n\n')  # 以列为维度循环输出，可以指定几行

# 6.5按列迭代
for i in df:
    print(i)  # 简单粗暴的循环输出df中的所有列名


# 07 函数应用

# 7.1pipe() 跳过

# 7.2apply()
df = df.年龄.apply(lambda x: x+100)  # 把函数应用到某列

# 7.3applymap()
def mylen(x):
    return len(str(x))
df = df.applymap(lambda x: mylen(x))  # 把函数应用到所有元素中

# 7.4map()
df['班级'].map({'1班': '火箭班A', '2班': '奥数班B', '8班': '艺术班C', })  # 枚举替换，没被枚举到的元素就变成NaN

# 7.5agg()
print(df.agg({'分数': ['max', 'min'], '生涯平均分': ['mean', 'sum']}))  # 自己指定序列做聚合
print(df.groupby(['班级', '科目']).agg(['mean', 'max'])['期中分数'])  # 自定义分组后的聚合

# 7.6transform 跳过

# 7.7copy() 跳过
