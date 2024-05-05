import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 150, 800, 600)
        self.setWindowTitle("Тайна деревни")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()


if __name__ == '__main__':
    qt_launcher = QApplication(sys.argv)
    example = Window()
    example.show()
    sys.exit(qt_launcher.exec_())
