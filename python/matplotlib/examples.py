# coding=gbk
# matplotlib 官网
import matplotlib.pyplot as plt
import numpy as np

## bar chart
# 开一个 多行多列 的窗口, 一次性拿到多个 Axes
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(10, 4))  # 一次性创建"图窗(Figure)"和"坐标轴(Axes)"两个对象, ax 是真正在上面画画的那块画布(坐标系)

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

#### hat graph
values =[
    [11, 12, 11, 11, 11],
    [8, 14, 13, 3, 6],
]
x = np.arange(len(values[0]))  # 0, 1, 2, 3, 4
ax4.set_xticks(x, labels=['I', 'II', 'III', 'IV', 'V'])  # 设置x轴刻度
spacing = 0.3  # 左右两端留空比例 30%
width = (1 - spacing) /  len(values)  # 单根柱子宽度
heights0 = values[0]  # 第一行(以 Player A 的高度)作为基准高度

for i, (heights, group_label) in enumerate(zip(values, ['Player A', 'Player B'])):
    style = {'fill': False, 'edgecolor': 'blue'} if i == 0 else {'edgecolor': 'black', 'color': 'red'}  # 第一组仅描边不填充，第二组黑色边框+填充
    heights = np.asarray(heights)  # 确保后续向量运算
    rects = ax4.bar(
        x=x-spacing/2+i*width,
        height=(heights-heights0),  # 仅画 delta 部分
        width=width,
        bottom=heights0,  # 从基准线开始往上
        label=group_label,
        **style  # "字典拆包"语法, 把字典拆成关键字参数
    )
    for height, rect in zip(heights, rects):
        ax4.annotate(
            text=f'{height}',  # 文字内容
            xy=(rect.get_x()+rect.get_width()/2, height),  # 文字位置在柱子顶部的中心
            xytext=(0, 4),  # 再向上平移4个像素
            textcoords='offset points',  # 偏移量用像素, 不随缩放改变
            ha='center',
            va='bottom',
        )
ax4.set_xlabel('Games')
ax4.set_ylabel('Score')
ax4.set_ylim(0, 20)  # 固定 y 轴范围，避免帽子被裁
ax4.set_title('Scores by number of game and players')
ax4.legend()

#### horizontal bar chart
np.random.seed(19680891)  # 固定随机种子, 保证每次运行得到一样的随机数 只要种子相同 算法走的路线就一模一样 方便复现
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))  # 0 1 2 3 4
performance = 3 + 10 * np.random.rand(len(people))  # 3–13 之间的随机值
error = np.random.rand(len(people))  # 0–1 之间的随机误差
r = ax5.barh(y=y_pos, width=performance, xerr=error, align='center')  # 每条横条加上水平误差线 横条中心与y刻度对齐
ax5.bar_label(container=r, label_type='edge', labels=[f'{float(w):.2f}' for w in performance])  # 强制转 float 再写
ax5.set_yticks(y_pos, labels=people)  # 把刻度换成名字
ax5.invert_yaxis()  # y 轴反向, 最上面是 Tom, 最下面是 Jim
ax5.set_xlabel('Performance')  # x 轴标题
ax5.set_title('How fast do you want to go today?')  # 图标题

#### discrete distribution as horizontal bar chart
category_names = ['Strongly disagree', 'Disagree', 'Neither agree nor disagree', 'Agree', 'Strongly agree']
result = {
    'Question 1': [10, 15, 17, 32, 26],
    'Question 2': [26, 22, 29, 10, 13],
    'Question 3': [35, 37, 7, 2, 19],
    'Question 4': [32, 11, 9, 15, 33],
    'Question 5': [21, 29, 5, 5, 40],
    'Question 6': [8, 19, 5, 30, 38]
}
labels = list(result.keys())
data = np.array(list(result.values()))  # 6行问题, 5列选项
data_cum = data.cumsum(axis=1)
category_colors = plt.colormaps['RdYlGn'](np.linspace(0.15, 0.85, data.shape[1]))  # 在 0.15 到 0.85 之间均匀地取 5 个数, 如果直接 linspace(0, 1, 5)会拿到红 橙 黄 浅绿 绿
ax6.invert_yaxis()  # 将y轴反向, 最上面是Q1, 最下面是Q6
ax6.xaxis.set_visible(False)  # 隐藏x轴刻度线, 只保留条形长度, 不需要顶部坐标轴
ax6.set_xlim(left=0, right=np.sum(data, axis=1).max())  # 让x轴的最大刻度=人数最多那一行的总人数
for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[:, i]  # 每次画一层水平条形, 本层宽度=当前选项人数
    starts = data_cum[:, i] - widths  # 本层起点=累计-自身宽度, 累计里面已经包含了自身宽度
    rects = ax6.barh(y=labels, width=widths, left=starts, label=colname, color=color, height=0.5)
    r, g, b, _ = color
    text_color = 'white' if r * g * b < 0.5 else 'darkgrey'  # 根据背景亮度决定文字用白还是深灰, 保证可读性
    ax6.bar_label(container=rects, label_type='center', color=text_color)  # 把人数写在条形中间
ax6.legend(ncols=len(category_names), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')  # 先定锚点左上角, 再定图例的左下角去贴(0, 1), 图例整体紧贴着子图 顶部外侧 左侧对齐, 不会压到条形图

plt.show()
