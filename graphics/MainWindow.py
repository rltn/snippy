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
    QSplitter,
)

from PySide6.QtGui import QAction

from classes.Loader import Loader
from classes.Container import Container
from classes.Snippet import Snippet

from graphics.TreeWidgetItem import TreeWidgetItem

class MainWindow(QMainWindow):

    def __init__(self, loader):
        super(MainWindow, self).__init__()

        self.loader = loader
        self.container = None
        # Window setup

        self.setWindowTitle("snippy")

        # Empty label adding
        # label = QLabel("Hey! Load container or create new own.")
        # label.setAlignment(Qt.AlignCenter)
        #
        # self.setCentralWidget(label)

        self.tree_view = QTreeWidget()
        # item = QTreeWidgetItem()
        # treeWidget.setColumnCount(1)
        # *> = QList<QTreeWidgetItem()>
        # for i in range(0, 10):
        #     items.append(QTreeWidgetItem(QTreeWidget (None), QStringList(QString("item: %1").arg(i))))
        # treeWidget.insertTopLevelItems(0, items)

        self.text_editor = QTextEdit()

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

        print(savefile_path)
        self.bump_container()

    def bump_container(self):
        self.tree_view.clear()

        self.container_item = TreeWidgetItem(self.tree_view, self.container)
