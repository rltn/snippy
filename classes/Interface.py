from classes.ArgObject import ArgObject
import kivy

class Interface(ABC):
    """docstring for Interface."""
    
    def __init__(self, **arg):
        super(Interface, self).__init__(**arg)
        
    def load(self, **arg):
        self.arg = arg
        
    def __str__(self):
        return f'Interface'
        
    def __repr__(self):
        return f'Interface'