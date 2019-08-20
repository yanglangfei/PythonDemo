import matplotlib.pyplot as plt
import numpy as np

# 简单的绘图
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x))  # 如果没有第一个参数 x，图形的 x 坐标默认为数组的索引
plt.show()  # 显示图形

x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x),
         x, np.sin(2 * x))
plt.show()

# 自定义曲线的外观
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-o',
         x, np.cos(x), 'g--')
plt.show()

# 使用子图
x = np.linspace(0, 2 * np.pi, 50)
plt.subplot(2, 1, 1)  # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r')
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), 'g')
plt.show()

# 添加标题，坐标轴标记和图例
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')
plt.legend()  # 展示图例
plt.xlabel('Rads')  # 给 x 轴添加标签
plt.ylabel('Amplitude')  # 给 y 轴添加标签
plt.title('Sin and Cos Waves')  # 添加图形标题
plt.show()

# 直方图
np.random.seed(19680801)
mu1, sigma1 = 100, 15
mu2, sigma2 = 80, 15
x1 = mu1 + sigma1 * np.random.randn(10000)
x2 = mu2 + sigma2 * np.random.randn(10000)
# the histogram of the data
# 50：将数据分成50组
# facecolor：颜色；alpha：透明度
# density：是密度而不是具体数值
n1, bins1, patches1 = plt.hist(x1, 50, density=True, facecolor='g', alpha=1)
n2, bins2, patches2 = plt.hist(x2, 50, density=True, facecolor='r', alpha=0.2)
# n：概率值；bins：具体数值；patches：直方图对象。
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(110, .025, r'$\mu=100,\ \sigma=15$')
plt.text(50, .025, r'$\mu=80,\ \sigma=15$')
# 设置x，y轴的具体范围
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

# 柱状图
size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
x = np.arange(size)
# 有多少个类型，只需更改n即可
total_width, n = 0.8, 3
width = total_width / n
# 重新拟定x的坐标
x = x - (total_width - width) / 2
# 这里使用的是偏移
plt.bar(x, a, width=width, label='a')
plt.bar(x + width, b, width=width, label='b')
plt.bar(x + 2 * width, c, width=width, label='c')
plt.legend()
plt.show()

size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
x = np.arange(size)
# 这里使用的是偏移
plt.bar(x, a, width=0.5, label='a', fc='r')
plt.bar(x, b, bottom=a, width=0.5, label='b', fc='g')
plt.bar(x, c, bottom=a + b, width=0.5, label='c', fc='b')
plt.ylim(0, 2.5)
plt.legend()
plt.grid(True)
plt.show()

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
# 设置分离的距离，0表示不分离
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio 保证画出的图是正圆形
plt.axis('equal')
plt.show()

# 设置每环的宽度
size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
# 通过get_cmap随机获取颜色
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3) * 4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))
print(vals.sum(axis=1))
# [92. 77. 39.]
plt.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
        wedgeprops=dict(width=size, edgecolor='w'))
print(vals.flatten())
# [60. 32. 37. 40. 29. 10.]
plt.pie(vals.flatten(), radius=1 - size, colors=inner_colors,
        wedgeprops=dict(width=size, edgecolor='w'))
# equal 使得为正圆
plt.axis('equal')
plt.show()

np.random.seed(19680801)
N = 10
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)
# left表示从哪开始，
# radii表示从中心点向边缘绘制的长度（半径）
# width表示末端的弧长
# 自定义颜色和不透明度
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)
plt.show()

data = np.random.randint(0, 255, size=[40, 40, 40])
x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
# 将数据点分成三部分画，在颜色上有区分度
ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
