# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.setWindowModality(Qt.WindowModal)
        MainForm.resize(1323, 863)
        font = QFont()
        font.setPointSize(12)
        MainForm.setFont(font)
        MainForm.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.verticalLayout_2 = QVBoxLayout(MainForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fm_thk = QFrame(MainForm)
        self.fm_thk.setObjectName(u"fm_thk")
        self.fm_thk.setMaximumSize(QSize(16777215, 50))
        self.fm_thk.setStyleSheet(u"background-color: rgb(84, 84, 84);")
        self.fm_thk.setFrameShape(QFrame.StyledPanel)
        self.fm_thk.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fm_thk)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_thk = QLabel(self.fm_thk)
        self.lb_thk.setObjectName(u"lb_thk")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        self.lb_thk.setFont(font1)
        self.lb_thk.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.lb_thk.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_thk)


        self.verticalLayout_2.addWidget(self.fm_thk)

        self.frame = QFrame(MainForm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(400, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(206, 206, 206);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setStyleSheet(u"background-color: rgb(162, 162, 162);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_4.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 200))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(200, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_8)

        self.pb_connect = QPushButton(self.frame_12)
        self.pb_connect.setObjectName(u"pb_connect")
        self.pb_connect.setMaximumSize(QSize(150, 40))
        self.pb_connect.setFont(font2)
        self.pb_connect.setMouseTracking(True)
        self.pb_connect.setTabletTracking(True)
        self.pb_connect.setStyleSheet(u"border: 2px solid ;\n"
"selection-color: rgb(0, 85, 0);\n"
"border-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 170, 0);")

        self.verticalLayout_5.addWidget(self.pb_connect)


        self.horizontalLayout_8.addWidget(self.frame_12)

        self.line = QFrame(self.frame_10)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(200, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.le_ip = QLineEdit(self.frame_11)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setMaximumSize(QSize(16777215, 40))
        self.le_ip.setFont(font2)
        self.le_ip.setToolTipDuration(-1)
        self.le_ip.setStyleSheet(u"border-color: rgb(186, 186, 186);\n"
"background-color: rgb(186, 186, 186);\n"
"border-bottom-color: rgb(186, 186, 186);\n"
"border-top-color: rgb(186, 186, 186);")

        self.verticalLayout_6.addWidget(self.le_ip)

        self.le_port = QLineEdit(self.frame_11)
        self.le_port.setObjectName(u"le_port")
        self.le_port.setMaximumSize(QSize(16777215, 40))
        self.le_port.setFont(font2)
        self.le_port.setStyleSheet(u"border-color: rgb(186, 186, 186);\n"
"background-color: rgb(186, 186, 186);\n"
"border-bottom-color: rgb(186, 186, 186);\n"
"border-top-color: rgb(186, 186, 186);")

        self.verticalLayout_6.addWidget(self.le_port)

        self.rb_status = QRadioButton(self.frame_11)
        self.rb_status.setObjectName(u"rb_status")
        self.rb_status.setMaximumSize(QSize(16777215, 40))
        self.rb_status.setFont(font2)

        self.verticalLayout_6.addWidget(self.rb_status)

        self.pb_disconnect = QPushButton(self.frame_11)
        self.pb_disconnect.setObjectName(u"pb_disconnect")
        self.pb_disconnect.setMaximumSize(QSize(150, 40))
        self.pb_disconnect.setFont(font2)
        self.pb_disconnect.setStyleSheet(u"border: 2px solid ;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 0, 0);")

        self.verticalLayout_6.addWidget(self.pb_disconnect)


        self.horizontalLayout_8.addWidget(self.frame_11)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color: rgb(162, 162, 162);")

        self.verticalLayout_4.addWidget(self.label_9)

        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 120))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton = QPushButton(self.frame_16)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(150, 40))
        self.pushButton.setFont(font2)

        self.verticalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_16)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(150, 40))
        self.pushButton_2.setFont(font2)

        self.verticalLayout_7.addWidget(self.pushButton_2)


        self.horizontalLayout_9.addWidget(self.frame_16)

        self.line_2 = QFrame(self.frame_14)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line_2)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_3 = QPushButton(self.frame_15)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(150, 40))
        self.pushButton_3.setFont(font2)

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_15)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(150, 40))
        self.pushButton_4.setFont(font2)

        self.verticalLayout_8.addWidget(self.pushButton_4)


        self.horizontalLayout_9.addWidget(self.frame_15)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_13)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(163, 163, 163);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_rgb = QLabel(self.frame_6)
        self.lb_rgb.setObjectName(u"lb_rgb")
        self.lb_rgb.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.lb_rgb)

        self.lb_rgbd = QLabel(self.frame_6)
        self.lb_rgbd.setObjectName(u"lb_rgbd")
        self.lb_rgbd.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.horizontalLayout_4.addWidget(self.lb_rgbd)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setStyleSheet(u"background-color: rgb(162, 162, 162);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_detection = QLabel(self.frame_8)
        self.lb_detection.setObjectName(u"lb_detection")
        self.lb_detection.setStyleSheet(u"background-color: rgb(198, 198, 198);")

        self.horizontalLayout_6.addWidget(self.lb_detection)

        self.lb_parameters = QLabel(self.frame_8)
        self.lb_parameters.setObjectName(u"lb_parameters")
        self.lb_parameters.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.horizontalLayout_6.addWidget(self.lb_parameters)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_30 = QFrame(self.frame_3)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 50))
        self.frame_30.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pb_start = QPushButton(self.frame_30)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setFont(font2)

        self.horizontalLayout_14.addWidget(self.pb_start)

        self.pb_capture = QPushButton(self.frame_30)
        self.pb_capture.setObjectName(u"pb_capture")
        self.pb_capture.setFont(font2)

        self.horizontalLayout_14.addWidget(self.pb_capture)

        self.pb_grasp = QPushButton(self.frame_30)
        self.pb_grasp.setObjectName(u"pb_grasp")
        self.pb_grasp.setFont(font2)

        self.horizontalLayout_14.addWidget(self.pb_grasp)

        self.pb_open = QPushButton(self.frame_30)
        self.pb_open.setObjectName(u"pb_open")
        self.pb_open.setFont(font2)

        self.horizontalLayout_14.addWidget(self.pb_open)


        self.verticalLayout_3.addWidget(self.frame_30)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 50))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: rgb(162, 162, 162);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_5 = QPushButton(self.frame_18)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(100, 40))
        font3 = QFont()
        font3.setPointSize(22)
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_10.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_18)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(100, 40))
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_10.addWidget(self.pushButton_6)


        self.horizontalLayout_10.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_7 = QPushButton(self.frame_19)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(100, 40))
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_11.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_19)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(100, 40))
        self.pushButton_8.setFont(font3)
        self.pushButton_8.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_11.addWidget(self.pushButton_8)


        self.horizontalLayout_10.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_9 = QPushButton(self.frame_20)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(100, 40))
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_12.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_20)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(100, 40))
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_12.addWidget(self.pushButton_10)


        self.horizontalLayout_10.addWidget(self.frame_20)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.frame_21 = QFrame(self.frame_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_24)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_11 = QPushButton(self.frame_24)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(100, 40))
        self.pushButton_11.setFont(font3)
        self.pushButton_11.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_13.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_24)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(100, 40))
        self.pushButton_12.setFont(font3)
        self.pushButton_12.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_13.addWidget(self.pushButton_12)


        self.horizontalLayout_11.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_23)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_13 = QPushButton(self.frame_23)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(100, 40))
        self.pushButton_13.setFont(font3)
        self.pushButton_13.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_14.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_23)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(100, 40))
        self.pushButton_14.setFont(font3)
        self.pushButton_14.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_14.addWidget(self.pushButton_14)


        self.horizontalLayout_11.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_22)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton_15 = QPushButton(self.frame_22)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMaximumSize(QSize(100, 40))
        self.pushButton_15.setFont(font3)
        self.pushButton_15.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_15.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_22)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMaximumSize(QSize(100, 40))
        self.pushButton_16.setFont(font3)
        self.pushButton_16.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_15.addWidget(self.pushButton_16)


        self.horizontalLayout_11.addWidget(self.frame_22)


        self.verticalLayout_9.addWidget(self.frame_21)

        self.frame_25 = QFrame(self.frame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_28)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_17 = QPushButton(self.frame_28)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMaximumSize(QSize(100, 40))
        self.pushButton_17.setFont(font3)
        self.pushButton_17.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_16.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_28)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMaximumSize(QSize(100, 40))
        self.pushButton_18.setFont(font3)
        self.pushButton_18.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_16.addWidget(self.pushButton_18)


        self.horizontalLayout_12.addWidget(self.frame_28)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_27)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_19 = QPushButton(self.frame_27)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMaximumSize(QSize(100, 40))
        self.pushButton_19.setFont(font3)
        self.pushButton_19.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_17.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.frame_27)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMaximumSize(QSize(100, 40))
        self.pushButton_20.setFont(font3)
        self.pushButton_20.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_17.addWidget(self.pushButton_20)


        self.horizontalLayout_12.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_26)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pushButton_21 = QPushButton(self.frame_26)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMaximumSize(QSize(100, 40))
        self.pushButton_21.setFont(font3)
        self.pushButton_21.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_18.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_26)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMaximumSize(QSize(100, 40))
        self.pushButton_22.setFont(font3)
        self.pushButton_22.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_18.addWidget(self.pushButton_22)


        self.horizontalLayout_12.addWidget(self.frame_26)


        self.verticalLayout_9.addWidget(self.frame_25)

        self.frame_29 = QFrame(self.frame_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 50))
        self.frame_29.setStyleSheet(u"background-color: rgb(195, 195, 195);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pb_reset = QPushButton(self.frame_29)
        self.pb_reset.setObjectName(u"pb_reset")
        self.pb_reset.setMaximumSize(QSize(16777215, 40))
        self.pb_reset.setFont(font2)

        self.horizontalLayout_13.addWidget(self.pb_reset)

        self.pb_saveas = QPushButton(self.frame_29)
        self.pb_saveas.setObjectName(u"pb_saveas")
        self.pb_saveas.setMaximumSize(QSize(16777215, 40))
        self.pb_saveas.setFont(font2)

        self.horizontalLayout_13.addWidget(self.pb_saveas)

        self.pb_save = QPushButton(self.frame_29)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setMaximumSize(QSize(16777215, 40))
        self.pb_save.setFont(font2)

        self.horizontalLayout_13.addWidget(self.pb_save)


        self.verticalLayout_9.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.frame_2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_31)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_subscript = QFrame(MainForm)
        self.frame_subscript.setObjectName(u"frame_subscript")
        self.frame_subscript.setMaximumSize(QSize(16777215, 50))
        self.frame_subscript.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.frame_subscript.setFrameShape(QFrame.StyledPanel)
        self.frame_subscript.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_subscript)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_subscript = QLabel(self.frame_subscript)
        self.lb_subscript.setObjectName(u"lb_subscript")
        font4 = QFont()
        font4.setBold(False)
        self.lb_subscript.setFont(font4)
        self.lb_subscript.setStyleSheet(u"color: rgb(85, 255, 0);")
        self.lb_subscript.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_subscript)


        self.verticalLayout_2.addWidget(self.frame_subscript)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Form", None))
        self.lb_thk.setText(QCoreApplication.translate("MainForm", u"THK 1.0", None))
        self.label_4.setText(QCoreApplication.translate("MainForm", u"Status", None))
        self.label_5.setText(QCoreApplication.translate("MainForm", u"IP", None))
        self.label_7.setText(QCoreApplication.translate("MainForm", u"Port", None))
        self.label_8.setText(QCoreApplication.translate("MainForm", u"Status", None))
        self.pb_connect.setText(QCoreApplication.translate("MainForm", u"Connect", None))
        self.rb_status.setText(QCoreApplication.translate("MainForm", u"Connected", None))
        self.pb_disconnect.setText(QCoreApplication.translate("MainForm", u"Disconnect", None))
        self.label_9.setText(QCoreApplication.translate("MainForm", u"Hand", None))
        self.pushButton.setText(QCoreApplication.translate("MainForm", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainForm", u"Load", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainForm", u"Save", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainForm", u"Delete", None))
        self.label_2.setText(QCoreApplication.translate("MainForm", u"RGB", None))
        self.label.setText(QCoreApplication.translate("MainForm", u"RGB_D", None))
        self.lb_rgb.setText("")
        self.lb_rgbd.setText("")
        self.label_3.setText(QCoreApplication.translate("MainForm", u"Detection", None))
        self.label_6.setText(QCoreApplication.translate("MainForm", u"Parameters", None))
        self.lb_detection.setText("")
        self.lb_parameters.setText("")
        self.pb_start.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.pb_capture.setText(QCoreApplication.translate("MainForm", u"Capture", None))
        self.pb_grasp.setText(QCoreApplication.translate("MainForm", u"Grasp", None))
        self.pb_open.setText(QCoreApplication.translate("MainForm", u"Open", None))
        self.label_10.setText(QCoreApplication.translate("MainForm", u"JOG", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pb_reset.setText(QCoreApplication.translate("MainForm", u"Reset", None))
        self.pb_saveas.setText(QCoreApplication.translate("MainForm", u"Save As", None))
        self.pb_save.setText(QCoreApplication.translate("MainForm", u"Save", None))
        self.lb_subscript.setText(QCoreApplication.translate("MainForm", u"Powered by Chizu Denki Co., Ltd.", None))
    # retranslateUi

