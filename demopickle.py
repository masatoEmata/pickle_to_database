from typing import List
import sqlite3

class Path:
    def __init__(self, line: List[float], curve: List[float]) -> None:
        self.line = line
        self.curve = curve

import pickle
import bz2

def ptoz(obj):
    return bz2.compress(pickle.dumps(obj, pickle.HIGHEST_PROTOCOL), 3)

def ztop(b):
    return pickle.loads(bz2.decompress(b))

dbname = 'chars.db'
tbname = 'afs'


def main():
    objs = ["hoge", ("h","o","g","e"), {0:"h", 1:"o", 2:"g", 3:"e"}]
    obj_names = ["hoge_str", "hoge_tuple", "hoge_dict"]

    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('create table afs(id integer primary key, charname text, pathobj blob);')
    insert_sql = f"insert into {tbname} (charname, pathobj) values (?,?)"
    insert_objs = list(zip(obj_names, [ptoz(x) for x in objs]))
    c.executemany(insert_sql, insert_objs)
    conn.commit()

    select_sql = f'select * from {tbname} where charname = "hoge_tuple"'
    for row in c.execute(select_sql):
        print((row[0], row[1], ztop(row[2])))
    conn.close()

main()

# paths = [Path(1.1, 1.2), Path(2.1, 2.2)]
# z = ptoz(paths)
# v = ztop(z)
# print(v[0].line, v[1].line)
