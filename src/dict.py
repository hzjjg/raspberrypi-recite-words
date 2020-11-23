import sys
import os
sys.path.append('..')

from lib.ecdict.stardict import open_dict  # NOQA: E402


def query(key):

    dict_path = os.path.join(
        os.path.dirname(__file__),
        '../'
        'dict.db'
    )

    db = open_dict(dict_path)
    return db.query(key)
