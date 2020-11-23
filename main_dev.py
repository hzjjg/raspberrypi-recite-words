# 由于开发环境预览程序

from src.dict import query
from src.draw import draw
import random
from threading import Timer

# 要背的单词、词组
simple_words = [
    'absorb',
    'crawl',
    'shrug',
    'maximum',
    'layman',
]


# 单词切换间隔时间 / 秒
interval = 10

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
    img.show()
    t = Timer(interval, start_show_words)
    t.start()


def test_show_word():
    word = query('good')
    img = draw(word)
    img.show()


# 测试单个单词显示
# test_show_word()

# 测试单词循环
start_show_words()
