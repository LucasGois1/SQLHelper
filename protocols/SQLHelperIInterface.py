from abc import ABCMeta, abstractmethod
from typing import List, Dict, Any


class SQLHelperIInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def select(self, columns: List = None): raise NotImplementedError()

    @abstractmethod
    def count(self, *args): raise NotImplementedError()

    @abstractmethod
    def query(self) -> str: raise NotImplementedError()

    @abstractmethod
    def insert(self, arg: Dict[str, Any]): raise NotImplementedError()
