from lib.ecdict.stardict import convert_dict


def init_db():
    convert_dict('dict.db', 'ecdict.csv')


init_db()
