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


from SocketCommunication import socketCom



class MainForm(qtw.QWidget, Ui_MainForm):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.image =" /Images/"

        self.running=True

        self.pb_connect.clicked.connect(self.Connect_2_Hand)
        self.pb_reset.clicked.connect(self.reset)
        self.pb_start.clicked.connect(self.capture_photo)
        self.pb_capture.clicked.connect(self.stop)


    def UpdateRGBImage(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
        self.lb_rgb.setFixedSize(360, 360)
        self.lb_rgb.setPixmap(QPixmap.fromImage(image))
        #self.lb_detection.setPixmap(QPixmap.fromImage(image))

    def UpdateDepthImage(self, frame):
        depth_cm = cv2.applyColorMap(cv2.convertScaleAbs(frame, alpha=0.5), cv2.COLORMAP_JET)
        depth_image = QImage(depth_cm, depth_cm.shape[1], depth_cm.shape[0],  QImage.Format_RGB888)
        self.lb_rgbd.setFixedSize(360, 360)
        self.lb_rgbd.setPixmap(QPixmap.fromImage(depth_image))
    def UpdateDetection(self,frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
        self.lb_detection.setFixedSize(360, 360)
        self.lb_detection.setPixmap(QPixmap.fromImage(image))
        self.lb_detection.setPixmap(QPixmap.fromImage(image))


    def capture_photo(self):
        pipe = rs.pipeline()
        config = rs.config()

        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        pipe.start(config)
        output_directory = 'Images_new'
        os.makedirs(output_directory, exist_ok=True)
        frame_count = 0
        while self.running:
            #camera initialization
            frame = pipe.wait_for_frames()
            rgb_frame = frame.get_color_frame()
            depth_frame = frame.get_depth_frame()

            rgb_image = np.asanyarray(rgb_frame.get_data())
            depth_image = np.asanyarray(depth_frame.get_data())
            #depth_image = cv2.applyColorMap(cv2.convertScaleAbs(depth_frame, alpha=0.5), cv2.COLORMAP_JET)

            self.UpdateRGBImage(rgb_image)
            self.UpdateDepthImage(depth_image)
            self.UpdateDetection(rgb_image)

            frame_count += 1
            if frame_count == 20:
                rgb_image_filename = os.path.join(output_directory, f'rgb_image_{1}.jpg')
                depth_image_filename = os.path.join(output_directory, f'depth_image_{1}.jpg')
                cv2.imwrite(rgb_image_filename, rgb_image)
                cv2.imwrite(depth_image_filename, depth_image)
            if cv2.waitKey(1) == ord("q"):
                break

    def stop(self):
        self.running = False


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

