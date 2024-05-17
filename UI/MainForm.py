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
        MainForm.resize(1363, 863)
        font = QFont()
        font.setPointSize(12)
        MainForm.setFont(font)
        MainForm.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.verticalLayout_2 = QVBoxLayout(MainForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Frame_Title = QFrame(MainForm)
        self.Frame_Title.setObjectName(u"Frame_Title")
        self.Frame_Title.setMaximumSize(QSize(16777215, 50))
        self.Frame_Title.setStyleSheet(u"background-color: rgb(84, 84, 84);")
        self.Frame_Title.setFrameShape(QFrame.StyledPanel)
        self.Frame_Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_Title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_LexxPluss = QLabel(self.Frame_Title)
        self.lb_LexxPluss.setObjectName(u"lb_LexxPluss")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        self.lb_LexxPluss.setFont(font1)
        self.lb_LexxPluss.setStyleSheet(u"color: rgb(232, 232, 232);")
        self.lb_LexxPluss.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_LexxPluss)


        self.verticalLayout_2.addWidget(self.Frame_Title)

        self.frame_2 = QFrame(MainForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(1600, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(1000, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(118, 118, 118);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(118, 118, 118);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(500, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(106, 106, 106);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(122, 122, 122);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_15)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_22 = QFrame(self.frame_17)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(200, 16777215))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_22)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lb_ip = QLabel(self.frame_22)
        self.lb_ip.setObjectName(u"lb_ip")
        self.lb_ip.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setPointSize(18)
        self.lb_ip.setFont(font2)
        self.lb_ip.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.lb_ip)

        self.lb_port = QLabel(self.frame_22)
        self.lb_port.setObjectName(u"lb_port")
        self.lb_port.setMaximumSize(QSize(150, 16777215))
        self.lb_port.setFont(font2)
        self.lb_port.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.lb_port)

        self.lb_status = QLabel(self.frame_22)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMaximumSize(QSize(150, 16777215))
        self.lb_status.setFont(font2)
        self.lb_status.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.lb_status)

        self.pb_connect = QPushButton(self.frame_22)
        self.pb_connect.setObjectName(u"pb_connect")
        self.pb_connect.setMaximumSize(QSize(150, 16777215))
        self.pb_connect.setFont(font2)
        self.pb_connect.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 170, 0);\n"
"")

        self.verticalLayout_22.addWidget(self.pb_connect)


        self.horizontalLayout_10.addWidget(self.frame_22)

        self.line_5 = QFrame(self.frame_17)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(95, 95, 95);")
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_5)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(200, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_21)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.le_ip = QLineEdit(self.frame_21)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setPointSize(14)
        self.le_ip.setFont(font3)
        self.le_ip.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-color: rgb(211, 211, 211);")

        self.verticalLayout_23.addWidget(self.le_ip)

        self.le_port = QLineEdit(self.frame_21)
        self.le_port.setObjectName(u"le_port")
        self.le_port.setMaximumSize(QSize(150, 16777215))
        self.le_port.setFont(font3)
        self.le_port.setStyleSheet(u"background-color: rgb(211, 211, 211);\n"
"border-color: rgb(211, 211, 211);")

        self.verticalLayout_23.addWidget(self.le_port)

        self.rb_status = QRadioButton(self.frame_21)
        self.rb_status.setObjectName(u"rb_status")
        self.rb_status.setMaximumSize(QSize(150, 16777215))
        self.rb_status.setFont(font2)

        self.verticalLayout_23.addWidget(self.rb_status)

        self.pb_disconnect = QPushButton(self.frame_21)
        self.pb_disconnect.setObjectName(u"pb_disconnect")
        self.pb_disconnect.setMaximumSize(QSize(150, 16777215))
        self.pb_disconnect.setFont(font2)
        self.pb_disconnect.setStyleSheet(u"border: 2px solid ;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 0, 0);\n"
"")

        self.verticalLayout_23.addWidget(self.pb_disconnect)


        self.horizontalLayout_10.addWidget(self.frame_21)


        self.verticalLayout_21.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(182, 182, 182);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_19)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.pushButton_30 = QPushButton(self.frame_19)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setFont(font)

        self.verticalLayout_24.addWidget(self.pushButton_30)

        self.pushButton_32 = QPushButton(self.frame_19)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setFont(font)

        self.verticalLayout_24.addWidget(self.pushButton_32)


        self.horizontalLayout_11.addWidget(self.frame_19)

        self.line_4 = QFrame(self.frame_18)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(83, 83, 83);")
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_4)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pushButton_31 = QPushButton(self.frame_20)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setFont(font)

        self.verticalLayout_25.addWidget(self.pushButton_31)

        self.pushButton_33 = QPushButton(self.frame_20)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setFont(font)

        self.verticalLayout_25.addWidget(self.pushButton_33)


        self.horizontalLayout_11.addWidget(self.frame_20)


        self.verticalLayout_21.addWidget(self.frame_18)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(122, 122, 122);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_16)


        self.horizontalLayout_9.addWidget(self.frame_14)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(22, 22, 22);\n"
"background-color: rgb(38, 38, 38);")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(500, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(118, 118, 118);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(140, 140, 140);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(148, 148, 148);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame)

        self.line_2 = QFrame(self.frame_7)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(120, 120, 120);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_23 = QFrame(self.frame_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 50))
        self.frame_23.setStyleSheet(u"background-color: rgb(124, 124, 124);")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_35 = QPushButton(self.frame_23)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMaximumSize(QSize(100, 16777215))
        self.pushButton_35.setFont(font2)
        self.pushButton_35.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 170, 0);\n"
"")

        self.horizontalLayout_12.addWidget(self.pushButton_35)

        self.pushButton_34 = QPushButton(self.frame_23)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMaximumSize(QSize(100, 16777215))
        self.pushButton_34.setFont(font2)
        self.pushButton_34.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_12.addWidget(self.pushButton_34)

        self.pushButton_36 = QPushButton(self.frame_23)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMaximumSize(QSize(100, 16777215))
        self.pushButton_36.setFont(font2)
        self.pushButton_36.setStyleSheet(u"border: 2px solid ;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 170, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_12.addWidget(self.pushButton_36)


        self.verticalLayout_7.addWidget(self.frame_23)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.line_3 = QFrame(self.frame_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.line_6 = QFrame(self.frame_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_6)

        self.frame_StatCtrlPanel = QFrame(self.frame_2)
        self.frame_StatCtrlPanel.setObjectName(u"frame_StatCtrlPanel")
        self.frame_StatCtrlPanel.setMaximumSize(QSize(500, 16777215))
        self.frame_StatCtrlPanel.setStyleSheet(u"background-color: rgb(124, 124, 124);")
        self.frame_StatCtrlPanel.setFrameShape(QFrame.StyledPanel)
        self.frame_StatCtrlPanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_StatCtrlPanel)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_pb = QFrame(self.frame_StatCtrlPanel)
        self.frame_pb.setObjectName(u"frame_pb")
        self.frame_pb.setStyleSheet(u"background-color: rgb(166, 166, 166);\n"
"\n"
"")
        self.frame_pb.setFrameShape(QFrame.StyledPanel)
        self.frame_pb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_pb)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.frame_pb)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(16)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.frameFinger_1 = QFrame(self.frame_pb)
        self.frameFinger_1.setObjectName(u"frameFinger_1")
        self.frameFinger_1.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameFinger_1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frameFinger_1_L1 = QFrame(self.frameFinger_1)
        self.frameFinger_1_L1.setObjectName(u"frameFinger_1_L1")
        self.frameFinger_1_L1.setMaximumSize(QSize(16777215, 16777215))
        self.frameFinger_1_L1.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;\n"
"")
        self.frameFinger_1_L1.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_1_L1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frameFinger_1_L1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_6 = QPushButton(self.frameFinger_1_L1)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_11.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frameFinger_1_L1)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font4)
        self.pushButton_7.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_11.addWidget(self.pushButton_7)


        self.horizontalLayout_4.addWidget(self.frameFinger_1_L1)

        self.frameFinger_1_L2 = QFrame(self.frameFinger_1)
        self.frameFinger_1_L2.setObjectName(u"frameFinger_1_L2")
        self.frameFinger_1_L2.setMaximumSize(QSize(16777215, 16777215))
        self.frameFinger_1_L2.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_1_L2.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_1_L2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameFinger_1_L2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_2 = QPushButton(self.frameFinger_1_L2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frameFinger_1_L2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addWidget(self.frameFinger_1_L2)

        self.frameFinger_1_R1 = QFrame(self.frameFinger_1)
        self.frameFinger_1_R1.setObjectName(u"frameFinger_1_R1")
        self.frameFinger_1_R1.setMaximumSize(QSize(16777215, 16777215))
        self.frameFinger_1_R1.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_1_R1.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_1_R1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frameFinger_1_R1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_4 = QPushButton(self.frameFinger_1_R1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_8.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frameFinger_1_R1)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_8.addWidget(self.pushButton_5)


        self.horizontalLayout_4.addWidget(self.frameFinger_1_R1)


        self.verticalLayout_10.addWidget(self.frameFinger_1)

        self.frame_10 = QFrame(self.frame_pb)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frameFinger_2_L1 = QFrame(self.frame_10)
        self.frameFinger_2_L1.setObjectName(u"frameFinger_2_L1")
        self.frameFinger_2_L1.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_2_L1.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_2_L1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frameFinger_2_L1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_8 = QPushButton(self.frameFinger_2_L1)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_8.setFont(font4)
        self.pushButton_8.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_12.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frameFinger_2_L1)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font4)
        self.pushButton_9.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_12.addWidget(self.pushButton_9)


        self.horizontalLayout_5.addWidget(self.frameFinger_2_L1)

        self.frameFinger_2_L2 = QFrame(self.frame_10)
        self.frameFinger_2_L2.setObjectName(u"frameFinger_2_L2")
        self.frameFinger_2_L2.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_2_L2.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_2_L2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frameFinger_2_L2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_10 = QPushButton(self.frameFinger_2_L2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font4)
        self.pushButton_10.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_13.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frameFinger_2_L2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font4)
        self.pushButton_11.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_13.addWidget(self.pushButton_11)


        self.horizontalLayout_5.addWidget(self.frameFinger_2_L2)

        self.frameFinger_2_R1 = QFrame(self.frame_10)
        self.frameFinger_2_R1.setObjectName(u"frameFinger_2_R1")
        self.frameFinger_2_R1.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_2_R1.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_2_R1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frameFinger_2_R1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_12 = QPushButton(self.frameFinger_2_R1)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font4)
        self.pushButton_12.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_14.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frameFinger_2_R1)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font4)
        self.pushButton_13.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_14.addWidget(self.pushButton_13)


        self.horizontalLayout_5.addWidget(self.frameFinger_2_R1)


        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_pb)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frameFinger_3_L1 = QFrame(self.frame_11)
        self.frameFinger_3_L1.setObjectName(u"frameFinger_3_L1")
        self.frameFinger_3_L1.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_3_L1.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_3_L1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frameFinger_3_L1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_16 = QPushButton(self.frameFinger_3_L1)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font4)
        self.pushButton_16.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_16.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frameFinger_3_L1)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font4)
        self.pushButton_17.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_16.addWidget(self.pushButton_17)


        self.horizontalLayout_6.addWidget(self.frameFinger_3_L1)

        self.frameFinger_3_L2 = QFrame(self.frame_11)
        self.frameFinger_3_L2.setObjectName(u"frameFinger_3_L2")
        self.frameFinger_3_L2.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_3_L2.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_3_L2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frameFinger_3_L2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton_18 = QPushButton(self.frameFinger_3_L2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font4)
        self.pushButton_18.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_15.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.frameFinger_3_L2)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFont(font4)
        self.pushButton_19.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_15.addWidget(self.pushButton_19)


        self.horizontalLayout_6.addWidget(self.frameFinger_3_L2)

        self.frameFinger_3_R1 = QFrame(self.frame_11)
        self.frameFinger_3_R1.setObjectName(u"frameFinger_3_R1")
        self.frameFinger_3_R1.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_3_R1.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_3_R1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frameFinger_3_R1)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_14 = QPushButton(self.frameFinger_3_R1)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font4)
        self.pushButton_14.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_17.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.frameFinger_3_R1)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font4)
        self.pushButton_15.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_17.addWidget(self.pushButton_15)


        self.horizontalLayout_6.addWidget(self.frameFinger_3_R1)


        self.verticalLayout_10.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_pb)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frameFinger_4_L1 = QFrame(self.frame_12)
        self.frameFinger_4_L1.setObjectName(u"frameFinger_4_L1")
        self.frameFinger_4_L1.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_4_L1.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_4_L1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frameFinger_4_L1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.pushButton_25 = QPushButton(self.frameFinger_4_L1)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setFont(font4)
        self.pushButton_25.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_20.addWidget(self.pushButton_25)

        self.pushButton_24 = QPushButton(self.frameFinger_4_L1)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setFont(font4)
        self.pushButton_24.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_20.addWidget(self.pushButton_24)


        self.horizontalLayout_7.addWidget(self.frameFinger_4_L1)

        self.frameFinger_4_L2 = QFrame(self.frame_12)
        self.frameFinger_4_L2.setObjectName(u"frameFinger_4_L2")
        self.frameFinger_4_L2.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_4_L2.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_4_L2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frameFinger_4_L2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_23 = QPushButton(self.frameFinger_4_L2)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setFont(font4)
        self.pushButton_23.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_19.addWidget(self.pushButton_23)

        self.pushButton_22 = QPushButton(self.frameFinger_4_L2)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setFont(font4)
        self.pushButton_22.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_19.addWidget(self.pushButton_22)


        self.horizontalLayout_7.addWidget(self.frameFinger_4_L2)

        self.frameFinger_4_R2 = QFrame(self.frame_12)
        self.frameFinger_4_R2.setObjectName(u"frameFinger_4_R2")
        self.frameFinger_4_R2.setStyleSheet(u"background-color: rgb(110, 110, 110);\n"
"border-radius: 5px;")
        self.frameFinger_4_R2.setFrameShape(QFrame.StyledPanel)
        self.frameFinger_4_R2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frameFinger_4_R2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pushButton_21 = QPushButton(self.frameFinger_4_R2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setFont(font4)
        self.pushButton_21.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_18.addWidget(self.pushButton_21)

        self.pushButton_20 = QPushButton(self.frameFinger_4_R2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font4)
        self.pushButton_20.setStyleSheet(u"border: 2px solid ;\n"
"border-color: rgb(197, 197, 197);\n"
"border-radius: 5px;\n"
"background-color: rgba(52, 131, 74, 1);\n"
"color: rgb(25, 25, 25);")

        self.verticalLayout_18.addWidget(self.pushButton_20)


        self.horizontalLayout_7.addWidget(self.frameFinger_4_R2)


        self.verticalLayout_10.addWidget(self.frame_12)


        self.verticalLayout_9.addWidget(self.frame_pb)

        self.frame_9 = QFrame(self.frame_StatCtrlPanel)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setStyleSheet(u"background-color: rgb(99, 99, 99);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pb_reset = QPushButton(self.frame_9)
        self.pb_reset.setObjectName(u"pb_reset")
        self.pb_reset.setFont(font3)
        self.pb_reset.setStyleSheet(u"border: 2px solid ;\n"
"border-radius: 5px;\n"
"border-color: rgb(255, 116, 195);\n"
"background-color: rgb(255, 116, 195);\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_8.addWidget(self.pb_reset)

        self.pb_saveAs = QPushButton(self.frame_9)
        self.pb_saveAs.setObjectName(u"pb_saveAs")
        self.pb_saveAs.setFont(font4)
        self.pb_saveAs.setStyleSheet(u"border: 2px solid ;\n"
"border-radius: 5px;\n"
"border-color: rgb(0, 132, 0);\n"
"background-color: rgb(0, 132, 0);\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_8.addWidget(self.pb_saveAs)

        self.pb_save = QPushButton(self.frame_9)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setFont(font4)
        self.pb_save.setStyleSheet(u"border: 2px solid ;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 132, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 132, 0);\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.pb_save)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_13 = QFrame(self.frame_StatCtrlPanel)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_13)


        self.horizontalLayout_2.addWidget(self.frame_StatCtrlPanel)


        self.verticalLayout_2.addWidget(self.frame_2)

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
        font5 = QFont()
        font5.setBold(False)
        self.lb_subscript.setFont(font5)
        self.lb_subscript.setStyleSheet(u"color: rgb(85, 255, 0);")
        self.lb_subscript.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_subscript)


        self.verticalLayout_2.addWidget(self.frame_subscript)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Form", None))
        self.lb_LexxPluss.setText(QCoreApplication.translate("MainForm", u"THK 1.0", None))
        self.lb_ip.setText(QCoreApplication.translate("MainForm", u"IP", None))
        self.lb_port.setText(QCoreApplication.translate("MainForm", u"Port", None))
        self.lb_status.setText(QCoreApplication.translate("MainForm", u"Status", None))
        self.pb_connect.setText(QCoreApplication.translate("MainForm", u"Connect", None))
        self.le_ip.setPlaceholderText(QCoreApplication.translate("MainForm", u"Enter ip address", None))
        self.le_port.setPlaceholderText(QCoreApplication.translate("MainForm", u"Enter port no.", None))
        self.rb_status.setText(QCoreApplication.translate("MainForm", u"Connected", None))
        self.pb_disconnect.setText(QCoreApplication.translate("MainForm", u"Disconnect", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainForm", u"Add", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainForm", u"Load", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainForm", u"Save", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainForm", u"Delete", None))
        self.label_2.setText(QCoreApplication.translate("MainForm", u"Detection", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainForm", u"Capture", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainForm", u"Grasp", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainForm", u"Open", None))
        self.label.setText(QCoreApplication.translate("MainForm", u"JOG ", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainForm", u"+", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainForm", u"-", None))
        self.pb_reset.setText(QCoreApplication.translate("MainForm", u"Reset", None))
        self.pb_saveAs.setText(QCoreApplication.translate("MainForm", u"Save As", None))
        self.pb_save.setText(QCoreApplication.translate("MainForm", u"Save ", None))
        self.lb_subscript.setText(QCoreApplication.translate("MainForm", u"Powered by Chizu Denki Co., Ltd.", None))
    # retranslateUi

