from PIL import Image


guoqi = Image.open('flag.png')
touxiang = Image.open('pho.jpeg')


x,y = guoqi.size

#quyu = guoqi.crop((262,100, y+62,y-100))


w,h = touxiang.size

quyu = guoqi.resize((w,h))

for i in range(w):
    for j in range(h):
        color = quyu.getpixel((i, j))
        alpha = 255-i//3
        if alpha < 0:
            alpha=0
        color = color[:-1] + (alpha, )
        quyu.putpixel((i, j), color)


touxiang.paste(quyu,(0,0),quyu)
touxiang.save('五星红旗半透明渐变头像.png')
