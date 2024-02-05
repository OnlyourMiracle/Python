import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def trans_ch(txt):
  words = jieba.lcut(txt)
  newtxt = ''.join(words)
  return newtxt


f = open('/content/2023.txt','r',encoding = 'utf-8')     #将你的文本文件名与此句的'maozedong.txt'替换
txt = f.read()
f.close
txt = trans_ch(txt)
def filter_chars(s, chars_to_remove):
    for char in chars_to_remove:
        s = s.replace(char, '')  # 替换为''即删除
    return s

original_string = txt
chars_to_remove = "心情指数晴雨"  # 想要删除的字符
filtered_string = filter_chars(original_string, chars_to_remove)
print(filtered_string)  # 输出过滤后的字符串
txt = filtered_string
mask = np.array(Image.open("/content/未命名.jpeg").convert("RGBA"))               #将你的背景图片名与此句的"love.png"替换
wordcloud = WordCloud(background_color="white",\
                      width = 800,\
                      height = 600,\
                      max_words = 100,\
                      max_font_size = 35,\
                      mask = mask,\
                      contour_width = 1,\
                      contour_color = 'steelblue',\
                        font_path =  "/content/HYYingXiongFangSong-45F-2.ttf"
                      ).generate(txt)
wordcloud.to_file('love_词云图.png')

