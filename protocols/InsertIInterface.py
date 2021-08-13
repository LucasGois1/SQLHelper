from abc import ABCMeta, abstractmethod


class InsertIInterface:
    __metaclass__: ABCMeta

    @abstractmethod
    def test(self): pass