from abc import ABCMeta, abstractmethod
from typing import List, Dict, Any


class SQLHelperIInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self): raise NotImplementedError()

    @abstractmethod
    def return_all(self): raise NotImplementedError()

    @abstractmethod
    def select(self, columns: List = None): raise NotImplementedError()

    @abstractmethod
    def count(self, *args): raise NotImplementedError()

    @abstractmethod
    def query(self) -> str: raise NotImplementedError()

    @abstractmethod
    def insert_one(self, arg: Dict[str, Any]): raise NotImplementedError()

    @abstractmethod
    def insert_many(self, arg: List[Dict[str, Any]]): raise NotImplementedError()
