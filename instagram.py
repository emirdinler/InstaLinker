import sys
import webbrowser

from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("INSTAGRAM")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #008000;")
        self.label = QtWidgets.QLabel("Press for Instagram", self)
        self.label.setStyleSheet("color: #FFFFFF; font-size: 20px;")
        self.button = QtWidgets.QPushButton("emir_dnlr")# you can write your insta profile name on button
        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.label)
        v_box.addWidget(self.button)
        v_box.addStretch()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.button.clicked.connect(lambda: webbrowser.open("https://www.instagram.com/"))
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
