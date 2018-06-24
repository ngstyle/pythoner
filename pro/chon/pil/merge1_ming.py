from PIL import Image

# 加载底图 116*98
for i in range(0, 34):
    base_img = Image.open('/Users/chon/Desktop/UI/11/majiang/CardBack_1_1.png')
    # 加载需要P上去的图片 46*74
    tmp_img = Image.open('/Users/chon/Desktop/UI/11/majiang/CardFace_{}.png'.format(i))
    tmp_img = tmp_img.rotate(90, expand=1)  # 对图片进行旋转
    print(tmp_img.size)

    if i == 27:
        l = (120 - tmp_img.size[0]) / 2
        t = (60 - tmp_img.size[1]) / 2
        r = 60 + tmp_img.size[0] / 2
        b = t + tmp_img.size[1]
    else:
        l = (120 - tmp_img.size[0]) / 2
        t = (60 - tmp_img.size[1]) / 2
        r = 60 + tmp_img.size[0] / 2
        b = t + tmp_img.size[1]



    # 使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
    # 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
    # 提前将图片进行缩放，以适应box区域大小
    # tmp_img = tmp_img.rotate(-90) #对图片进行旋转
    # region = region.resize((box[2] - box[0], box[3] - box[1]))
    base_img.paste(tmp_img, (int(l), int(t), int(r), int(b)), mask=tmp_img)

    if i <= 8:
        base_img.save('./mingmah_{}.png'.format(i+21))  # 保存图片
    elif i <= 17:
        base_img.save('./mingmah_{}.png'.format(i+22))  # 保存图片
    elif i <= 26:
        base_img.save('./mingmah_{}.png'.format(i-7))   # 保存图片
    elif i <= 33:
        base_img.save('./mingmah_{}.png'.format(i + 14))  # 保存图片

    if i == 0:
        base_img.show()