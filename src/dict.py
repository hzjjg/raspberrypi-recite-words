from dep.ecdict.stardict import open_dict

db = open_dict('dict.db')


def query(key):
    return db.query(key)
