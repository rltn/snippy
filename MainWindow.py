import sys

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QTreeView
from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QDockWidget
from PySide6.QtWidgets import QSplitter

from PySide6.QtGui import QAction

from PySide6.QtCore import Qt
# from PySide6.QtCore import QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("snippy")
        # self.setSize(QSize(400, 300))
        
        # Empty label adding
        # label = QLabel("Hey! Load container or create new own.")
        # label.setAlignment(Qt.AlignCenter)
        # 
        # self.setCentralWidget(label)
        
        
        self.tree_view = QTreeView()
        # self.dock_list_widget = QDockWidget(self.list_widget)
        self.text_editor = QTextEdit()
        # self.dock_text_editor = QDockWidget(self.text_editor)
        # self.setCentralWidget(self.text_editor)
        self.splitter = QSplitter()
        self.setCentralWidget(self.splitter)
        self.splitter.addWidget(self.tree_view)
        self.splitter.addWidget(self.text_editor)
        # self.tabifyDockWidget(self.dock_text_editor, self.dock_list_widget)
        
        
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
            "/home/",
            "JSON Files (*.json)"
        )[0]

        print(file_path)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
    
if __name__ == '__main__':
    main()