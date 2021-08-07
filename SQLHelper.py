from typing import Set, Dict, Any

from protocols.SQLHelperIInterface import SQLHelperIInterface


class SQLHelper(SQLHelperIInterface):
    base_query: str = ''

    def __init__(self, table: str, schema: str = None):
        self.schema = schema
        self.table = table

    def select(self, *args):
        core = 'SELECT'

        if args:
            for column in args:
                core += f' {column},'
            core = core[:-1]
        else:
            core += f' *'
        self.base_query += core

        return self

    def count(self, *args):
        core = 'COUNT'
        if args:
            core += '('
            for column in args:
                core += f'{column},'
            core = core[:-1] + ')'
        else:
            core += f'(*)'
        self.base_query = self.base_query[:-1] + core
        return self

    def query(self) -> str:
        return self.base_query

    def insert(self, arg: Dict[str, Any]):
        core = f"INSERT INTO {self.schema + '.' if self.schema else ''}{self.table}("

        for key in arg.keys():
            core += f'{key},'
        core = core[:-1] + ') VALUES('

        for value in arg.values():

            if type(value) == int:
                core += f"{value},"
            elif value is None:
                core += 'NULL,'
            else:
                core += f"'{value}',"

        core = core[:-1] + ')'

        self.base_query += core
        return self
