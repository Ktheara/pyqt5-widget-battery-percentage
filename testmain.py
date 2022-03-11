import sys
  
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
  
class EchoText(QtWidgets.QWidget):
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
  
        self.textbox = QtWidgets.QLineEdit()
        self.echo_label = QtWidgets.QLabel('hwllo')
  
        self.textbox.textChanged.connect(self.textbox_text_changed)
  
        self.layout.addWidget(self.textbox, 0, 0)
        self.layout.addWidget(self.echo_label, 1, 0)
  
    def textbox_text_changed(self):
        self.echo_label.setText(self.textbox.text())
  
class MainWindow(QtWidgets.QMainWindow):
  
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_gui()
  
    def init_gui(self):
        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)
  
        self.echotext_widget = EchoText()
        self.bat_widget = BatteryWidget()
  
        self.layout.addWidget(self.echotext_widget)
        self.layout.addWidget(self.bat_widget)

from batterywidget import BatteryWidget

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
  
    win = MainWindow()
    win.show()
  
    sys.exit(app.exec_())