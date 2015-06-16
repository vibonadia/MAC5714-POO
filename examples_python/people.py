"Abstract classes can be implemented using ABCMeta package"
import abc

class People(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abc.abstractmethod
    def print_name(self):
        pass
