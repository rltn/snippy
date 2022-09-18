import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QFileDialog,
    QLabel,
    QDockWidget,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QSplitter
)

from PySide6.QtGui import QAction, QFont

from classes.Loader import Loader
from classes.Container import Container
from classes.Snippet import Snippet

from graphics.TreeWidgetItem import TreeWidgetItem

class MainWindow(QMainWindow):

    def __init__(self, loader):
        super(MainWindow, self).__init__()

        self.loader = loader
        self.container = None
        self.current_item = None

        # Window setup
        self.setWindowTitle("snippy")

        # Container's tree viewing
        self.tree_view = QTreeWidget()
        self.tree_view.itemClicked.connect(self.tree_view_item_clicked)

        # Snippet's content viewing
        self.text_editor = QTextEdit()

        font = QFont("Monospace")
        font.setStyleHint(QFont.TypeWriter)

        self.text_editor.setCurrentFont(font)


        self.splitter = QSplitter()

        self.splitter.addWidget(self.tree_view)
        self.splitter.addWidget(self.text_editor)

        self.setCentralWidget(self.splitter)

        # < MENU BAR SETUP >

        menu_bar = self.menuBar() # Creating menu bar

        # File submenu
        file_menu = menu_bar.addMenu("&File")

        load_container = QAction("Load container...", self)
        load_container.setStatusTip("Open file dialog and choose json file")
        load_container.triggered.connect(self.load_container_triggered)
        file_menu.addAction(load_container)

    def tree_view_item_clicked(self, item, column):
        if self.current_item and type(self.current_item.obj) == Snippet:
            self.current_item.obj.set('content', self.text_editor.toPlainText())
        self.text_editor.setPlainText(item.obj.get('content'))
        self.current_item = item
        print(item, column)

    def load_container_triggered(self, s):
        savefile_path = QFileDialog.getOpenFileName(
            self,
            "Open JSON file",
            str(Path.home()),
            "JSON Files (*.json)"
        )[0]
        if savefile_path:
            self.container = self.loader.load_object(savefile_path)
            self.container_savepath = savefile_path
            self.bump_container()
            self.current_item = None

        print(savefile_path)

    def bump_container(self):
        self.tree_view.clear()

        self.container_item = TreeWidgetItem(self.tree_view, self.container)
