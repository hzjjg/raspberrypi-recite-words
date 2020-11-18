# 根据单词内容显示图像
# PIL api reference:
# https://pillow.readthedocs.io/en/stable/reference/index.html

from PIL import Image, ImageDraw, ImageFont
import os


fontdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'font')

print(fontdir)


def draw(word={}):
    print(word)
    img = Image.new('1', (250, 122), 255)
    size = {
        'w': 250,
        'h': 122
    }

    draw = ImageDraw.Draw(img)

    # 绘制外框
    if(False):
        draw.line(
            (
                (1, 1),
                (size['w']-1, 1),
                (size['w']-1, size['h']-1),
                (1, size['h']-1),
                (1, 1)
            ), fill=0)

    # 单词字体
    word_font = ImageFont.truetype(os.path.join(fontdir, 'en_font.ttf'), 28)
    # 单词释义字体
    explain_font = ImageFont.truetype(os.path.join(fontdir, 'en_font.ttf'), 16)
    # 单词翻译中文字体
    translation_font = ImageFont.truetype(
        os.path.join(fontdir, 'zh_font.ttc'), 12)

    draw.text((8, 6), word['word'], font=word_font, fill=0,)
    draw.line((8, 44, 130, 44), fill=0)

    # 科林斯词典分级
    if(word.get('collins')):
        draw.text((140, 38), '* ' * word['collins'],
                  font=translation_font, fill=0,)

    x = 8
    y = 50
    if(word.get('phonetic')):
        phonetic = f'[{word["phonetic"]}]'
        draw.text((x, y), phonetic, font=explain_font, fill=0,)
        size = translation_font.getsize(word['phonetic'])
        y += 5 + size[1]

    if(word.get('translation')):
        draw.text((x, y), word['translation'], font=translation_font, fill=0,)
    img = img.transpose(Image.ROTATE_180)
    return img
