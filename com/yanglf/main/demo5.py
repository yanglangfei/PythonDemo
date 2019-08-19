import os

from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator  # 词库
import matplotlib.pyplot as plt  # 绘制图像的模块
import jieba  # jieba分词
import numpy as np

path = os.path
print(path)
stopwords = {'这些': 0, '那些': 0, '因为': 0, '所以': 0}  # 噪声词
path_txt = '../file/all.txt'
path_img = '../img/heart01.jpg'
f = open(path_txt, 'r', encoding='UTF-8').read()
background_image = np.array(Image.open(path_img))

# 结巴分词分割文本，并拼接成字符串
cut_text = ' '.join(jieba.cut(f))
word_cloud = WordCloud(
    # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
    font_path=r'C:\Windows\Fonts\STXINWEI.TTF',
    background_color='black',
    max_words=100,  # 最大显示单词数
    max_font_size=60,  # 频率最大单词字体大小
    stopwords=stopwords,  # 过滤噪声词
    # width=1000,
    # height=880,
    # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
    mask=background_image
).generate(cut_text)

image = word_cloud.to_image()
image.show()

# 生成颜色值   绘制在面板上
# image_colors = ImageColorGenerator(background_image)
# 下面代码表示显示图片
# plt.imshow(word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
# plt.axis('off')
# plt.show()
