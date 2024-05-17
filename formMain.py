import sys
import time
import pyrealsense2 as rs
import numpy as np
import cv2
import time
import math
import os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from UI.MainForm import Ui_MainForm


from PySide6.QtCore import QTimer,QPoint,QDateTime
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader



from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtCore import QThread, Qt, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
pyqtSignal = Signal
pyqtSlot = Slot

#from SocketCommunication import HandControl
from SocketCommunication import socketCom


class MainForm(qtw.QWidget, Ui_MainForm):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.pb_connect.clicked.connect(self.clickMe)
        self.pb_connect.clicked.connect(self.Connect_2_Hand)
        self.pb_reset.clicked.connect(self.reset)


    def Connect_2_Hand(self):
        host = self.le_ip.text()
        port = int(self.le_port.text())
        if host == "192.168.30.200" and port == 1024:
            print("correct IP and Port entered")
        else:
            print("Invalid ip or port entered")
        hand = socketCom.THK_Hand_Controller()
        status=hand.connect(host, port)

        if status[0] == 1:
            print("connected successfully")
        else:
            print("Unsuccessful connection")

        hand.close()
        return(host, port)

    def reset(self):
        host,port = self.Connect_2_Hand()
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.MoveOrigin()
            hand.close()
        else:
            print("Check hand connection")

        return



if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)

    window = MainForm()
    window.show()


    sys.exit(app.exec())

