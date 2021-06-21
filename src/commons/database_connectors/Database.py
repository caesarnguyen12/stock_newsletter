from abc import ABC, abstractmethod


class Database(ABC):

    @staticmethod
    @abstractmethod
    def read(database, query=None):
        pass

    @staticmethod
    @abstractmethod
    def write(database, model):
        pass
