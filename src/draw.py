# 根据单词内容显示图像
# PIL api reference:
# https://pillow.readthedocs.io/en/stable/reference/index.html

from PIL import Image, ImageDraw, ImageFont

word = {
    'spell': 'avenger',
    'meaning': '复仇者',
    'phonemes': '[/əˈven.dʒɚ/]',
    'form': 'n.'
}

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

# 单词字体
word_font = ImageFont.truetype('arial.ttf', 28)
# 单词释义字体
explain_font = ImageFont.truetype('arial.ttf', 16)
# 单词翻译中文字体
meaning_font = ImageFont.truetype('msyh.ttc', 14)

draw.text((8, 12), word['spell'], font=word_font, fill=0,)
draw.line((8, 50, 150, 50), fill=0)

x = 8
draw.text((x, 55), word['form'], font=explain_font, fill=0,)
x += explain_font.getsize(word['form'])[0]

draw.text((x, 55), word['meaning'], font=meaning_font, fill=0,)
x += meaning_font.getsize(word['meaning'])[0]

draw.text((x, 55), word['phonemes'], font=explain_font, fill=0,)

img.show()
