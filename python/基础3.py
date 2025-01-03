# coding=gbk
"""
python高级遍历技巧
公众号：测试开发学习交流
2024-07-30
"""

# 列表推导式
numbers = [1, 2, 3, 5, 10]
squares = [n**2 for n in numbers]
print(squares)

# 使用字典推导式创建映射
keys = ['a', 'b', 'c']
values = [1, 2, 3]
mappings = {key: value for key, value in zip(keys, values)}
print(mappings)

# 使用集合推导式去除重复元素
items = [1, 2, 2, 3, 1, 4, 6, 4]
unique_items = {item for item in items}
unique_items2 = set(items)
print(unique_items)
print(unique_items2)

# 使用zip并行遍历多个序列
names = ['alice', 'bob', 'thomas']
ages = [10, 12, 9]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old.')

# 使用enumerate获取索引和值
fruits = ['apple', 'banana', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# 使用itertools.permutations生成排列
# 使用itertools.product生成笛卡尔积
