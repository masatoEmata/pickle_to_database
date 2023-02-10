from typing import List
from mydb.sqlite import SerializedSqlite


class SampleObj:
    def __init__(self, line: List[float], curve: List[float]) -> None:
        self.line = line
        self.curve = curve


def demo():
    dbname = 'chars.db'
    tbname = 'afs'
    obj_names = ["hoge_dict", "path"]
    obj_values = [{0:"h", 1:"o", 2:"g", 3:"e"}, [SampleObj(1.1, 1.2), SampleObj(2.1, 2.2)]]

    table = SerializedSqlite(dbname, tbname)
    table.create()
    table.insert(obj_names, obj_values)
    data = table.select(['path', 'hoge_dict'])
    table.close()
    print('data: ', data)


if __name__ == '__main__':
    demo()
