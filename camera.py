from PyQt5 import QtCore, QtGui, QtWidgets
import connection 
import cv2
import os
import face_recognition
import glob
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import sys
import matplotlib.pyplot as plt

class Ui_camera(object):
    def setupUi(self, camera):
        camera.setObjectName("camera")
        camera.resize(938, 565)
        camera.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        camera.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(camera)
        self.widget.setGeometry(QtCore.QRect(70, 20, 802, 501))
        self.widget.setStyleSheet("background:rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"")
        self.widget.setObjectName("widget")
        self.menubar_2 = QtWidgets.QLabel(self.widget)
        self.menubar_2.setGeometry(QtCore.QRect(0, 0, 191, 501))
        self.menubar_2.setStyleSheet("background-color: rgb(165, 165, 189);\n"
"border-rabius: none; ")
        self.menubar_2.setText("")
        self.menubar_2.setObjectName("menubar_2")
        self.dashboard = QtWidgets.QPushButton(self.widget)
        self.dashboard.setGeometry(QtCore.QRect(0, 151, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dashboard.setFont(font)
        self.dashboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dashboard.setStyleSheet("QPushButton#dashboard{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#dashboard:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#dashboard:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")
        self.dashboard.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\dashboard.png'))
        self.dashboard.setObjectName("dashboard")
        self.employee = QtWidgets.QPushButton(self.widget)
        self.employee.setGeometry(QtCore.QRect(0, 187, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.employee.setFont(font)
        self.employee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.employee.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"\n"
"")
        self.employee.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\group.png'))
        self.employee.setObjectName("employee")
        self.rapport = QtWidgets.QPushButton(self.widget)
        self.rapport.setGeometry(QtCore.QRect(0, 223, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rapport.setFont(font)
        self.rapport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rapport.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")
        self.rapport.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\rapport.png'))
        self.rapport.setObjectName("rapport")
        self.terminer = QtWidgets.QPushButton(self.widget)
        self.terminer.setGeometry(QtCore.QRect(0, 450, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.terminer.setFont(font)
        self.terminer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.terminer.setStyleSheet("QPushButton#terminer{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#terminer:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#terminer:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")
        self.terminer.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\exit.png'))
        self.terminer.setObjectName("terminer")
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setGeometry(QtCore.QRect(60, 5, 61, 61))
        self.logo.setStyleSheet("\n"
"    background-image: url(:/logo/face-detection.png);\n"
"   background-color:none;\n"
" ")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 70, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;\n"
"background-color: none;\n"
"color: #887575;")
        self.label.setObjectName("label")
        self.recherche = QtWidgets.QLineEdit(self.widget)
        self.recherche.setGeometry(QtCore.QRect(270, 30, 311, 20))
        self.recherche.setStyleSheet("                max-width: 300px;\n"
"                padding: 0px 12px; \n"
"                border-radius: 8px;\n"
"                border: 1px solid #000000;\n"
"                outline: none;\n"
"                box-shadow: 0px 0px 20px -18px; ")
        self.recherche.setObjectName("recherche")
        self.user_pic = QtWidgets.QLabel(self.widget)
        self.user_pic.setGeometry(QtCore.QRect(740, 20, 40, 40))
        self.user_pic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_pic.setStyleSheet("\n"
"    width: 40px; \n"
"    height: 40px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 20px;\n"
"\n"
"")
        self.user_pic.setText("")
        self.user_pic.setObjectName("user_pic")
        self.userName = QtWidgets.QLabel(self.widget)
        self.userName.setGeometry(QtCore.QRect(672, 30, 51, 16))
        self.userName.setObjectName("userName")
        self.notification_btn = QtWidgets.QPushButton(self.widget)
        self.notification_btn.setGeometry(QtCore.QRect(620, 30, 21, 21))
        self.notification_btn.setStyleSheet("        QPushButton{ \n"
"        border: none;\n"
"        }\n"
"        QPushButton:hover{\n"
"         border: #B3D9E4;                           \n"
"        }  ")
        self.notification_btn.setText("")
        self.notification_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\not.png'))
        self.notification_btn.setObjectName("notification_btn")
        self.recherche_btn = QtWidgets.QPushButton(self.widget)
        self.recherche_btn.setGeometry(QtCore.QRect(550, 31, 15, 15))
        self.recherche_btn.setStyleSheet("        QPushButton{ \n"
"        border: none;\n"
"        }\n"
"        QPushButton:hover{\n"
"         border: #B3D9E4;                           \n"
"        }  ")
        self.recherche_btn.setText("")
        self.recherche_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\glass.png'))
        self.recherche_btn.setObjectName("recherche_btn")
        self.close_btn = QtWidgets.QPushButton(self.widget)
        self.close_btn.setGeometry(QtCore.QRect(784, 10, 10, 10))
        self.close_btn.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 60, 63);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(255, 90, 93);\n"
"}")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.close_btn.clicked.connect(exit)
        def reduir():
            camera.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.widget)
        self.reduit.clicked.connect(reduir)
        self.reduit.setGeometry(QtCore.QRect(770, 10, 10, 10))
        self.reduit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(84, 255, 90);\n"
"}")
        self.reduit.setText("")
        self.reduit.setObjectName("reduit")
        self.cam = QtWidgets.QPushButton(self.widget)
        self.cam.setGeometry(QtCore.QRect(0, 260, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cam.setFont(font)
        self.cam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cam.setStyleSheet("\n"
"background-color:#D9D9D9;\n"
"border-radius: 0px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"\n"
"")
        self.cam.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\camera.png'))
        self.cam.setObjectName("cam")
        self.themr = QtWidgets.QPushButton(self.widget)
        self.themr.setGeometry(QtCore.QRect(0, 414, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.themr.setFont(font)
        self.themr.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}")
        self.themr.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\theme.png'))
        self.themr.setObjectName("themr")
        self.profil = QtWidgets.QPushButton(self.widget)
        self.profil.setGeometry(QtCore.QRect(0, 377, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.profil.setFont(font)
        self.profil.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}")
        self.profil.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\user.png'))
        self.profil.setObjectName("profil")
        self.hide_btn = QtWidgets.QPushButton(self.widget)
        self.hide_btn.setGeometry(QtCore.QRect(150, 10, 31, 23))
        self.hide_btn.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}")
        self.hide_btn.setText("")
        self.hide_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\menu.png'))
        self.hide_btn.setObjectName("hide_btn")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(199, 79, 591, 411))
        self.widget_2.setObjectName("widget_2")
        self.stat = QtWidgets.QLabel(self.widget_2)
        self.stat.setGeometry(QtCore.QRect(10, 10, 190, 190))
        self.stat.setStyleSheet("background-color: rgb(226, 255, 239);\n"
"border-radius: 95px;\n"
"")
        self.stat.setText("")
        self.stat.setObjectName("stat")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(60, 240, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(60, 300, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 31, 16))
        self.label_5.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 7px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 31, 16))
        self.label_6.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 7px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(10, 300, 31, 16))
        self.label_7.setStyleSheet("background-color: rgb(130, 0, 0);\n"
"border-radius: 7px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.cam_2 = QtWidgets.QLabel(self.widget_2)
        self.cam_2.setGeometry(QtCore.QRect(290, 10, 291, 161))
        self.cam_2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.cam_2.setText("")
        self.cam_2.setObjectName("cam_2")
        self.fullscreen = QtWidgets.QPushButton(self.widget_2)
        self.fullscreen.setGeometry(QtCore.QRect(550, 140, 21, 23))
        self.fullscreen.setStyleSheet("background-color: none;\n"
"")
        self.fullscreen.setText("")
        self.fullscreen.setObjectName("fullscreen")
        self.fullscreen.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\full.png'))
        self.listabsence = QtWidgets.QTableWidget(self.widget_2)
        self.listabsence.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: rgb(176, 111, 255); \n"
"}\n"
"")
        self.listabsence.setGeometry(QtCore.QRect(295, 231, 300, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listabsence.setFont(font)
        self.listabsence.setObjectName("listabsence")
        self.listabsence.setColumnCount(3)
        self.listabsence.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listabsence.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listabsence.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listabsence.setHorizontalHeaderItem(2, item)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(10, 340, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.bannee = QtWidgets.QPushButton(self.widget_2)
        self.bannee.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\ban.png'))
        self.bannee.setGeometry(QtCore.QRect(30, 370, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bannee.setFont(font)
        self.bannee.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"\n"
"")
        self.bannee.setObjectName("bannee")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(393, 200, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.bannee.clicked.connect(self.open_ban)
        self.terminer.clicked.connect(self.close)
        self.fullscreen.clicked.connect(self.fullCam)
        
        self.retranslateUi(camera)
        QtCore.QMetaObject.connectSlotsByName(camera)

        self.cap = cv2.VideoCapture(0)

        self.known_faces = []
        self.known_names = []
        self.face_detect_time = None

        self.registered_faces = 'registred/'

        for name in os.listdir(self.registered_faces):
            images_mask = os.path.join(self.registered_faces, name, '*.jpg')
            images_paths = glob.glob(images_mask)
            for image_path in images_paths:
                encoding = self.get_encoding(image_path)
                if encoding is not None:
                    self.known_faces.append(encoding)
                    self.known_names.append(name)

        self.timer = QTimer(camera)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self.conn = connection.connection

        self.statistique()
        self.conn = connection.connection

        self.name = None
        self.pic_path = None

        self.dashboard.clicked.connect(lambda: self.open_Dash(self.name, self.pic_path))
        self.rapport.clicked.connect(lambda: self.open_rappot(self.name, self.pic_path))
        self.employee.clicked.connect(lambda: self.open_emp(self.name, self.pic_path))
        self.terminer.clicked.connect(self.close)
        self.profil.clicked.connect(lambda: self.open_profile(self.name, self.pic_path))

    def set_user_info(self, name, pic_path):
         self.name = name
         self.pic_path = pic_path
         self.update_user_info()

    def update_user_info(self):
         if self.name:
              self.userName.setText(self.name)
         if self.pic_path:
              pixmap = QPixmap(self.pic_path)
              pixmap = pixmap.scaled(40, 40)
              pixmap = self.cercle(pixmap)
              self.user_pic.setPixmap(pixmap)
    
    def cercle(self, pixmap):
        size = pixmap.size()
        mask = QPixmap(size)
        mask.fill(Qt.transparent)

        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawEllipse(0, 0, size.width(), size.height())
        painter.end()

        result = QPixmap(size)
        result.fill(Qt.transparent)

        painter.begin(result)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)
        painter.drawPixmap(0, 0, mask)
        painter.end()

        return result

    def fig_to_pixmap(self, fig):
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        fig.savefig(buffer, format='png')
        pixmap = QtGui.QPixmap()  
        pixmap.loadFromData(buffer.data())
        pixmap = pixmap.scaled(190, 190)
        buffer.close()
        return pixmap
    
    def emp_nperformer_count(self):
        conn = connection.connection
        cursor = conn.cursor()

        emp = "SELECT count(*) FROM EMP WHERE temp_arrive IS NULL;"
        cursor.execute(emp)
        result = cursor.fetchone()
        count = str(result[0]) if result else 0  
        return count

    def emp_performer_count(self):
         conn = connection.connection
         cursor = conn.cursor()

         project = "select count(*) from emp WHere temp_arrive IS NOT NULL"
         cursor.execute(project)
         result = cursor.fetchone()
         count = str(result[0]) if result else 0  
         return count

    def baner_count(self):
        conn = connection.connection
        cursor = conn.cursor()

        rapport = "select count(*) from banee"
        cursor.execute(rapport)
        result = cursor.fetchone()
        count = str(result[0]) if result else 0  
        return count

    def statistique(self):
        
        nPerformer = self.emp_nperformer_count()
        Performer = self.emp_performer_count()
        banne = self.baner_count()

        colors = [(255/255, 60/255, 63/255), (0/255, 170/255, 0/255), (120/255, 0/255, 0/255)]  
        size = [int(nPerformer), int(Performer), int(banne)]
        print("Size list:", size)
        total = sum(size)

        if total == 0:
                print("Toutes les parts sont nulles. Le diagramme ne peut pas être affiché.")
                return
        
        fig, ax = plt.subplots(figsize=(2, 2))
        ax.pie(size, autopct='%1.1f%%', startangle=100, colors=colors)
        ax.axis('equal')

        pixmap = self.fig_to_pixmap(fig)

        self.stat.setPixmap(pixmap)

    def open_ban(self):
         from banée import Ui_banee
         self.work_window = QtWidgets.QMainWindow()
         self.work = Ui_banee()
         self.work.setupUi(self.work_window)
         self.work_window.show()
         def hide():
             self.work_window.hide()
         self.work.close.clicked.connect(hide)

    def fullCam(self):
        from fullScreen import Ui_cam
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_cam()
        self.work.setupUi(self.work_window)
        self.work_window.show()

    def close(self):
        from close import Ui_quitter
        self.Close = QtWidgets.QMainWindow()
        self.work = Ui_quitter()
        self.work.setupUi(self.Close)
        self.Close.show()
        def hide():
            self.work.logOut
            camera.hide()
        self.work.oui.clicked.connect(hide)    
        def close():
            self.Close.hide()
        self.work.non.clicked.connect(close)
       

    def retranslateUi(self, camera):
        _translate = QtCore.QCoreApplication.translate
        camera.setWindowTitle(_translate("camera", "camera"))
        self.dashboard.setText(_translate("camera", "Tableau de bord"))
        self.employee.setText(_translate("camera", "Employée           "))
        self.rapport.setText(_translate("camera", "Rapport               "))
        self.terminer.setText(_translate("camera", "Quitter                 "))
        self.label.setText(_translate("camera", "Face smart project"))
        self.recherche.setPlaceholderText(_translate("camera", "Rechercher ici ..."))
        self.userName.setText(_translate("camera", "user name"))
        self.cam.setText(_translate("camera", "Camera               "))
        self.themr.setText(_translate("camera", "Théme                 "))
        self.profil.setText(_translate("camera", "Profil                    "))
        self.label_2.setText(_translate("camera", "Nom Pércameraer"))
        self.label_3.setText(_translate("camera", "Pércameraer"))
        self.label_4.setText(_translate("camera", "Bannée"))
        item = self.listabsence.horizontalHeaderItem(0)
        item.setText(_translate("camera", "Cin"))
        item = self.listabsence.horizontalHeaderItem(1)
        item.setText(_translate("camera", "Nom"))
        item = self.listabsence.horizontalHeaderItem(2)
        item.setText(_translate("camera", "Prénom"))
        self.label_9.setText(_translate("camera", "Bannée un Pérsonne"))
        self.bannee.setText(_translate("camera", "Bannée"))
        self.label_10.setText(_translate("camera", "Liste d\'absence"))

    def get_encoding(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)
        if len(face_encoding) > 0:
            return face_encoding[0]
        return None

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame_rgb)

        for face in faces:
            top, right, bottom, left = face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            encoding = face_recognition.face_encodings(frame_rgb, [face])[0]

            rst = face_recognition.compare_faces(self.known_faces, encoding)

            if any(rst):
                name = self.known_names[rst.index(True)]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 128, 0), 2)
                cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 128, 0), 2)
                if name == 'banned':
                        name = 'banned'
                        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
                        cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                        continue  
            
            else:
                name = 'inconnue'
                cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            frame = cv2.resize(frame, (640, 480))
            image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.cam_2.setPixmap(pixmap.scaled(291, 161))

        cursor = self.conn.cursor()
        if faces:
            if self.face_detect_time is None:
                self.face_detect_time = datetime.now()
                self.last_detection_day = self.face_detect_time.date()
                insert_last = "update EMP set temp_arrive = ? where cin = ?;"
                cursor.execute(insert_last, (self.face_detect_time.strftime("%H:%M:%S"), name))
                cursor.commit()

        query = """ SELECT cin, nom, prenom
FROM EMP
WHERE temp_arrive IS NULL;
"""     
        cursor.execute(query)
        result = cursor.fetchall()
        
        self.listabsence.setRowCount(len(result))

        for row, data in enumerate(result):
            cin = data[0]
            nom = data[1]
            prenom = data[2]

            cin_item = QTableWidgetItem(cin)
            nom_item = QTableWidgetItem(nom)
            prenom_item = QTableWidgetItem(prenom)

            self.listabsence.setItem(row, 0, cin_item)
            self.listabsence.setItem(row, 1, nom_item)
            self.listabsence.setItem(row, 2, prenom_item)

    def close(self):
        from close import Ui_quitter
        self.Close = QtWidgets.QWidget()
        self.work = Ui_quitter()
        self.work.setupUi(self.Close)
        self.Close.show()
        def hide():
            self.work.logOut()
            camera.hide()
        self.work.oui.clicked.connect(hide)    
        def close():
            self.Close.hide()
        self.work.non.clicked.connect(close)

    def open_profile(self, name, pic_path):
        from profil import Ui_profile
        self.profil = QtWidgets.QMainWindow()
        self.work = Ui_profile()
        self.work.setupUi(self.profil)
        self.work.set_user_info(name, pic_path)
        self.profil.show()
        def close():
            self.profil.hide()
        self.work.close.clicked.connect(close)
        self.cap.release()

    def open_emp(self, name, pic_path):
        from EMP import Ui_EMP
        self.work_window = QtWidgets.QMainWindow()
        self.ui = Ui_EMP()
        self.ui.setupUi(self.work_window)
        self.ui.set_user_info(name, pic_path)
        self.work_window.show()
        self.widget.hide()
        self.cap.release()

    def open_rappot(self, name, pic_path):
        from rapport import Ui_Rapport
        self.work_window = QtWidgets.QMainWindow()
        self.ui = Ui_Rapport()
        self.ui.setupUi(self.work_window)
        self.ui.set_user_info(name, pic_path)
        self.work_window.show()
        self.widget.hide() 
        self.cap.release()  

    def open_Dash(self, name, pic_path):
        from dashboard import Ui_dash
        self.work_window = QtWidgets.QMainWindow()
        self.ui = Ui_dash()
        self.ui.setupUi(self.work_window)
        self.ui.set_user_info(name, pic_path)
        self.work_window.show()
        self.widget.hide() 
        self.cap.release()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    camera = QtWidgets.QWidget()
    ui = Ui_camera()
    ui.setupUi(camera)
    camera.show()
    sys.exit(app.exec_())
