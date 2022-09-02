import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar,
    QFileDialog
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("snippy")

        label = QLabel("Hey! Load container or create new own.")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        # < MENU BAR SETUP >

        menu_bar = self.menuBar() # Creating menu bar

        # File submenu
        file_menu = menu_bar.addMenu("&File")

        load_container = QAction("Load container...", self)
        load_container.setStatusTip("Open file dialog and choose json file")
        load_container.triggered.connect(self.load_container_on_click)
        file_menu.addAction(load_container)



    def load_container_on_click(self, s):
        file_dialog = QFileDialog.getOpenFileName(
            self,
            "Open JSON file",
            "/home/",
            "JSON Files (*.json)"
        )
        file_dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()