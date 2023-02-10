from typing import List
from mydb.sqlite import SerializedSqlite
# from mydb.bigquery import DataUploader, Char

class Path:
    def __init__(self, line: List[float], curve: List[float]) -> None:
        self.line = line
        self.curve = curve


def test_sqlite():
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


# def test_bq():
#     font_name = 'dev_sqlitedb2'
#     chars = [
#         Char('a', [Path(1.1, 1.2), Path(2.1, 2.2)]),
#         Char('z', [Path(3.1, 3.2), Path(4.1, 4.2)])
#         ]
#     register = DataUploader(font_name, chars)
#     result = register.insert()
#     print(result)
#
#  -> TypeError: Object of type bytes is not JSON serializable

if __name__ == '__main__':
    test_sqlite()
