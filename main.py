import sys

from PySide6.QtWidgets import QApplication

from classes.Snippet import Snippet
from classes.Container import Container
from classes.Loader import Loader

from graphics.MainWindow import MainWindow

import qdarktheme

def create_example(loader):
    main_container = loader.load_object()
    sub_container = Container(name='sub')
    snippet = Snippet(name='greetings', content='hi')
    main_container.append(sub_container)
    sub_container.append(snippet)
    sn = Snippet(name='snippet', content='snippet at root container')
    main_container.append(sn)
    loader.save_object(main_container)
    print(main_container)

def main():
    loader = Loader(filepath='save.json')
    app = QApplication(sys.argv)
    main_window = MainWindow(loader)
    main_window.show()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    app.exec()

if __name__ == '__main__':
    main()