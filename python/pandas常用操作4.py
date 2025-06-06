# coding=gbk

"""
公众号文章:法纳斯特 2022-11-14
尝试用python实现对excel的操作，增强数据处理能力
"""


import pandas as pd
import os

pd.set_option('display.max_rows', 9999)
pd.set_option('display.max_columns', 9999)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

home = os.path.join(os.path.expanduser('~'), 'PycharmProjects\\pythonProject')
print(home)

# 源数据
file_path = os.path.join(home, '模拟数据.xlsx')
df1 = pd.read_excel(io=file_path, sheet_name='英超积分榜')
df2 = pd.read_excel(r'C:\Users\c1998\PycharmProjects\pythonProject\模拟数据.xlsx', sheet_name='英超球员榜')
print(df1)
print(df2)

# 01 VLOOKUP
df_merge = pd.merge(df1, df2, on='球队', how='left')  # 效果类似left join，即 如果df2里有针对On的多条记录它会导致df1返回多行数据
print(df_merge)

# 可以先用此法查看On列是否有重复值，如果没有则应该显示True=0
print(df2['球队'].duplicated().value_counts())

# 02 PV_Table
pv = pd.pivot_table(df1, index='去向', columns='城市', values='积分', aggfunc=['sum', 'mean', 'min'])  # 每个杯赛去向的城市球队内的积分总和,平均值，最小值
print(pv)

# 03 对比两列差异
print(df2.loc[df2['球队'].isin(df1['球队']), ['球员', '球队']])  # 射手榜里有，且球队排名也在积分榜靠前的球员名字和球队名字
print(df2.loc[df2['球队'].isin(df1['球队']) == False, ['球员', '球队']])  # 射手榜里有，但球队排名在积分榜不靠前的球员名字和球队名字
print(df2.loc[~df2['球队'].isin(df1['球队']), ['球员', '球队']])  # 同上

# 04 去除重复值
print(df2.drop_duplicates('球队'))  # 基于“球队”列进行去重

# 05 缺失值处理
print(df2.info())  # 返回每一列里有几个非空值
df2['球队'] = df2['球队'].fillna('阿森纳')
print(df2)  # 指定将某列的空值替换成某值
print(df2.dropna(subset='球队'))  # 删除特定某列上有缺失值的行

# 06 多条件筛选
print(df1.loc[(((df1['去向'] == '欧冠') & (df1['城市'] == '曼彻斯特')) | (df1['城市'] == '伯明翰'))])  # 能打欧冠的曼市球队 或 伯明翰的球队

# 07 模糊筛选数据
print(df1.loc[df1['球队'].str.contains('斯|曼')])  # 球队名字里带有“斯”或“曼”的
print(df1.loc[df1['球队'].str.contains('斯') & df1['球队'].str.contains('阿')])  # 球队名字里带有“斯”和“阿”的
print(df1.loc[df1['球队'].str.contains('^阿')])  # 球队名字以“阿”开头的
print(df1.loc[df1['球队'].str.contains('拉$')])  # 球队名字以“拉”结尾的
print(df1.loc[df1['球队'].str.contains('^.{1}斯')])  # 球队名字第二个字为“斯”的

# 08 分类汇总
print(df1.groupby(['城市', '去向'])['积分'].sum())  # 计算不同城市&去向 分组下的积分综合

# 09 条件计算 跳过

# 10 删除数据间的空格 跳过

# 11 数据分列 跳过--存疑

# 12 异常值替换 跳过

# 13 分组 跳过

# 14 根据业务逻辑定义标签
# method1
df1.loc[df1['积分'] > 50, 'label'] = '满足下限'
df1.loc[df1['积分'] > 60, 'label'] = '不错的'
df1.loc[df1['积分'] > 70, 'label'] = '牛逼阿'
print(df1)

# method2
def assign_label(score):
    if score > 70:
        return '牛逼阿'
    elif score > 60:
        return '不错的'
    elif score > 50:
        return '满足下限'
    else:
        return '不满足'

df1['label'] = df1['积分'].apply(assign_label)
print(df1)

# method3
def get_label(score):
    if score > 70:
        return '牛逼阿'
    elif score > 60:
        return '不错的'
    elif score > 50:
        return '满足下限'
    else:
        return '不满足'

# 将函数应用于DataFrame
df1['label'] = df1['积分'].map(get_label)
print(df1)

# apply方法可以应用于整个DataFrame或其单个列（或行），而map方法只能应用于Series（即DataFrame的单列）
