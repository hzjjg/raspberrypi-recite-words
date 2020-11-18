from dep.ecdict.stardict import open_dict


def query(key):
    db = open_dict('dict.db')
    return db.query(key)
