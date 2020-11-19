import logging

from PIL import Image
from draw import draw
from dict import query
from dep.epd import epd as Epd
import random
from threading import Timer

# 要背的单词、词组
simple_words = [
    'absorb',
    'crawl',
    'shrug',
    'maximum',
    'layman',
    'obstruct',
    'summit',
    'prescribe',
    'sufficient',
    'challenge',
    'abuse',
    'ambition',
    'dub',
    'lace',
    'psychiatry',
    'shock',
    'ceremony',
    'scrutiny',
    'sovereign',
    'fascinate',
    'sprawl',
    'pant',
    'sow',
    'privilege',
    'cork',
    'vacant',
    'accumulate',
    'slap',
    'civic',
    'frugal',
    'navigable',
]

# 单词切换间隔时间 / 秒
interval = 60

word_index = 0
random.shuffle(simple_words)


def start_show_words():
    global word_index
    word = query(simple_words[word_index])

    if(word_index + 1 < len(simple_words)):
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
