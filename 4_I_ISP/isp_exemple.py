# I - Principio da Segregacao de Interfaces (ISP)
""""
Uma classe nao deve ser forcada a implementar interfaces que ela nao utiliza

Em vez disso, as interfaces devem ser segregadas em conjuntos menores e mais especificos de metodos
"""

from abc import ABC, abstractmethod


class Document(ABC):

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass


class DocumentPDF(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass


class DocumentTXT(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass


class DocumentExcel(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass