from typing import Set, Dict, Any, List
from psycopg2._psycopg import cursor
from psycopg2.extras import RealDictCursor

from protocols.SQLHelperIInterface import SQLHelperIInterface

import psycopg2


class SQLHelper(SQLHelperIInterface):
    base_query: str = ''

    def __init__(self, table: str, schema: str = None):
        self.schema = schema
        self.table = table

        connection = psycopg2.connect("dbname=testunit user=postgres password=Arutiunian1 host=localhost port=5432")
        connection.autocommit = True
        self.database: cursor = connection.cursor(cursor_factory=RealDictCursor)

    def return_all(self):
        self.database.execute(self.base_query)
        self.base_query = ''
        response = self.database.fetchall()
        list = []
        for row in response:
            object = {}
            for item, value in row.items():
                object[item] = value
            list.append(object)

        return list

    def execute(self):
        self.database.execute(self.base_query)
        self.base_query = ''

    def select(self, *args):
        core = 'SELECT'

        if args:
            for column in args:
                core += f' {column},'
            core = core[:-1]
        else:
            core += f' *'
        self.base_query += core + f" FROM {self.schema + '.' if self.schema else ''}{self.table} "

        return self

    def where(self, args: Dict[str, Any]):
        core = "WHERE"

        for column, value in args.items():
            core += f" {column} = "
            if type(value) == int or type(value) == float:
                core += f"{value} "
            else:
                core += f"'{value}' "
            core += f"AND"

        self.base_query += core[:-4]
        return self

    def count(self, *args):
        core = 'SELECT COUNT'
        if args:
            core += '('
            for column in args:
                core += f'{column},'
            core = core[:-1] + ')'
        else:
            core += f'(*)'
        self.base_query = core + f" FROM {self.schema + '.' if self.schema else ''}{self.table} "
        return self

    def query(self) -> str:
        return self.base_query

    def insert_one(self, args: Dict[str, Any]):
        core = f"INSERT INTO {self.schema + '.' if self.schema else ''}{self.table}("

        for column in args.keys():
            core += f'{column},'
        core = core[:-1] + ') VALUES('

        for value in args.values():

            if type(value) == int:
                core += f"{value},"
            elif value is None:
                core += 'NULL,'
            else:
                core += f"'{value}',"

        core = core[:-1] + ')'

        self.base_query += core
        return self

    def insert_many(self, args: List[Dict[str, Any]]):
        core = f"INSERT INTO {self.schema + '.' if self.schema else ''}{self.table}("

        for item in args:
            for column in item.keys():
                if column not in core:
                    core += f'{column},'
        core = core[:-1] + ') VALUES'

        for item in args:
            core += '('
            for value in item.values():
                if type(value) == int:
                    core += f"{value},"
                elif value is None:
                    core += 'NULL,'
                else:
                    core += f"'{value}',"

            core = core[:-1] + '),'

        self.base_query += core[:-1]
        return self
