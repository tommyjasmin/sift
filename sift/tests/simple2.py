#!/usr/bin/env python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# http://pyqt.sourceforge.net/Docs/PyQt4/modules.html
#from PyQt4.QtWidgets import *


class MainWindow(QMainWindow):

    significant = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.windowTitleChanged.connect(self.onWindowTitleChange)
        self.setWindowTitle("simple2")
        layout = QVBoxLayout()
        widget = QWidget()
        things = [QDateEdit, QLabel, QDial, QDoubleSpinBox, QSpinBox, QProgressBar, QSlider, QRadioButton, QTimeEdit, QFontComboBox, QLineEdit]
        widget.setLayout(layout)
        for w in things: 
            if w is QLabel:
                wid = QLabel('hola')
                font = wid.font()
                font.setPointSize(32)
                wid.setFont(font)
                wid.setAlignment(Qt.AlignHCenter)
            elif w is QLineEdit:
                q = QLineEdit()
                q.setPlaceholderText("I am text hear me roar")
                q.returnPressed.connect(self.return_pressed)
                q.selectionChanged.connect(self.selection_changed)
                q.textChanged.connect(self.text_changed)
                q.textEdited.connect(self.text_edited)
                self.line = q
                wid = q
            else:
                wid = w()
            layout.addWidget(wid)

        self.setCentralWidget(widget)
        self.significant.connect(self.on_my_signal)

    def contextMenuEvent(self, e):
        print("context menu")
        super(MainWindow, self).contextMenuEvent(e)  # can also use e.accept() or e.ignore()

    def return_pressed(self):
        print('return pressed')
        self.line.setText("BOOM")

    def selection_changed(self):
        print('selection changed')

    def text_edited(self):
        print("text edited to " + repr(self.line.text()))

    def text_changed(self):
        print("text changed to " + repr(self.line.text()))

    def on_golden_pond(self, a):
        print(a)

    def on_button_pressed(self):
        print("bort")
        self.significant.emit('-bort-')

    def on_my_signal(self, s):
        print('there has been {0:s}'.format(s))


    # def onWindowTitleChange(self, s):
    #     print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
