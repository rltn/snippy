import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

from classes.ArgObject import ArgObject


class Interface(ArgObject):
    """Interface is the graphics interface class for the project"""

    def __init__(self, **arg):
        super(Interface, self).__init__(**arg)
    
    def load(self, **arg):
        self.arg['name'] = arg.get('name', '')
        self.arg['language'] = arg.get('language', '')
        self.arg['storage'] = arg.get('storage', list())
        self.arg['dump_storage'] = arg.get('dump_storage', list())
        self.arg['decription'] = arg.get('decription', '')
        self.arg['tags'] = arg.get('tags', [])
    
    def __str__(self):
        return f'Interface <>'
        
    def __repr__(self):
        return f'Interface <>'
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    label.show()
    app.exec()