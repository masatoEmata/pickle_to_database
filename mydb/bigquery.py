from google.cloud import bigquery
from google.api_core.exceptions import NotFound
# import re
from .datetime_helper import Datetime
from typing import List
from .serializer import binarize, debinarize, serialize



class Char:
    def __init__(self, name: str, paths: List) -> None:
        self.name = name
        self.paths = paths
        self.created_at = Datetime().datetime_str


class DataUploader:
    PROJECT = 'handwritten-dm-automation'
    DATASET = 'fonts'
    KEY_PATH = './service_account_key.json'
    SLEEP = 5

    def __init__(self, table_name: str, chars: List[Char]) -> None:
        self._bigquery_path = f'{self.PROJECT}.{self.DATASET}.{table_name}'
        self._chars = chars
        self._client = bigquery.Client.from_service_account_json(self.KEY_PATH)
        self.__create_table_if_not_exist()

    def insert(self) -> bigquery:
        inserted_dicts = self.__make_inserted_dicts()
        return self._client.insert_rows_json(self._bigquery_path, inserted_dicts)

    def __make_inserted_dicts(self) -> dict:
        return [binarize({'name': c.name, 'path': c.paths, 'created_at': c.created_at}) for c in self._chars]

    def __create_table_if_not_exist(self):
        try:
            return self._client.get_table(self._bigquery_path)
        except Exception as e:
            schema = [
                bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("path", "BYTES", mode="REQUIRED"),
                bigquery.SchemaField("created_at", "DATETIME", mode="REQUIRED"),
            ]
            table = bigquery.Table(self._bigquery_path, schema=schema)
            return self._client.create_table(table)


# if __name__ == '__main__':
#     font_name = 'dev_sqlitedb'
#     chars = [Char('a', )]
#     register = DataUploader(font_name, svg_dicts)
#     result = register.insert()
#     print(result)
