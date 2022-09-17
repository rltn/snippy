from PySide6 import QtCore
from PySide6.QtWidgets import QTreeWidgetItem, QSpinBox, QPushButton

from classes.Snippet import Snippet
from classes.Container import Container
from classes.Loader import Loader

class TreeWidgetItem(QTreeWidgetItem):
    def __init__(self, parent, obj):
        '''
        parent (QTreeWidget) : Item's QTreeWidget parent.
        obj    (object)         : Item's name. just an example.
        '''
        super(TreeWidgetItem, self).__init__(parent)
        self.obj = obj
        # Column 0 - Text:
        self.setText(0, self.obj.get('name'))
        # Column 1 - SpinBox:
        self.spinBox = QSpinBox()
        self.spinBox.setValue(0)
        self.treeWidget().setItemWidget(self, 1, self.spinBox)
        # Column 2 - Button:
        self.button = QPushButton()
        self.button.setText(f"button {self.obj.get('name')}")
        self.treeWidget().setItemWidget(self, 2, self.button)
        # Signals
        self.treeWidget().connect(
            self.button,
            QtCore.SIGNAL("clicked()"),
            self.buttonPressed
        )
        # Recursive items initialization
        if type(self.obj) == Container:
            for item in self.obj.get('storage'):
                TreeWidgetItem(self, item)

    @property
    def name(self):
        return self.text(0)

    @property
    def value(self):
        '''
        Return value (2nd column int)
        '''
        return self.spinBox.value()

    def buttonPressed(self):
        '''
        Triggered when Item's button pressed.
        an example of using the Item's own values.
        '''
        print(f"This Item name:{self.name} value:{self.value}")