# Battery Widget
# Author: Theara Kong
# Email: theara729@gmail.com
# GitHub: 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class BatteryWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wg_container = QtWidgets.QWidget(self)
        self.wg_container.setGeometry(QtCore.QRect(12, 5, 179, 59))
        self.wg_container.setStyleSheet("#wg_container\n"
        "{\n"
        "    background:rgba(0, 0, 0, 0);\n"
        "}")
        self.wg_container.setObjectName("wg_container")
        self.body_head = QtWidgets.QLabel(self.wg_container)
        self.body_head.setGeometry(QtCore.QRect(145, 10, 10, 25))
        self.body_head.setStyleSheet("#body_head\n"
        "{\n"
        "    background:rgba(0, 0, 0, 0);\n"
        "    background:#ffffff;\n"
        "    border-radius: 2px;\n"
        "}")
        self.body_head.setText("")
        self.body_head.setObjectName("body_head")
        self.body = QtWidgets.QLabel(self.wg_container)
        self.body.setGeometry(QtCore.QRect(0, 0, 146, 45))
        self.body.setStyleSheet("#body\n"
        "{\n"
        "    border:3px ridge #ffffff;\n"
        "    border-radius: 5px;\n"
        "}")
        self.body.setText("")
        self.body.setObjectName("body")
        self.lvl_1 = QtWidgets.QLabel(self.wg_container)
        self.lvl_1.setGeometry(QtCore.QRect(5, 5, 25, 35))
        self.lvl_1.setStyleSheet("#lvl_1\n"
        "{\n"
        "    background:#7CFC00;\n"
        "}")
        self.lvl_1.setText("")
        self.lvl_1.setObjectName("lvl_1")
        self.lvl_2 = QtWidgets.QLabel(self.wg_container)
        self.lvl_2.setGeometry(QtCore.QRect(32, 5, 25, 35))
        self.lvl_2.setStyleSheet("#lvl_2\n"
        "{\n"
        "    background:#7CFC00;\n"
        "}")
        self.lvl_2.setText("")
        self.lvl_2.setObjectName("lvl_2")
        self.lvl_3 = QtWidgets.QLabel(self.wg_container)
        self.lvl_3.setGeometry(QtCore.QRect(60, 5, 25, 35))
        self.lvl_3.setStyleSheet("#lvl_3\n"
        "{\n"
        "    background:#7CFC00;\n"
        "}")
        self.lvl_3.setText("")
        self.lvl_3.setObjectName("lvl_3")
        self.lvl_4 = QtWidgets.QLabel(self.wg_container)
        self.lvl_4.setGeometry(QtCore.QRect(88, 5, 25, 35))
        self.lvl_4.setStyleSheet("#lvl_4\n"
        "{\n"
        "    background:#7CFC00;\n"
        "}")
        self.lvl_4.setText("")
        self.lvl_4.setObjectName("lvl_4")
        self.lvl_5 = QtWidgets.QLabel(self.wg_container)
        self.lvl_5.setGeometry(QtCore.QRect(116, 5, 25, 35))
        self.lvl_5.setStyleSheet("#lvl_5\n"
        "{\n"
        "    background:#7CFC00;\n"
        "}")
        self.lvl_5.setText("")
        self.lvl_5.setObjectName("lvl_5")

        self.setValue(50)

    # This method is used to set battery value
    # The value must be between 0-100
    # Input of invalid value will be round to min 0 and max 100
    @QtCore.pyqtSlot(int)
    def setValue(self, value):
        self.value = value
        if self.value > 100 :
            self.value = 100
        elif self.value < 0:
            self.value = 0
        
        # Interal of 20%
        if self.value < 5 :
            # Battery supper low
            # frame white
            self.body_head.setStyleSheet("#body_head\n"
            "{\n"
            "    background:#ff0000;\n"
            "    border-radius: 2px;\n"
            "}")
            self.body.setStyleSheet("#body\n"
            "{\n"
            "    border:3px ridge #ff0000;\n"
            "    border-radius: 5px;\n"
            "}")
            # Level 1 : None
            self.lvl_1.setStyleSheet("#lvl_1\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 2 : None
            self.lvl_2.setStyleSheet("#lvl_2\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 3 : None
            self.lvl_3.setStyleSheet("#lvl_3\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 4 : None
            self.lvl_4.setStyleSheet("#lvl_4\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 5 : None
            self.lvl_5.setStyleSheet("#lvl_5\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            
        elif self.value >= 5 and self.value < 20:
            # Batery level 1
            # frame white
            self.body_head.setStyleSheet("#body_head\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    background:#ffffff;\n"
            "    border-radius: 2px;\n"
            "}")
            self.body.setStyleSheet("#body\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    border:3px ridge #ffffff;\n"
            "    border-radius: 5px;\n"
            "}")
            # Level 1 : Green
            self.lvl_1.setStyleSheet("#lvl_1\n"
            "{\n"
            "    background:#ff0000;\n"
            "}")
            # Level 2 : None
            self.lvl_2.setStyleSheet("#lvl_2\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 3 : None
            self.lvl_3.setStyleSheet("#lvl_3\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 4 : None
            self.lvl_4.setStyleSheet("#lvl_4\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 5 : None
            self.lvl_5.setStyleSheet("#lvl_5\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
        
        elif self.value >= 20 and self.value < 40:
            # Battery level 2
            # frame white
            self.body_head.setStyleSheet("#body_head\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    background:#ffffff;\n"
            "    border-radius: 2px;\n"
            "}")
            self.body.setStyleSheet("#body\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    border:3px ridge #ffffff;\n"
            "    border-radius: 5px;\n"
            "}")
            # Level 1 : Green
            self.lvl_1.setStyleSheet("#lvl_1\n"
            "{\n"
            "    background:#F28500;\n"
            "}")
            # Level 2 : Green
            self.lvl_2.setStyleSheet("#lvl_2\n"
            "{\n"
            "    background:#F28500;\n"
            "}")
            # Level 3 : None
            self.lvl_3.setStyleSheet("#lvl_3\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 4 : None
            self.lvl_4.setStyleSheet("#lvl_4\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 5 : None
            self.lvl_5.setStyleSheet("#lvl_5\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")

        elif self.value >= 40 and self.value < 60:
            # Battery level 3
            # frame white
            self.body_head.setStyleSheet("#body_head\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    background:#ffffff;\n"
            "    border-radius: 2px;\n"
            "}")
            self.body.setStyleSheet("#body\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    border:3px ridge #ffffff;\n"
            "    border-radius: 5px;\n"
            "}")
            # Level 1 : Green
            self.lvl_1.setStyleSheet("#lvl_1\n"
            "{\n"
            "    background:#ffd700;\n"
            "}")
            # Level 2 : Green
            self.lvl_2.setStyleSheet("#lvl_2\n"
            "{\n"
            "    background:#ffd700;\n"
            "}")
            # Level 3 : Green
            self.lvl_3.setStyleSheet("#lvl_3\n"
            "{\n"
            "    background:#ffd700;\n"
            "}")
            # Level 4 : None
            self.lvl_4.setStyleSheet("#lvl_4\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")
            # Level 5 : None
            self.lvl_5.setStyleSheet("#lvl_5\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")

        elif self.value >= 60 and self.value < 80:
            # Battery level 4
            # frame white
            self.body_head.setStyleSheet("#body_head\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    background:#ffffff;\n"
            "    border-radius: 2px;\n"
            "}")
            self.body.setStyleSheet("#body\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    border:3px ridge #ffffff;\n"
            "    border-radius: 5px;\n"
            "}")
            # Level 1 : Green
            self.lvl_1.setStyleSheet("#lvl_1\n"
            "{\n"
            "    background:#32cd32;\n"
            "}")
            # Level 2 : Green
            self.lvl_2.setStyleSheet("#lvl_2\n"
            "{\n"
            "    background:#32cd32;\n"
            "}")
            # Level 3 : Green
            self.lvl_3.setStyleSheet("#lvl_3\n"
            "{\n"
            "    background:#32cd32;\n"
            "}")
            # Level 4 : Green
            self.lvl_4.setStyleSheet("#lvl_4\n"
            "{\n"
            "    background:#32cd32;\n"
            "}")
            # Level 5 : None
            self.lvl_5.setStyleSheet("#lvl_5\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "}")

        elif self.value >= 80:
            # Battery level 5
            # frame white
            self.body_head.setStyleSheet("#body_head\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    background:#ffffff;\n"
            "    border-radius: 2px;\n"
            "}")
            self.body.setStyleSheet("#body\n"
            "{\n"
            "    background:rgba(0, 0, 0, 0);\n"
            "    border:3px ridge #ffffff;\n"
            "    border-radius: 5px;\n"
            "}")
            # Level 1 : Green
            self.lvl_1.setStyleSheet("#lvl_1\n"
            "{\n"
            "    background:#7CFC00;\n"
            "}")
            # Level 2 : Green
            self.lvl_2.setStyleSheet("#lvl_2\n"
            "{\n"
            "    background:#7CFC00;\n"
            "}")
            # Level 3 : Green
            self.lvl_3.setStyleSheet("#lvl_3\n"
            "{\n"
            "    background:#7CFC00;\n"
            "}")
            # Level 4 : Green
            self.lvl_4.setStyleSheet("#lvl_4\n"
            "{\n"
            "    background:#7CFC00;\n"
            "}")
            # Level 5 : Green
            self.lvl_5.setStyleSheet("#lvl_5\n"
            "{\n"
            "    background:#7CFC00;\n"
            "}")
        self.wg_container.update()
    

