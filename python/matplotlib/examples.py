# coding=gbk
# matplotlib 官网
import matplotlib.pyplot as plt
import numpy as np

## bar chart
# 开一个 多行多列 的窗口, 一次性拿到多个 Axes
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 4))  # 一次性创建"图窗(Figure)"和"坐标轴(Axes)"两个对象, ax 是真正在上面画画的那块画布(坐标系)

### with individual bar colors
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', 'red_', 'orange']  # 数量要和bar的数量匹配, 前缀带有下划线的和为空字符串的标签不会显示在图例中
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
# 以后所有"画什么"都通过 ax 下的方法完成, 而不是 plt.xxx, 这样写法更面向对象, 也更容易把多张图放一起
ax1.bar(fruits, counts, label=bar_labels, color=bar_colors)  # 画柱形图, 第一参数决定 x 轴位置(这里直接用字符串, matplotlib 会自动把它们当类别型刻度)
ax1.set_ylabel('fruit supply')
ax1.set_title('Fruit supply by kind and color')
ax1.legend(title='Fruit color')  # legend 是“图例”, 把每条柱子对应的 label 收集起来画个小表

### stacked bar chart
species = ('Aelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': [73, 34, 61],
    'Female': [50, 24, 58],
}
width = 0.6  # 单根柱子的总宽度, 也可以改成数组给每个柱子不同宽
bottom = np.zeros(3)  # 初始 [0, 0, 0], 之后循环中不断 += 新的段高度, 实现逐层堆叠
for sex, sex_count in sex_counts.items():
    # 依次取出 Male 与 Female
    p = ax2.bar(x=species, height=sex_count, width=width, label=sex, bottom=bottom)
    bottom += sex_count  # 更新底部，供下一段堆叠使用
    ax2.bar_label(p, label_type='center')  # 把数值写在段内正中
ax2.legend()  # 只要你给绘图函数传了 label 参数, ax.legend() 就能自动汇总
plt.tight_layout()  # 自动排版

#### grouped bar chart
species = ('Aelie', 'Chinstrap', 'Gentoo')
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
x = np.arange(len(species))  # 0, 1, 2 用来当基本刻度
width = 0.15  # 单根柱子的宽度
multiplier = 0  # 偏移序号
for attribute, measurement in penguin_means.items():
    offset = width * multiplier  # 当前指标的整体左右平移距离
    p = ax3.bar(x=x+offset, height=measurement, width=width, label=attribute)  # 画当前组的柱子
    ax3.bar_label(container=p, padding=-20, label_type='edge')  #  先把文字锚定在柱顶外侧, 然后再把这个锚点整体往下移xx个像素
    multiplier += 1  # 0, 1, 2 对应三项指标
ax3.set_ylabel('Length (mm)')
ax3.set_title('Penguin attributes by species')
ax3.set_xticks(x+width, species)  # 手工把刻度线挪到三组柱子的中间位置
ax3.legend(loc='upper left', ncols=3)  # 把图例横向分成 3 列显示, 也就是一行展示


plt.show()
