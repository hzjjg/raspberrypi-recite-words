# 由于开发环境预览程序

from src.dict import query, get_random_collins_words
from src.draw import draw
from threading import Timer

words = get_random_collins_words(1, 30)


# 单词切换间隔时间 / 秒
interval = 5

word_index = 0


def start_show_words():
    global word_index
    word = words[word_index]

    if(word_index + 1 < len(words)):
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
