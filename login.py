import connection
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import os
import glob
import face_recognition
import numpy as np
import time

class Ui_logIn(object):
    
    def setupUi(self, LogiInwindow):
        self.LogiInwindow = LogiInwindow
        LogiInwindow.setObjectName("LogiInwindow")
        LogiInwindow.resize(783, 600)
        LogiInwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LogiInwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        LogiInwindow.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(LogiInwindow)
        self.centralwidget.setStyleSheet("border-radius: 7px;")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 40, 671, 391))
        self.widget.setObjectName("widget")
        self.image = QtWidgets.QLabel(self.widget)
        self.image.setGeometry(QtCore.QRect(310, -150, 411, 561))
        self.image.setStyleSheet("background-image: ;")
        self.image.setText("")
        self.image.setObjectName("image")
        self.log_int = QtWidgets.QLabel(self.widget)
        self.log_int.setGeometry(QtCore.QRect(0, 0, 671, 391))
        self.log_int.setStyleSheet("background-color: #DED9D9;")
        self.log_int.setText("")
        self.log_int.setObjectName("log_int")
        self.login_word = QtWidgets.QLabel(self.widget)
        self.login_word.setGeometry(QtCore.QRect(90, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.login_word.setFont(font)
        self.login_word.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.login_word.setAutoFillBackground(False)
        self.login_word.setStyleSheet("font-size: 36px; \n"
" color: #333; \n"
" text-shadow: 5px 5px 4px rgba(0, 0, 0, 0.5);")
        self.login_word.setScaledContents(False)
        self.login_word.setWordWrap(False)
        self.login_word.setObjectName("login_word")
        self.user_name = QtWidgets.QLineEdit(self.widget)
        self.user_name.setGeometry(QtCore.QRect(60, 159, 201, 31))
        self.user_name.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.user_name.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.user_name.setObjectName("user_name")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(62, 229, 200, 30))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.password.setFont(font)
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"    \n"
"")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setGeometry(QtCore.QRect(80, 300, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("QPushButton#login_btn {\n"
"    color: white;\n"
"    text-shadow: 0 1px 0 rgba(0, 0, 0, 0.4); \n"
"    background: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0 #89E5FF, stop: 1 #A5A5BD);\n"
"    border: 0; \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#login_btn:hover {\n"
"    text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9); \n"
"    background: qradialgradient(cx: 1.5, cy: 0.5, radius: 1.5, fx: 1.5, fy: 0.5, stop: 0.5 #A5A5BD, stop: 1.5 #8838ff);\n"
"}\n"
"\n"
"QPushButton#login_btn:pressed { \n"
"    background: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0 #3c4fe0, stop: 1 #5468FF); \n"
"}\n"
"rgb(136, 56, 255)")
        self.login_btn.setObjectName("login_btn")
        self.came = QtWidgets.QPushButton(self.widget)
        self.came.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.came.setStyleSheet("background-color: none;")
        self.came.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\camera.png'))
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setGeometry(QtCore.QRect(60, 140, 61, 16))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_password = QtWidgets.QLabel(self.widget)
        self.label_password.setGeometry(QtCore.QRect(60, 210, 47, 13))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 100, 111, 16))
        self.label.setStyleSheet("color: rgb(99, 99, 100);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(300, 0, 371, 401))
        self.label_2.setStyleSheet("\n"
"background-image: url(:/e_s image_log.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.close_btn = QtWidgets.QPushButton(self.widget)
        self.close_btn.setGeometry(QtCore.QRect(655, 5, 10, 10))
        self.close_btn.setStyleSheet("QPushButton#close_btn {\n"
"    background-color: rgb(255, 60, 63);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#close_btn:hover {\n"
"    background-color: rgb(255, 90, 93);\n"
"}\n"
"")
        self.close_btn.setText("")
        self.close_btn.clicked.connect(exit)
        self.close_btn.setObjectName("close_btn")
        self.rduit_btn = QtWidgets.QPushButton(self.widget)
        self.rduit_btn.setGeometry(QtCore.QRect(640, 5, 10, 10))
        self.rduit_btn.setStyleSheet("QPushButton#rduit_btn{\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton#rduit_btn:hover{\n"
"    background-color: rgb(84, 255, 90);\n"
"}")
        self.rduit_btn.setText("")
        def reduire():
            LogiInwindow.showMinimized()
        
        self.rduit_btn.clicked.connect(reduire)
        self.rduit_btn.setObjectName("rduit_btn")
        LogiInwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogiInwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName("menubar")
        LogiInwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogiInwindow)
        self.statusbar.setObjectName("statusbar")
        LogiInwindow.setStatusBar(self.statusbar)

        self.retranslateUi(LogiInwindow)
        QtCore.QMetaObject.connectSlotsByName(LogiInwindow)

        self.known_faces = []
        self.known_names = []

        self.registered_faces = 'admin/'

        for name in os.listdir(self.registered_faces):
            images_mask = os.path.join(self.registered_faces, name, '*.jpg')
            images_paths = glob.glob(images_mask)
            for image_path in images_paths:
                encoding = self.get_encoding(image_path)
                if encoding is not None:
                    self.known_faces.append(encoding)
                    self.known_names.append(name)
        
        self.came.clicked.connect(self.login_face)
        self.login_btn.clicked.connect(self.login)    
        
    def get_encoding(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            return face_encodings[0]
        return None

    def retranslateUi(self, LogiInwindow):
        _translate = QtCore.QCoreApplication.translate
        LogiInwindow.setWindowTitle(_translate("LogiInwindow", "LogiInwindow"))
        self.image.setWhatsThis("<html><head/><body><p><img src=\":/Enterprise-architecture.png\"/></p></body></html>")
        self.login_word.setText(_translate("LogiInwindow", "LOG IN"))
        self.login_btn.setText(_translate("LogiInwindow", "LOGIN"))
        self.label_name.setText(_translate("LogiInwindow", "UserName"))
        self.label_password.setText(_translate("LogiInwindow", "Password"))
        self.label.setText(_translate("LogiInwindow", "Welcome to the team,"))

    def open(self, name, pic_path):
        from dashboard import Ui_dash 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_dash()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(name, pic_path)
        self.work_window.show()
        LogiInwindow.hide()

    def login(self):
        conn = connection.connection
        try:
                cursor = conn.cursor()

                nameuser = self.user_name.text()
                password = self.password.text()

                if not nameuser and not password:
                      self.erreur()
                
                query = "SELECT nom, photo FROM log_in WHERE nom = ? AND pass_word = ? ;"
                cursor.execute(query, (nameuser, password))
                result = cursor.fetchone()

                if result:
                   name = result[0]
                   pic_path = result[1]
                   self.open(name, pic_path)
                else:
                   self.erreur()
        except Exception as e:
            print("Erreur: ", e)
        finally:
                if cursor and not cursor.closed:
                   cursor.close()

    def login_face(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if not ret:
            return

        conn = connection.connection
        cursor = conn.cursor()

        try:
            timeout = 5
            start_time = time.time()
            while time.time() - start_time < timeout:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faces = face_recognition.face_locations(frame_rgb)
                encodings = face_recognition.face_encodings(frame_rgb, faces)

                encodings_np = np.array(encodings)

                if len(encodings_np) > 0:  
                    for encoding_np in encodings_np:
                        results = face_recognition.compare_faces(self.known_faces, encoding_np)
                        if True in results:
                            index = results.index(True)
                            name = self.known_names[index]

                            query = "SELECT nom, photo FROM log_in WHERE nom = ?;"
                            cursor.execute(query, (name,))
                            result = cursor.fetchone()

                            if result:
                                name = result[0]
                                pic_path = result[1]

                                self.open(name, pic_path)
                                cap.release()
                                return  
                            
            print("Délai de détection du visage atteint.")
        except Exception as e:
            print("Erreur: ", e)
        finally:
            if cursor and not cursor.closed:
                cursor.close()

    def erreur(self):
        from erreur import Ui_erreur
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_erreur()

        self.work.setupUi(self.work_window)
        self.work_window.show()
        
        def close():
             self.work_window.close()

        self.work.pushButton_2.clicked.connect(close)

        

import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogiInwindow = QtWidgets.QMainWindow()
    ui = Ui_logIn()
    ui.setupUi(LogiInwindow)
    LogiInwindow.show()
    sys.exit(app.exec_())