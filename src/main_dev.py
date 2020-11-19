# 由于开发环境没有比如gpio这种硬件，便于开发时调试程序

from dict import query
from draw import draw
import random
from threading import Timer

simple_words = [
    'good',
    'police',
    'nice',
    'set',
    'right'
]

random.shuffle(simple_words)
word_index = 0
interval = 10


def start_show_words():
    global word_index
    word = query(simple_words[word_index])

    if(word_index + 1 < len(simple_words)):
        word_index += 1
    else:
        word_index = 0

    img = draw(word)
    img.show()
    t = Timer(interval, start_show_words)
    t.start()


start_show_words()
