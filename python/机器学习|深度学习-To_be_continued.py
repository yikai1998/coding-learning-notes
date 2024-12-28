# coding=gbk
"""机器学习大体上来说，可以分为“有监督学习”“无监督学习”“强化学习”

“有监督学习”：提前给学习数据和正确答案，然后对未知数据进行预测
“无监督学习”：没有提前提供正确答案，需要从未知数据中发现规律
“强化学习”：根据行动反馈部分的正确答案，然后寻找数据中的最优解

机器学习的能力
classification：将给予的数据资料进行分类
regression：根据过去的成果预测未来的数值
clustering：将相似的数据资料分类成集合
recommendation：推导数据资料的相关信息
dimensionality reduction：缩减数据资料仅留下特征"""


from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import numpy as np



# 第二章 机器学习入门
learning_data = [[0, 0], [1, 0], [0, 1], [1, 1]]  # 学习数据
learning_label = [0, 0, 0, 1]  # 正确答案
clf = LinearSVC()  # 指定算法 algorithm
clf.fit(learning_data, learning_label)  # 开始学习样本数据和正确结果
test_label = clf.predict([[0, 0], [1, 0], [0, 1], [1, 1]])  # 使用测试数据进行结果预测
print([[0, 0], [1, 0], [0, 1], [1, 1]], '的预测结果：', test_label)
print('正确率 = ', accuracy_score([0, 0, 0, 1], test_label))

# 基于python的机器学习中，scikit-learn是必不可少的
# 无法确定使用何种算法更好时，可以使用算法速查表作为参考 scikit-learn algorithm cheat-sheet, 根据一个个问题走下来会引导你适用哪个算法，比如问你：“do you have labeled data 是否有标签，即带有结果的数据”
# 评估结果不理想时，可以尝试改变算法或输入的参数
learning_data = [[0, 0], [1, 0], [0, 1], [1, 1]]  # 学习数据
learning_label = [0, 1, 1, 1]  # 正确答案
clf = KNeighborsClassifier(n_neighbors=1)
clf.fit(learning_data, learning_label)
test_label = clf.predict([[0, 0], [1, 0], [0, 1], [1, 1]])
print([[0, 0], [1, 0], [0, 1], [1, 1]], '的预测结果：', test_label)
print('正确率 = ', accuracy_score([0, 1, 1, 1], test_label))


iris_data = pd.read_csv(r'C:\Users\Ben\Desktop\ywh.csv')
y = iris_data.loc[:, 'species']
x = iris_data.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
# 用train_test_split()方法可以将数据分为 学习用的数据 和 测试用的数据，指定80%用于学习，20%用于测试；参数shuffle=True可以将原数据xy打乱次序后再进行分离，从而是的数据更加均匀分布（但其实他的默认参数就是True，不额外赋值也没关系）
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)
# 开始学习训练；先生成用于分组的svc分类机，然后调用fit方法学习数据
clf = SVC()
clf.fit(x_train, y_train)
# 使用测试数据进行预测，然后和正确的标签数据对比
y_pred = clf.predict(x_test)
print('正确率 = ', accuracy_score(y_test, y_pred))


wine = pd.read_csv('winequality-white.csv', sep=';', encoding='utf-8')
# 专家的评价quality作为标签，剩下的11种成份作为数据
y = wine['quality']
x = wine.drop('quality', axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 通过RandomForestClassifier制作能够实际运作的分类机，然后使用fit()方法完成学习资料的训练
model = RandomForestClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))
# precision是判断为正确的数据中，实际上也正确的比率【模型预测的某品质结果中，符合专家正确答案的比率】
# recall是所有实际为正确的数据结果中，正确判断出来的比率【某品质酒的所有专家答案中，模型成功预测出来的部分所占比率】
# f1-score是精确率和召回率的调和平均数
# support是该品质酒的测试样本数量
print('正确率=', accuracy_score(y_test, y_pred))  # 每次运行，精确度都会有变化，这是因为学习数据和测试数据是随机划分的，使用不同的数据就行训练后，就会产生一定的误差
# 67%左右的正确率过于不理想
# UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. 这代表着标签中存在没有被分到数据的情况
# 综上，需要重新审视本次使用的数据 


count_data = wine.groupby('quality')['quality'].count()
print(count_data)
count_data.plot()
plt.show()
# 从统计结果来看，大部分是品质5-7的酒，其他的品质仅为少量数据，这种数据分布有差异的情况，被称为 不平衡数据
# 可以尝试将数据重新划分为三类，0为劣品葡萄酒，1为普通葡萄酒，2为极品葡萄酒；分别对应<=4, 5~7, >=8
new_list = []
for v in list(y):
    if v <= 4:
        new_list.append(0)
    elif v <= 7:
        new_list.append(1)
    else:
        new_list.append(2)

y = new_list
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 通过RandomForestClassifier制作能够实际运作的分类机，然后使用fit()方法完成学习资料的训练
model = RandomForestClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))
print('正确率=', accuracy_score(y_test, y_pred))  # 可以看到准确率大幅提升 
# 随机森林算法可以实现高精度的分类、回归、聚类等操作，它是从学习用的数据中抽样生成多棵决策树，再根据生成的决策树以“少数服从多数”的方式决定结果


# weather temperature prediction
in_file = './self_learn_adhoc_use/data.csv'
out_file = './self_learn_adhoc_use/kion10y.csv'
# data = pd.read_csv(in_file, encoding = 'Shift_JIS')
with open(in_file, 'r', encoding='Shift_JIS') as fr:
    lines = fr.readlines()
lines = ['Year,Month,Day,Temperature,Quality,AvgQRank\n'] + lines[5:]
lines = map(lambda line: line.replace('/', ','), lines)
result = ''.join(lines).strip()
print(result)
with open(out_file, 'w', encoding='utf-8') as fw:
    fw.write(result)
    print('saved')

df = pd.read_csv(out_file, encoding='utf-8')
# create a dictionary, and take the "month/day" as key to store the weather data
md = {}
for i, row in df.iterrows():
    m, d, v = (int(row['Month']), int(row['Day']), float(row['Temperature']))
    key = str(m) + '/' + str(d)
    if key not in md:
        md[key] = []
        # md[key] += [v]
    md[key].append(v)
avs = {}
for k in md:
    v = avs[k] = sum(md[k]) / len(md[k])  # calculate the average temperature of that date
    print('{0}: {1}'.format(k, round(v, 2)))

"""# another way to get the average temperature trend [monthly average temperature] 
g = df.groupby(['Month'])['Temperature'] 
gg = g.sum()/g.count() 
# gg.plot()"""



# 第三章opencv与机器学习-图像、视频入门

# 自动给脸部添加马赛克
cascade_file = '.venv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml'
cascade = cv2.CascadeClassifier(cascade_file)

def mosaic(img, rect, size):
    # 获取需要添加马赛克的部分
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]
    # 先缩小，再放大
    i_small = cv2.resize(i_rect, (size, size))
    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)
    # 将处理后的图像覆盖至原图中对应的位置
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2


# 读取图像并灰度化
img = cv2.imread('girl.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 进行人脸识别
face_list = cascade.detectMultiScale(img_gray, minSize=(25, 25))
if len(face_list) == 0:
    quit()
# 向图像中识别为脸部的区域添加马赛克
for (x, y, w, h) in face_list:
    img = mosaic(img, (x, y, x + w, y + h), 10)
# 输出图像
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# opencv的人脸识别并不完美，虽然可以检测出正脸，但是没法识别侧脸或图像十分倾斜的情况

# 视频分析
# 通过反复读取图像来获得视频，并展示到窗口中
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()  # 使用read方法读取图象
    frame = cv2.resize(frame, (500, 300))  # 调整图象的大小
    frame[:, :, 0] = 0  # [:,:,0]代表B通道，即蓝色通道
    frame[:, :, 1] = 0  # [:,:,1]代表G通道，即绿色通道
    # 所以只保留了红色通道
    cv2.imshow('OpenCVWebCamera-Red', frame)  # 在窗口中输出图象

    k = cv2.waitKey(1)  # 等待1微秒，返回的是对应按键的ASCII码
    if k in (27, 13):
        break  # 如果用户输入了esc或者enter键，则终止循环
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 关闭窗口


"""RGB颜色空间中使用红绿蓝三原色的组合来展现颜色，难以直观的感受到颜色的变化； 
而在HSV颜色空间中，通过调整饱和度Saturation与明度Value，可以更加直观的选择所需的颜色； 
色相Hue通常表示为360度的色相环，红绿蓝以顺时针旋转的方式排列在圆环中 """
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (500, 300))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)  # 转为hsv颜色空间
    # 分割hsv,将各个部分提取出来
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    img = np.zeros(h.shape, dtype=np.uint8)
    img[((h < 50) & (h > 200)) & (s > 100)] = 255
    cv2.imshow('OpenCVWebCamera', frame)
    k = cv2.waitKey(1)
    if k in (27, 13):
        break
cap.release()
cv2.destroyAllWindows()
