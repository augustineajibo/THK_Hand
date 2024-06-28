import sys
import time
import pyrealsense2 as rs
import numpy as np
import time
import math
import os
import csv
import ast
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from UI.MainForm import Ui_MainForm

import shutil

from PySide6.QtCore import QTimer,QPoint,QDateTime
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader

from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtCore import QThread, Qt, Signal, Slot
from PySide6.QtGui import QImage, QPixmap

from SocketCommunication import socketCom

import cv2
from PIL import Image
from ultralytics import YOLO

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


pyqtSignal = Signal
pyqtSlot = Slot


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.plot_sensor_data()

    def plot_sensor_data(self):
        # Generate some example time series data
        now = datetime.now()
        x = [now - timedelta(minutes=i) for i in range(100)]
        y = [random.random() for _ in range(100)]

        # Create a plot
        self.ax.clear()
        self.ax.plot(x, y, 'r-')
        self.ax.set_title("Sensor Data Over Time")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Sensor Value")
        self.ax.xaxis.set_major_formatter(DateFormatter("%H:%M"))

        # Rotate date labels for better readability
        self.figure.autofmt_xdate()

        # Refresh the canvas
        self.canvas.draw()


class MainForm(qtw.QWidget, Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Finger_1_current_status = [0, 0, 0]
        self.Finger_2_current_status = [0, 0, 0]
        self.Finger_3_current_status = [0, 0, 0]
        self.Finger_4_current_status = [0, 0, 0]

        self.step = 50
        self.new_value = 0



        self.seg_image = "./runs/segment/predict/rgb_image.jpg"
        self.captured_image = './Images_new/rgb_image.jpg'
        #delete_files_and_folders(directory)

        self.item = "Pet-bottle"

        self.running = True

        self.pb_connect.clicked.connect(self.Connect_2_Hand)
        self.pb_reset.clicked.connect(self.reset_handPos)
        self.pb_all_finger.clicked.connect(self.AllFinger)
        self.pb_all_grip.clicked.connect(self.AllGrip)
        self.pb_start.clicked.connect(self.capture_photo)
        self.pb_capture.clicked.connect(self.stop)
        self.pb_save.clicked.connect(self.itemDetection)
        self.pb_detect.clicked.connect(self.detectionCheck)
        self.pb_saveJog.clicked.connect(self.save_to_csv)
        self.pb_load.clicked.connect(self.load_Move_AllFinger)
        self.pb_add.clicked.connect(self.plot_sensor_data)

        self.pb_f1_joint1_pos.clicked.connect(self.Finger_1_joint_1_Pos)
        self.pb_f1_joint1_neg.clicked.connect(self.Finger_1_joint_1_Neg)
        self.pb_f1_joint2_pos.clicked.connect(self.Finger_1_joint_2_Pos)
        self.pb_f1_joint2_neg.clicked.connect(self.Finger_1_joint_2_Neg)
        self.pb_f1_joint3_pos.clicked.connect(self.Finger_1_joint_3_Pos)
        self.pb_f1_joint3_neg.clicked.connect(self.Finger_1_joint_3_Neg)

        self.pb_f2_joint1_pos.clicked.connect(self.Finger_2_joint_1_Pos)
        self.pb_f2_joint1_neg.clicked.connect(self.Finger_2_joint_1_Neg)
        self.pb_f2_joint2_pos.clicked.connect(self.Finger_2_joint_2_Pos)
        self.pb_f2_joint2_neg.clicked.connect(self.Finger_2_joint_2_Neg)
        self.pb_f2_joint3_pos.clicked.connect(self.Finger_2_joint_3_Pos)
        self.pb_f2_joint3_neg.clicked.connect(self.Finger_2_joint_3_Neg)

        self.pb_f3_joint1_pos.clicked.connect(self.Finger_3_joint_1_Pos)
        self.pb_f3_joint1_neg.clicked.connect(self.Finger_3_joint_1_Neg)
        self.pb_f3_joint2_pos.clicked.connect(self.Finger_3_joint_2_Pos)
        self.pb_f3_joint2_neg.clicked.connect(self.Finger_3_joint_2_Neg)
        self.pb_f3_joint3_pos.clicked.connect(self.Finger_3_joint_3_Pos)
        self.pb_f3_joint3_neg.clicked.connect(self.Finger_3_joint_3_Neg)

        self.pb_f4_joint1_pos.clicked.connect(self.Finger_4_joint_1_Pos)
        self.pb_f4_joint1_neg.clicked.connect(self.Finger_4_joint_1_Neg)
        self.pb_f4_joint2_pos.clicked.connect(self.Finger_4_joint_2_Pos)
        self.pb_f4_joint2_neg.clicked.connect(self.Finger_4_joint_2_Neg)
        self.pb_f4_joint3_pos.clicked.connect(self.Finger_4_joint_3_Pos)
        self.pb_f4_joint3_neg.clicked.connect(self.Finger_4_joint_3_Neg)

    def sensor_data(self):
        sense_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sensor_value = [0x80, 0x00, 0x00, 0x00]

        host, port = self.Connect_2_Hand()
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)
        #mean, xax, j = [], [], 0
        #new_result=[]

        while True:
            result = hand.get_data(sensor_value)




    def plot_sensor_data(self):
        # Generate some example time series data
        now = datetime.now()
        result= self.sensor_data()

        print(result)



    def delete_files_and_folders(self, detection_dir):
        print(detection_dir)
        # Ensure the directory is a valid path
        if not isinstance(detection_dir, (str, bytes, os.PathLike)):
            raise TypeError(f"Expected str, bytes, os.PathLike or None, but got {type(detection_dir).__name__}")

        # Check if the directory exists
        if not os.path.exists(detection_dir):
            print(f"The directory {detection_dir} does not exist.")
            return

        # Loop through all the items in the directory
        for item in os.listdir(detection_dir):
            item_path = os.path.join(detection_dir, item)

            # If the item is a file, delete it
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                print(f"Deleted file: {item_path}")

            # If the item is a directory, delete it and its contents
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Deleted folder: {item_path}")



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
        self.lb_detection.show()



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


            self.UpdateRGBImage(rgb_image)
            self.UpdateDepthImage(depth_image)


            frame_count += 1
            if frame_count == 20:
                rgb_image_filename = os.path.join(output_directory, f'rgb_image.jpg')
                depth_image_filename = os.path.join(output_directory, f'depth_image.jpg')
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






    def reset_handPos(self):
        host,port = self.Connect_2_Hand()
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.MoveOrigin()
            hand.close()
        else:
            print("Check hand connection")

        return

    def AllGrip(self):
        host, port = self.Connect_2_Hand()
        pos = int(self.le_grip_pos.text())
        speed = int(self.le_grip_speed.text())
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            #hand.MoveOrigin()
            hand.MoveAllGrip(pos,speed)
            # hand.MoveAllFingers(-200,10)
            hand.close()
        else:
            print("Check hand connection")
        return


    def AllFinger(self):
        host, port = self.Connect_2_Hand()
        pos = int(self.le_finger_pos.text())
        speed = int(self.le_finger_speed.text())
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.MoveAllFingers(pos,speed)
            hand.close()
        else:
            print("Check hand connection")
        return

    def load_Move_AllFinger(self):
        host, port = self.Connect_2_Hand()
        pos = self.load_csv()
        speed = 5
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.MoveAllFingers(pos,speed)
            hand.close()
        else:
            print("Check hand connection")
        return


    def Finger_1_Joint_1(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [9]
        pos = self.Finger_1_current_status[0]
        print(pos)
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Rotation(pos,speed,finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_1_Joint_2(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [1]
        pos = self.Finger_1_current_status[1]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Linear(pos, speed,finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_1_Joint_3(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        pos = self.Finger_1_current_status[2]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)
        finger_id = [2]

        if status[0] == 1:
            hand.Specific_Grip(pos, speed,finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_2_Joint_1(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [10]
        pos = self.Finger_2_current_status[0]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Rotation(pos,speed,finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_2_Joint_2(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [3]
        pos = self.Finger_2_current_status[1]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Linear(pos, speed,finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_2_Joint_3(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [4]
        pos = self.Finger_2_current_status[2]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)


        if status[0] == 1:
            hand.Specific_Grip(pos, speed,finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_3_Joint_1(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [11]
        pos = self.Finger_3_current_status[0]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Rotation(pos, speed, finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_3_Joint_2(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [5]
        pos = self.Finger_3_current_status[1]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Linear(pos, speed, finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_3_Joint_3(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [6]
        pos = self.Finger_3_current_status[2]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Grip(pos, speed, finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_4_Joint_1(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [12]
        pos = self.Finger_4_current_status[0]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Rotation(pos, speed, finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_4_Joint_2(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [7]
        pos = self.Finger_4_current_status[1]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Linear(pos, speed, finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_4_Joint_3(self):
        host, port = self.Connect_2_Hand()
        speed = 10
        finger_id = [8]
        pos = self.Finger_4_current_status[2]
        hand = socketCom.THK_Hand_Controller()
        status = hand.connect(host, port)

        if status[0] == 1:
            hand.Specific_Grip(pos, speed, finger_id)
            hand.close()
        else:
            print("Check hand connection")
        return

    def Finger_1_joint_1_Pos(self):
        lower_limit = -800
        upper_limit = 800
        current_value = int(self.Finger_1_current_status[0])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
           self.Finger_1_current_status[0] = upper_limit
        elif new_value < lower_limit:
            self.Finger_1_current_status[0] = lower_limit
        else:
            self.Finger_1_current_status[0] = new_value
        self.Finger_1_Joint_1()

        return self.Finger_1_current_status[0]

    def Finger_1_joint_2_Pos(self):
        lower_limit = -700
        upper_limit = 150
        current_value = int(self.Finger_1_current_status[1])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_1_current_status[1] = upper_limit
        elif new_value < lower_limit:
            self.Finger_1_current_status[1] = lower_limit
        else:
            self.Finger_1_current_status[1] = new_value
        self.Finger_1_Joint_2()

        return self.Finger_1_current_status[1]

    def Finger_1_joint_3_Pos(self):
        lower_limit = -500
        upper_limit = 100
        current_value = int(self.Finger_1_current_status[2])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_1_current_status[2] = upper_limit
        elif new_value < lower_limit:
            self.Finger_1_current_status[2] = lower_limit
        else:
            self.Finger_1_current_status[2] = new_value
        self.Finger_1_Joint_3()

        return self.Finger_1_current_status[2]

    def Finger_1_joint_1_Neg(self):
        lower_limit = -800
        upper_limit = 800
        current_value = int(self.Finger_1_current_status[0])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
           self.Finger_1_current_status[0] = upper_limit
        elif new_value < lower_limit:
            self.Finger_1_current_status[0] = lower_limit
        else:
            self.Finger_1_current_status[0] = new_value
        self.Finger_1_Joint_1()
        return self.Finger_1_current_status[0]

    def Finger_1_joint_2_Neg(self):
        lower_limit = -700
        upper_limit = 150
        current_value = int(self.Finger_1_current_status[1])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_1_current_status[1] = upper_limit
        elif new_value < lower_limit:
            self.Finger_1_current_status[1] = lower_limit
        else:
            self.Finger_1_current_status[1] = new_value
        self.Finger_1_Joint_2()

        return self.Finger_1_current_status[1]

    def Finger_1_joint_3_Neg(self):
        lower_limit = -500
        upper_limit = 100
        current_value = int(self.Finger_1_current_status[2])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_1_current_status[2] = upper_limit
        elif new_value < lower_limit:
            self.Finger_1_current_status[2] = lower_limit
        else:
            self.Finger_1_current_status[2] = new_value
        self.Finger_1_Joint_3()

        return self.Finger_1_current_status[2]


    def Finger_2_joint_1_Pos(self):
        lower_limit = -800
        upper_limit = 800
        current_value = int(self.Finger_2_current_status[0])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
           self.Finger_2_current_status[0] = upper_limit
        elif new_value < lower_limit:
            self.Finger_2_current_status[0] = lower_limit
        else:
            self.Finger_2_current_status[0] = new_value
        self.Finger_2_Joint_1()

        return self.Finger_2_current_status[0]

    def Finger_2_joint_2_Pos(self):
        lower_limit = -700
        upper_limit = 150
        current_value = int(self.Finger_2_current_status[1])

        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_2_current_status[1] = upper_limit
        elif new_value < lower_limit:
            self.Finger_2_current_status[1] = lower_limit
        else:
            self.Finger_2_current_status[1] = new_value
        self.Finger_2_Joint_2()

        return print(self.Finger_2_current_status[1])

    def Finger_2_joint_3_Pos(self):
        lower_limit = -500
        upper_limit = 100
        current_value = int(self.Finger_2_current_status[2])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_2_current_status[2] = upper_limit
        elif new_value < lower_limit:
            self.Finger_2_current_status[2] = lower_limit
        else:
            self.Finger_2_current_status[2] = new_value
        self.Finger_2_Joint_3()

        return self.Finger_2_current_status[2]

    def Finger_2_joint_1_Neg(self):
        lower_limit = -800
        upper_limit = 800
        current_value = int(self.Finger_2_current_status[0])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_2_current_status[0] = upper_limit
        elif new_value < lower_limit:
            self.Finger_2_current_status[0] = lower_limit
        else:
            self.Finger_2_current_status[0] = new_value
        self.Finger_2_Joint_1()

        return self.Finger_2_current_status[0]

    def Finger_2_joint_2_Neg(self):
        lower_limit = -700
        upper_limit = 150
        current_value = int(self.Finger_2_current_status[1])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_2_current_status[1] = upper_limit
        elif new_value < lower_limit:
            self.Finger_2_current_status[1] = lower_limit
        else:
            self.Finger_2_current_status[1] = new_value
        self.Finger_2_Joint_2()

        return self.Finger_2_current_status[1]

    def Finger_2_joint_3_Neg(self):
        lower_limit = -500
        upper_limit = 100
        current_value = int(self.Finger_2_current_status[2])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_2_current_status[2] = upper_limit
        elif new_value < lower_limit:
            self.Finger_2_current_status[2] = lower_limit
        else:
            self.Finger_2_current_status[2] = new_value
        self.Finger_2_Joint_3()

        return self.Finger_2_current_status[2]

    def Finger_3_joint_1_Pos(self):
        lower_limit = -800
        upper_limit = 800
        current_value = int(self.Finger_3_current_status[0])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_3_current_status[0] = upper_limit
        elif new_value < lower_limit:
            self.Finger_3_current_status[0] = lower_limit
        else:
            self.Finger_3_current_status[0] = new_value
        self.Finger_3_Joint_1()

        return self.Finger_3_current_status[0]

    def Finger_3_joint_2_Pos(self):
        lower_limit = -700
        upper_limit = 150
        current_value = int(self.Finger_3_current_status[1])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_3_current_status[1] = upper_limit
        elif new_value < lower_limit:
            self.Finger_3_current_status[1] = lower_limit
        else:
            self.Finger_3_current_status[1] = new_value
        self.Finger_3_Joint_2()

        return self.Finger_3_current_status[1]

    def Finger_3_joint_3_Pos(self):
        lower_limit = -500
        upper_limit = 100
        current_value = int(self.Finger_3_current_status[2])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_3_current_status[2] = upper_limit
        elif new_value < lower_limit:
            self.Finger_3_current_status[2] = lower_limit
        else:
            self.Finger_3_current_status[2] = new_value
        self.Finger_3_Joint_3()

        return self.Finger_3_current_status[2]

    def Finger_3_joint_1_Neg(self):
        lower_limit = -800
        upper_limit = 800
        current_value = int(self.Finger_3_current_status[0])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_3_current_status[0] = upper_limit
        elif new_value < lower_limit:
            self.Finger_3_current_status[0] = lower_limit
        else:
            self.Finger_3_current_status[0] = new_value
        self.Finger_3_Joint_1()

        return self.Finger_3_current_status[0]

    def Finger_3_joint_2_Neg(self):
        lower_limit = -700
        upper_limit = 150
        current_value = int(self.Finger_3_current_status[1])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_3_current_status[1] = upper_limit
        elif new_value < lower_limit:
            self.Finger_3_current_status[1] = lower_limit
        else:
            self.Finger_3_current_status[1] = new_value
        self.Finger_3_Joint_2()

        return self.Finger_3_current_status[1]

    def Finger_3_joint_3_Neg(self):
        lower_limit = -500
        upper_limit = 100
        current_value = int(self.Finger_3_current_status[2])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_3_current_status[2] = upper_limit
        elif new_value < lower_limit:
            self.Finger_3_current_status[2] = lower_limit
        else:
            self.Finger_3_current_status[2] = new_value
        self.Finger_3_Joint_3()

        return self.Finger_3_current_status[2]

    def Finger_4_joint_1_Pos(self):
        lower_limit = -800
        upper_limit = 800
        current_value = int(self.Finger_4_current_status[0])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_4_current_status[0] = upper_limit
        elif new_value < lower_limit:
            self.Finger_4_current_status[0] = lower_limit
        else:
            self.Finger_4_current_status[0] = new_value
        self.Finger_4_Joint_1()

        return self.Finger_4_current_status[0]

    def Finger_4_joint_2_Pos(self):
        lower_limit = -700
        upper_limit = 150
        current_value = int(self.Finger_4_current_status[1])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_4_current_status[1] = upper_limit
        elif new_value < lower_limit:
            self.Finger_4_current_status[1] = lower_limit
        else:
            self.Finger_4_current_status[1] = new_value
        self.Finger_4_Joint_2()

        return self.Finger_4_current_status[1]

    def Finger_4_joint_3_Pos(self):
        lower_limit = -500
        upper_limit = 100
        current_value = int(self.Finger_4_current_status[2])
        print(current_value)
        new_value = current_value + int(self.step)
        if new_value > upper_limit:
            self.Finger_4_current_status[2] = upper_limit
        elif new_value < lower_limit:
            self.Finger_4_current_status[2] = lower_limit
        else:
            self.Finger_4_current_status[2] = new_value
        self.Finger_4_Joint_3()

        return self.Finger_4_current_status[2]

    def Finger_4_joint_1_Neg(self):
        lower_limit = -800
        upper_limit = 800
        current_value = int(self.Finger_4_current_status[0])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_4_current_status[0] = upper_limit
        elif new_value < lower_limit:
            self.Finger_4_current_status[0] = lower_limit
        else:
            self.Finger_4_current_status[0] = new_value
        self.Finger_4_Joint_1()

        return self.Finger_4_current_status[0]

    def Finger_4_joint_2_Neg(self):
        lower_limit = -700
        upper_limit = 150
        current_value = int(self.Finger_4_current_status[1])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_4_current_status[1] = upper_limit
        elif new_value < lower_limit:
            self.Finger_4_current_status[1] = lower_limit
        else:
            self.Finger_4_current_status[1] = new_value
        self.Finger_4_Joint_2()

        return self.Finger_4_current_status[1]

    def Finger_4_joint_3_Neg(self):
        lower_limit = -500
        upper_limit = 100
        current_value = int(self.Finger_4_current_status[2])
        print(current_value)
        new_value = current_value - int(self.step)
        if new_value > upper_limit:
            self.Finger_4_current_status[2] = upper_limit
        elif new_value < lower_limit:
            self.Finger_4_current_status[2] = lower_limit
        else:
            self.Finger_4_current_status[2] = new_value
        self.Finger_4_Joint_3()

        return self.Finger_4_current_status[2]

    def save_to_csv(self):
        # Open a file dialog to select the save location

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                   options=options)
        if file_name:
            merged_list = self.Finger_1_current_status + self.Finger_2_current_status + self.Finger_3_current_status + self.Finger_4_current_status
            merged_list = np.array(merged_list)
            print(merged_list)

            # Save data to the CSV file
            try:
                np.savetxt(file_name, [merged_list], delimiter=',', fmt='%d')
                print(f"Data successfully saved to {file_name}")

            except Exception as e:
                print(f"Error saving data to CSV: {e}")

    def load_csv(self):
        # Open a file dialog to select a CSV file
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        if file_dialog.exec():
            # Get the selected file path
            file_path = file_dialog.selectedFiles()[0]

            # Read and display the CSV contents
            try:
                # Load the CSV file into a numpy array
                data = np.loadtxt(file_path, delimiter=',', dtype=int)
                # Convert the numpy array to a list
                data_list = data.tolist()


                # Convert the nested list (since we used [merged_list] in savetxt) to a flat list
                if len(data_list) == 1:
                    data_list = data_list[0]

            except (ValueError, SyntaxError):

                pass
        return data_list



    """
    def load_csv(self):
        # Open a file dialog to select a CSV file
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        if file_dialog.exec():
            # Get the selected file path
            file_path = file_dialog.selectedFiles()[0]

            # Read and display the CSV contents
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                content = ""

                for row in reader:
                    # Convert the specific column (assuming the first column here) from string to list of floats
                    # Adjust the column index as needed
                    try:
                        # Evaluate the string to get a list
                        list_as_str = ast.literal_eval(row[0])
                        # Convert each element of the list to float
                        if isinstance(list_as_str, list):
                            list_as_floats = [float(x) for x in list_as_str]
                            row[0] = list_as_floats
                    except (ValueError, SyntaxError):
                        pass
                    content += str(row) + "\n"
                print(content)

        return content

    """





    def itemDetection(self,item):
        print("started.............")
        items = ["Pet-bottle","Cardboard","Wine-glass","Sponge"]
         # Flag to indicate if item was found
        item_found = False

        detected_item = " "

        # Loop through each element in the list
        for element in items:
            if element == item:
                item_found = True
                detected_item = item
                break

        # Check the flag and print the appropriate message
        if item_found:
            print(f"'{detected_item}' was found in the list.")

        else:
            print(f"'{detected_item}' was not found in the list.")
        return detected_item
    def modelPrediction(self,detection_dir):
        self.delete_files_and_folders(detection_dir)
        model = YOLO("./Model/best.pt")
        results = model('./images_new/rgb_image.jpg', save=True,conf=0.85, verbose=False)
        probs = results[0].boxes.conf.numpy()
        prob = np.round(probs[0], 2)

        object_name = ""
        for result in results:
            if result.boxes:
                box = result.boxes[0]
                class_id = int(box.cls)
                object_name = model.names[class_id]
        return results, object_name, prob

    def detectionCheck(self):
        item = "Pet-bottle"
        detection_dir = './runs/'
        results, object_name, prob = self.modelPrediction(detection_dir)
        #print(prob)

        #detected_item = self.itemDetection(item)
        self.lb_itemdetected.setText(object_name)
        self.lb_accuracy.setText(str(prob))
        seg_image = "./runs/segment/predict/rgb_image.jpg"
        frame = cv2.imread(seg_image)

        # Check if the image was loaded successfully
        if frame is None:
            raise ValueError(f"Failed to load image from {seg_image}")

        # Convert the color from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.UpdateDetection(frame)

        return


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec())

