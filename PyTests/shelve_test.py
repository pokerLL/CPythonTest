import shelve as sh


def print_db(db):
    for k,v in db.items():
        print(f"{k} - {v}")

DB_NAME = "ff.db"
db = sh.open(DB_NAME) # 从路径加载数据库文件（有的话）或者新建数据库（没有的话）
print_db(db)

db['mylist'] = [1, 2, 3]
db['mydict'] = {'key1': 'value1', 'key2': 'value2'}

ml = db["mylist"]
print(ml)
print_db(db)
"""
mylist - [1, 2, 3]
mydict - {'key1': 'value1', 'key2': 'value2'}
"""

db.close()
