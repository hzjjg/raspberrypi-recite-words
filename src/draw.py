# 根据单词内容显示图像
# PIL api reference:
# https://pillow.readthedocs.io/en/stable/reference/index.html

from PIL import Image, ImageDraw, ImageFont

img = Image.new('1', (250, 122), 255)
size = {
    'w': 250,
    'h': 122
}

draw = ImageDraw.Draw(img)

# 绘制外框
draw.line(
    (
        (1, 1),
        (size['w']-1, 1),
        (size['w']-1, size['h']-1),
        (1, size['h']-1),
        (1, 1)
    ), fill=0)

word_font = ImageFont.truetype('arial.ttf', 28)
draw.text((8, 12), 'avenger', font=word_font, fill=0,)

draw.line((8, 50, 100, 50), fill=0)

explain_font = ImageFont.truetype('arial.ttf', 20)
draw.text((8, 55), 'n.复仇者[/əˈven.dʒɚ/]', font=explain_font, fill=0,)

img.show()
