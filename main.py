import sys
import logging
from PIL import Image
from threading import Timer

from src.draw import draw
from src.dict import get_random_collins_words
from lib.epd import epd as Epd

words = get_random_collins_words(1, 30)

# 单词切换间隔时间 / 秒
interval = 60

word_index = 0


def start_show_words():
    global word_index
    word = words[word_index]

    if(word_index + 1 < len(words)):
        word_index += 1
    else:
        word_index = 0

    img = draw(word)
    img = img.transpose(Image.ROTATE_180)

    try:
        epd = Epd.EPD()
        epd.display(epd.getbuffer(img))
    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        Epd.epdconfig.module_exit()
        exit()

    t = Timer(interval, start_show_words)
    t.start()


try:
    epd = Epd.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
except IOError as e:
    logging.info(e)

start_show_words()
