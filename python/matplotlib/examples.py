# coding=gbk
# matplotlib 官网
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker


# 开一个 多行多列 的窗口, 一次性拿到多个 Axes
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(15, 5))  # 一次性创建"图窗(Figure)"和"坐标轴(Axes)"两个对象, ax 是真正在上面画画的那块画布(坐标系)
# 1. bar chart
# 1.1 with individual bar colors
x = np.logspace(0, 3, 300)          # 0.1 ~ 1000
y = 1 / (1 + x**2)                  # 1/f? 衰减
ax1.loglog(x, y, label='1/f?')
ax1.set_xlabel('Frequency [Hz]')
ax1.set_ylabel('PSD')
ax1.set_title('Log-Log Plot')
ax1.legend()

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
for attribute, measurement in penguin_means.items():
    offset = width * multiplier  # 当前指标的整体左右平移距离
    p = ax3.bar(x=x+offset, height=measurement, width=width, label=attribute)  # 画当前组的柱子
    ax3.bar_label(container=p, padding=-20, label_type='edge')  #  先把文字锚定在柱顶外侧, 然后再把这个锚点整体往下移xx个像素
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

# 1.5 horizontal bar chart
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
ax6.legend(ncols=len(category_names), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')  # 先定锚点左上角, 再定图例的左下角去贴(0, 1), 图例整体紧贴着子图 顶部外侧 左侧对齐, 不会压到条形图

plt.show()


fig2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(15, 25))
# 2. line chart
# 2.1 basic line plot
t = np.arange(start=0.0, stop=2.0, step=0.01)  # 0~2, 步长0.01 一共201个点
s = 1 + np.sin(2 * np.pi * t)  # 把时间数组t放大2π倍 得到弧度坐标, 对整个数组逐元素求正弦，返回同样长度的数组，值域 [-1, 1], 把整条正弦曲线整体向上平移 1 个单位
ax1.plot(t, s)  # 折线图, x=时间, y=电压
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
