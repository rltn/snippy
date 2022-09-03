from abc import ABC, abstractmethod


class ArgObject(ABC):
    """docstring for ArgObject."""

    def __init__(self, **arg):
        super(ArgObject, self).__init__()
        self.arg = dict()
        self.load(**arg)

    @abstractmethod
    def load(self, **arg):
        self.arg = arg
    
    def dumpd(self):
        return self.arg

    def set(self, key, val):
        self.arg[key] = val

    def get(self, key, std = None):
        return self.arg.get(key, std)

    @abstractmethod
    def __str__(self):
        return f'ArgObject'

    @abstractmethod
    def __repr__(self):
        return f'ArgObject'