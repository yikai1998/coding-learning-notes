# coding=gbk
# matplotlib 官网
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches


# 开一个 多行多列 的窗口, 一次性拿到多个 Axes
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(15, 5))  # 一次性创建"图窗(Figure)"和"坐标轴(Axes)"两个对象, ax 是真正在上面画画的那块画布(坐标系)
"""
Question: 假如我想不要ax6, 我希望ax5单独占一行
fig = plt.figure(figsize=(15, 10))
gs  = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1.2])   # 第3行稍高
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[2, :])   # 整行合并
...  # 下面正常画
plt.tight_layout()
plt.show()
"""
# 1. bar chart
# 1.1 with individual bar colors
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']  # 数量要和bar的数量匹配, 前缀带有下划线的和为空字符串的标签不会显示在legend图例中
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']  # 每个bar的颜色
# 以后所有"画什么"都通过 ax 下的方法完成, 而不是 plt.xxx, 这样写法更面向对象, 也更容易把多张图放一起
p = ax1.bar(x=fruits, height=counts, label=bar_labels, color=bar_colors)  # 画柱形图, 第一参数决定 x 轴位置(这里直接用字符串, matplotlib 会自动把它们当类别型刻度)
ax1.bar_label(p, label_type='edge', padding=-1)
ax1.set_ylabel('fruit supply')
ax1.set_xlabel('fruit category')
ax1.set_title('Fruit supply by kind and color')
ax1.legend(title='Fruit color')  # legend 是“图例”, 把每条柱子对应的 label 收集起来画个小表

# 1.2 stacked bar chart
species = ('Aelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': [73, 34, 61],
    'Female': [50, 24, 58],
}
width = 0.6  # 单根柱子的总宽度, 也可以改成数组给每个柱子不同宽
bottom = np.zeros(3)  # 初始 [0, 0, 0], 之后循环中不断 += 新的段高度, 实现逐层堆叠
for sex, sex_count in sex_counts.items():
    # 依次取出 Male 与 Female
    p = ax2.bar(x=species, height=sex_count, width=width, label=sex, bottom=bottom)  # 这里的label不是文字, 而是bar的固有属性标签, 后面的legend有用
    bottom += sex_count  # 更新底部，供下一段堆叠使用
    ax2.bar_label(p, label_type='center')  # 把数值写在段内正中
ax2.legend()  # 只要你给绘图函数传了 label 参数, ax.legend() 就能自动汇总

# 1.3 grouped bar chart
species = ('Aelie', 'Chinstrap', 'Gentoo')
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
x = np.arange(len(species))  # 0, 1, 2 用来当基本刻度
width = 0.15  # 单根柱子的宽度
multiplier = 0  # 偏移序号
color_list = ['red', 'yellow', 'green']
for attribute, measurement in penguin_means.items():
    offset = width * multiplier  # 当前指标的整体左右平移距离
    p = ax3.bar(x=x+offset, height=measurement, width=width, label=attribute, color=color_list[multiplier])  # 画当前组的柱子
    ax3.bar_label(container=p, padding=-15, label_type='edge')  #  先把文字锚定在柱顶外侧, 然后再把这个锚点整体往下移xx个像素
    multiplier += 1  # 0, 1, 2 对应三项指标
ax3.set_ylabel('Length (mm)')
ax3.set_title('Penguin attributes by species')
ax3.set_xticks(x+width, species)  # 手工把刻度线挪到三组柱子的中间位置
ax3.legend(loc='upper left', ncols=3)  # 把图例横向分成 3 列显示, 也就是一行展示

# 1.4 hat graph
values =[
    [11, 12, 11, 11, 11],
    [8, 14, 13, 3, 6],
]
x = np.arange(len(values[0]))  # 0, 1, 2, 3, 4
ax4.set_xticks(x, labels=['I', 'II', 'III', 'IV', 'V'])  # 设置x轴刻度的值和文字标记
spacing = 0.3  # 左右两端留空比例 30%
width = (1 - spacing) /  len(values)  # 间接推算每根柱子的宽度
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

# 1.5 horizontal bar chart
np.random.seed(19680891)  # 固定随机种子, 随便写 整数就行 长度不限 只当哈希入口 想让图变就换个数保证每次运行得到一样的随机数 只要种子相同 算法走的路线就一模一样 方便复现
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

# 1.6 discrete distribution as horizontal bar chart
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
ax6.legend(ncols=len(category_names)/2, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')  # 先定锚点左上角, 再定图例的左下角去贴(0, 1), 图例整体紧贴着子图 顶部外侧 左侧对齐, 不会压到条形图
fig.tight_layout()  # 自动排版
plt.show()


fig2, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(15, 25))
# 2. line chart
# 2.1 basic line plot
t = np.arange(start=0.0, stop=2.0, step=0.01)  # 0~2, 步长0.01 一共201个点
s = 1 + np.sin(2 * np.pi * t)  # 把时间数组t放大2π倍 得到弧度坐标, 对整个数组逐元素求正弦，返回同样长度的数组，值域 [-1, 1], 把整条正弦曲线整体向上平移 1 个单位
ax1.plot(t, s)  # 折线图, x=时间, y=电压
s2 = 1 + np.cos(2 * np.pi * t)  # 自定义cos
ax1.plot(t, s2)
ax1.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
ax1.grid()  # 打开网格

# 2.2 stackplots
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
population_by_continent = {
    'Africa': [.228, .284, .365, .477, .631, .814, 1.044, 1.275],
    'the Americas': [.340, .425, .519, .619, .727, .840, .943, 1.006],
    'Asia': [1.394, 1.686, 2.120, 2.625, 3.202, 3.714, 4.169, 4.560],
    'Europe': [.220, .253, .276, .295, .310, .303, .294, .293],
    'Oceania': [.012, .015, .019, .022, .026, .031, .036, .039],
}
ax2.stackplot(year, population_by_continent.values(), labels=population_by_continent.keys(), alpha=0.8)  # x 和后面所有 y 数组都是位置参数, 不是关键字参数, 顺序即堆叠顺序, 整体透明度 80%
ax2.legend(loc='upper left', reverse=True)  # reverse=True 让图例顺序跟堆叠顺序一致 (先画在下 图例在上)
ax2.set_title('World population')
ax2.set_xlabel('Year')
ax2.set_ylabel('Number of people (billions)')
ax2.yaxis.set_minor_locator(mticker.MultipleLocator(.2))  # 每 0.2 十亿人放一根小刻度线 读数更细

# 3. heatmap
vegetables = ['cucumber', 'tomato', 'lettuce', 'asparagus', 'potato', 'wheat', 'barley']
farmers = ['Farmer Joe', 'Upland Bros.', 'Smith Gardening', 'Agrifun', 'Organiculture', 'BioGoods Ltd.', 'Cornylee Corp.']
harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
def heatmap(data, row_labels, col_labels, ax, cbar_kw=None, cbar_label='', **kwargs):
    if cbar_kw is None:
        cbar_kw = {}
    im = ax.imshow(data, **kwargs)  # 用 imshow 画矩阵  是专门把二维数组画成彩色栅格的函数 默认 origin='upper' 行列对应 data[i, j]
    # 它返回的 AxesImage 本质就是一张带坐标轴的照片, 而 plot 画的是线, bar 画的是矩形, 它们都不需要"颜色表→数值"的映射, 因此没有这种对象
    # im 里存了两个东西, 原始数据 data, 一个 Normalize 实例 负责把数据线性压到 0~1 再去颜色表里取颜色
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)   # 为图像添加右侧 colorbar
    cbar.ax.set_ylabel(cbar_label, rotation=-90, va='bottom')  # 给 colorbar 加纵向标题
    ax.set_xticks(range(data.shape[1]), labels=col_labels, rotation=-30, ha='right', rotation_mode='anchor')  # 设置 x/y 主刻度位置 + 文字
    ax.set_yticks(range(data.shape[0]), labels=row_labels)
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)  # 把刻度放到上方，并隐藏下方刻度
    ax.spines[:].set_visible(False)  # 去掉四周 spine边框
    # 画单元格分隔线：用 minor tick 定位，网格线 style 设成白色宽线
    ax.set_xticks(np.arange(data.shape[1]+1)+0.5, minor=True)  # minor=True 明确告诉坐标轴这是次要刻度
    ax.set_yticks(np.arange(data.shape[0]+1)-0.5, minor=True)  # 列数7, [-0.5  0.5  1.5 ... 6.5]
    ax.grid(which='minor', color='w', linestyle='-', linewidth=3)  # 用白线在这些位置画竖线 于是出现单元格边框效果
    ax.tick_params(which='minor', bottom=False, left=False)  # 只对次要刻度线生效 把 x 轴次要刻度线(竖的小黑线) + y 轴次要刻度线(横的小黑线)隐藏
    return im, cbar

def annotate_heatmap(im, data=None, valfmt='{x:.2f}', textcolors=('black', 'white'), threshold=None, **textkw):
    if not isinstance(data, (list, np.ndarray)):  # 类型不是 list 也不是 ndarray
        data = im.get_array()  # 从热力图对象里把原始 7×7 矩阵再拿出来
    if threshold is not None:
        threshold = im.norm(threshold)  # 在热力图每个格子里写上数值, 并根据背景亮度自动选黑字或白字
    else:
        threshold = im.norm(data.max())/2  # 如果没有指定阈值 就用数据最大值的一半作为 亮/暗 分界线, True → 深色 → 用白字
    kw = dict(horizontalalignment='center', verticalalignment='center')  # 默认文字对齐方式
    kw.update(textkw)  # 用户自定义的额外关键字 全放在 textkw 里一次性合并进来
    if isinstance(valfmt, str):  # 把格式字符串转成 matplotlib 格式化器
        valfmt = mticker.StrMethodFormatter(valfmt)
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j])>threshold)])  # 判断当前格子亮度 决定用黑字还是白字
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)  # 把数值按指定格式写进格子中心
            texts.append(text)
    return texts

im, cbar = heatmap(harvest, vegetables, farmers, ax=ax3, cmap='YlGn', cbar_label='harvest [t/year]')
texts = annotate_heatmap(im, valfmt='{x:.1f} t')  # 在每个格子里写数值 保留 1 位小数并加单位, 可以事后继续改
fig2.tight_layout()  # 自动调间距，防止文字溢出
plt.show()


fig3, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(15, 25))
# 3. pie chart
# 3.1 slices
labels = ('Frogs', 'Hogs', 'Dogs', 'Logs')
sizes = [15, 30, 145, 10]  # 每块的大小 列表或数组
colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown']  # 将颜色列表传递给颜色来设置每个切片的颜色
explode = (0, 0.1, 0, 0)  # 长度必须跟 sizes 一样长, 0不拽 >0往外拽多少
ax1.pie(x=sizes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode, shadow=True, startangle=90)  # autopct 老式的C/printf风格, "%1.1f"小数一位的浮点数, "%%"转义打印出真正的%, startangle 旋转整个饼图让第一块从头顶开始 而不是右边 (饼图从 0°（3 点钟）开始逆时针画)

# 3.2 donut
recipe = ['225 g flour', '90 g sugar', '1 egg', '60 g butter', '100 ml milk', '1/2 package of yeast']
data = [225, 90, 50, 60, 100, 5]
wedges, texts, autotexts = ax2.pie(x=data, wedgeprops=dict(width=0.5), startangle=-40, autopct='%1.1f%%')  # 把半径挖掉一半 → 形成甜甜圈, 返回 wedges 列表, 每个元素是一个Wedge对象 后面要拿它的角度和半径
bbox_props = dict(boxstyle='square,pad=0.3', fc='w', ec='k', lw=0.72)  # 方形框 文字到边框留0.3点边距 facecolor框里填白色 edgecolor边框黑色 linewidth线宽0.72点
kw = dict(arrowprops=dict(arrowstyle='-'), bbox=bbox_props, zorder=0, va='center')  # 无箭头头 把上面那个框套在文字外 图层最底层,防止压线 文字垂直居中
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1  # 取扇形中心角度
    y = np.sin(np.deg2rad(ang))  # 角度→弧度→圆上一点 (x,y) 单位圆坐标 你只要给出角度 ×1就是圆上一点, 半径1是pie的默认半径
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: 'right', 1:'left'}[int(np.sign(x))]
    connectionstyle = f'angle,angleA=0,angleB={ang}'  # 线段先水平再折向圆上 看起来整齐
    kw['arrowprops'].update({'connectionstyle': connectionstyle})
    ax2.annotate(text=recipe[i], xy=(x,y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)  # annotate带箭头的文字 自动画一条线从xytext→xy 线型,颜色,头型,折弯方式全在arrowprops里调
ax2.set_title('Matplotlib bakery: A donut')

# 3.3 bar of pie
overall_ratios = [0.27, 0.56, 0.17]
labels = ['Approve', 'Disapprove', 'Undecided']
explode = [0.1, 0, 0]
angle = -180 * overall_ratios[0]  # 把起始边向负方向挪一半角度 让这块正中被水平轴切开
#  3 个 Wedge 对象列表
wedges, *_ = ax3.pie(x=overall_ratios, labels=labels, autopct='%1.1f%%', explode=explode, startangle=angle)
age_ratios = [0.33, 0.54, 0.07, 0.06]
age_labels = ['Under 35', '35-49', '50-65', 'Over 65']  # 用倒序循环 从最老段开始往下画 这样图例顺序与柱子从上到下一致
bottom = 1
width = 0.2
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax4.bar(0, height=height, width=width, bottom=bottom, color='red', label=label, alpha=0.1+0.25*j)  # 透明度从 0.1 → 0.85 线性加深 远看像渐变色柱 近看能区分段
    ax4.bar_label(bc, labels=[f'{height:.0%}'], label_type='center')  # f'{表达式:格式说明符}' "把后面的值当成百分比显示 保留 0 位小数"
ax4.set_title('Age of approvers')
ax4.legend()
ax4.axis('off')  # 把坐标轴全部关掉 纯粹当彩色积木看
ax4.set_xlim(-2.5*width, 2.5*width)
theta1, theta2 = wedges[0].theta1, wedges[0].theta2  # 拿第 0 块Approve的两条角度边画线, 起止角度
center, r = wedges[0].center, wedges[0].r  # 把Approve这块扇形的圆心坐标和半径掏出来 后面公式里当极坐标原点用
bar_height = sum(age_ratios)
x = r * np.cos(np.pi/180*theta2) + center[0]  # x = r * cos(θ) + center[0], 把极坐标 (θ, r) 转成笛卡尔坐标 (x, y)
y = r * np.sin(np.pi/180*theta2) + center[1]
# ConnectionPatch 跨子图画任意线段
con = mpatches.ConnectionPatch(xyA=(-width/2, bar_height), coordsA=ax4.transData, xyB=(x, y), coordsB=ax3.transData)  # 子图数据坐标系
con.set_color([0, 0, 0])
ax4.add_artist(con)
con.set_linewidth(4)
x = r * np.cos(np.pi/180*theta1) + center[0]
y = r * np.sin(np.pi/180*theta1) + center[1]
con = mpatches.ConnectionPatch(xyA=(-width/2, 0), coordsA=ax4.transData, xyB=(x, y), coordsB=ax3.transData)
con.set_color([0, 0, 0])
ax4.add_artist(con)
con.set_linewidth(4)

# 3.4 bar chart on polar axis
np.random.seed(19680801)  #  固定随机种子 (保证每次运行图形一样)
theta = np.linspace(start=0.0, stop=2*np.pi, num=20, endpoint=False)  # θ 20个角度 均匀分布在0~2Π 返回等差数组 从start→stop 共num个点, endpoint=False表示不包含stop值 所以不重叠起点
radii = 10 * np.random.rand(20)  # 每个扇形的半径 0~1 小数 ×10 → 0~10
width = np.pi / 4 * np.random.rand(20)  # 每个扇形的圆心角度宽度 让每瓣角度在 0°~45°之间 看起来稀疏美观
colors = plt.cm.viridis(radii/10.)  # 颜色按照半径映射
ax5.remove()  # 先删掉原来的直角坐标轴
ax5 = fig3.add_subplot(3, 2, 5, projection='polar', aspect='equal')
ax5.bar(x=theta, height=radii, width=width, bottom=0, color=colors, alpha=0.5)  # bottom=0 都从圆心开始(可改成环) 透明度0.5 让重叠处好看
fig3.tight_layout()
plt.show()
