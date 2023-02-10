from typing import List
from mydb.sqlite import SerializedSqlite

class Path:
    def __init__(self, line: List[float], curve: List[float]) -> None:
        self.line = line
        self.curve = curve

dbname = 'chars.db'
tbname = 'afs'
obj_names = ["hoge_dict", "a"]
obj_values = [{0:"h", 1:"o", 2:"g", 3:"e"}, [Path(1.1, 1.2), Path(2.1, 2.2)]]

table = SerializedSqlite(dbname, tbname)
table.create()
table.insert(obj_names, obj_values)
data = table.select(['a', 'hoge_dict'])
table.close()
print('data: ', data)
