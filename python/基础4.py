# coding=gbk
"""
一次搞懂 Python 字典！Python字典的20种神奇用法
公众号：软件测试圈
2024-06-28
"""

# 创建字典
my_dic = {'Name': 'Ben Chen', 'Age': 26, 'Nationality': 'China', 'Gender': 'M'}
my_dic2 = dict(name='Kobe', age=19, nationality='USA', gender='M')

# 访问字典元素
name = my_dic2['name']

# 添加字典的值
my_dic2['height'] = 198

# 更新字典的值
my_dic2['name'] = 'James'

# 删除元素
del my_dic2['name']
removed = my_dic2.pop('age')
print(removed)

# 检查字典中是否存在某个键
if 'gender' in my_dic2:
    print('gender is in the dic')

# 字典中的键值对长度
length = len(my_dic2)

# 遍历字典
for key in my_dic2:
    print(key)
for value in my_dic2.values():
    print(value)
for key, value in my_dic2.items():
    print(key, value)

# 合并字典
dic1 = {'a': 1, 'c': 10}
dic2 = {'a': 3, 'b': 20}
dic1.update(dic2)
print(dic1)  # 若存在key交集，则被最新的覆盖

# 字典推导式
sqrs = {x: x ** 2 for x in range(6)}
# print(sqrs)

# 获取所有的键，值，键值对
print(my_dic.keys())
print(my_dic.values())
print(my_dic.items())

# 获取值，如果不存在 则返回默认值
print(my_dic.get('gender', 'No gender'))
print(my_dic.get('age', 'No age'))

# 获取字典中的值，如果键不存在则设置默认值
my_dic.setdefault('Team', 'Lakers')
my_dic.setdefault('Nationality', 'Japan')
my_dic.setdefault('Name', 'Yuki')
print(my_dic)

# 清空字典中的所有元素
my_dic.clear()
print(my_dic)
