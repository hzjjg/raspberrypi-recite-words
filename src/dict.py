import sys
import os
sys.path.append('..')

from lib.ecdict.stardict import open_dict  # NOQA: E402

dict_path = os.path.join(
    os.path.dirname(__file__),
    '../'
    'dict.db'
)


def query(key):
    db = open_dict(dict_path)
    return db.query(key)


def get_random_collins_words(min_star, count):
    db = open_dict(dict_path)
    conn = db.conn
    c = conn.cursor()
    c.execute(
        'select * from stardict where collins >= ? order by random() limit ?', (min_star, count))
    records = c.fetchall()
    result = []
    for record in records:
        result.append(db.record2obj(record))
    return result
