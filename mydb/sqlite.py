import sqlite3
from typing import List
import pickle
import bz2


def serialize(obj):
    return bz2.compress(pickle.dumps(obj, pickle.HIGHEST_PROTOCOL), 3)

def deserialize(binary):
    return pickle.loads(bz2.decompress(binary))


class SerializedSqlite:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def create(self):
        try:
            self.cursor.execute(f'create table {self.table_name}(charname text primary key, pathobj blob);')
            self.conn.commit()
        except sqlite3.OperationalError:
            pass

    def insert(self, obj_names: List, obj_values: List):
        insert_sql = f"INSERT OR REPLACE into {self.table_name} (charname, pathobj) values (?,?)"
        serialized_values = [serialize(x) for x in obj_values]
        insert_objs = list(zip(obj_names, serialized_values))
        self.cursor.executemany(insert_sql, insert_objs)
        self.conn.commit()

    def select(self, target_keys):
        select_sql = f'select * from {self.table_name} where charname in ({",".join(["?"]*len(target_keys))})'
        result = self.cursor.execute(select_sql, target_keys)
        data = [(row[0], deserialize(row[1])[0]) for row in result]
        self.conn.close()
        return data

    def close(self):
        self.conn.close()
