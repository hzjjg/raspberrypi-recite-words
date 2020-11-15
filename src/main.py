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


def show_word():
    global word_index
    word = query(simple_words[word_index])

    if(word_index + 1 < len(simple_words)):
        word_index += 1
    else:
        word_index = 0

    draw(word)
    t = Timer(interval, show_word)
    t.start()


show_word()
