import os

from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator  # 词库
import matplotlib.pyplot as plt  # 绘制图像的模块
import jieba  # jieba分词
import numpy as np

path = os.path
print(path)
path_txt = '../file/all.txt'
path_img = '../img/ball.jpg'
f = open(path_txt, 'r', encoding='UTF-8').read()
background_image = np.array(Image.open(path_img))

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
cut_text = ' '.join(jieba.cut(f))
word_cloud = WordCloud(
    # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
    font_path=r'C:\Windows\Fonts\STXINWEI.TTF',
    background_color='white',
    # width=1000,
    # height=880,
    # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
    mask=background_image
).generate(cut_text)

# 生成颜色值
image_colors = ImageColorGenerator(background_image)
# 下面代码表示显示图片
plt.imshow(word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
plt.show()
