import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QFileDialog,
    QTreeView,
    QTextEdit,
    QDockWidget,
    QSplitter
)

from PySide6.QtGui import QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Window setup
        
        self.setWindowTitle("snippy")
        
        # Empty label adding
        # label = QLabel("Hey! Load container or create new own.")
        # label.setAlignment(Qt.AlignCenter)
        # 
        # self.setCentralWidget(label)
        
        self.tree_view = QTreeView()
        
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
        file_path = QFileDialog.getOpenFileName(
            self,
            "Open JSON file",
            str(Path.home()),
            "JSON Files (*.json)"
        )[0]

        print(file_path)