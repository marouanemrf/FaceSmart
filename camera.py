from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from rapport import Ui_rapport

class Ui_camera(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 575)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)   
        self.center = QtWidgets.QWidget(MainWindow)
        self.center.setObjectName("center")
        self.widget = QtWidgets.QWidget(self.center)
        self.widget.setGeometry(QtCore.QRect(30, 20, 802, 501))
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
        self.dashboard.setObjectName("dashboard")
        self.dashboard.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\dashboard.png'))
        self.employee = QtWidgets.QPushButton(self.widget)
        self.employee.setGeometry(QtCore.QRect(0, 187, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.employee.setFont(font)
        self.employee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.employee.setStyleSheet("QPushButton#employee{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#employee:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#employee:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")
        self.employee.setObjectName("employee")
        self.employee.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\group.png'))
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
        self.rapport.setObjectName("rapport")
        self.rapport.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\rapport.png'))
        self.chat = QtWidgets.QPushButton(self.widget)
        self.chat.setGeometry(QtCore.QRect(0, 260, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chat.setFont(font)
        self.chat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chat.setStyleSheet("QPushButton#chat{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#chat:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#chat:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")
        self.chat.setObjectName("chat")
        self.chat.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\messenger.png'))
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
        self.terminer.setObjectName("terminer")
        self.terminer.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\exit.png'))
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
        self.reduit = QtWidgets.QPushButton(self.widget)
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
        def reduir():
            MainWindow.showMinimized()
        self.reduit.clicked.connect(reduir)    
        self.cam = QtWidgets.QPushButton(self.widget)
        self.cam.setGeometry(QtCore.QRect(0, 300, 191, 35))
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
        self.profil.setObjectName("profil")
        self.profil.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\user.png'))
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
        self.cam_wdgt = QtWidgets.QWidget(self.widget)
        self.cam_wdgt.setGeometry(QtCore.QRect(200, 80, 571, 401))
        self.cam_wdgt.setObjectName("cam_wdgt")
        self.stat = QtWidgets.QLabel(self.cam_wdgt)
        self.stat.setGeometry(QtCore.QRect(10, 10, 151, 151))
        self.stat.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius: 70px;")
        self.stat.setText("")
        self.stat.setObjectName("stat")
        self.lisetofstat = QtWidgets.QWidget(self.cam_wdgt)
        self.lisetofstat.setGeometry(QtCore.QRect(-20, 180, 191, 91))
        self.lisetofstat.setObjectName("lisetofstat")
        self.label_4 = QtWidgets.QLabel(self.lisetofstat)
        self.label_4.setGeometry(QtCore.QRect(50, 7, 191, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.lisetofstat)
        self.label_5.setGeometry(QtCore.QRect(50, 34, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.lisetofstat)
        self.label_2.setGeometry(QtCore.QRect(50, 64, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.lisetofstat)
        self.label_6.setGeometry(QtCore.QRect(28, 10, 16, 16))
        self.label_6.setStyleSheet("   background-color: rgb(255, 60, 63);\n"
"    border-radius: 5px;\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.lisetofstat)
        self.label_7.setGeometry(QtCore.QRect(28, 66, 16, 16))
        self.label_7.setStyleSheet("   background-color:rgb(0, 170, 0);\n"
"    border-radius: 5px;\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.lisetofstat)
        self.label_8.setGeometry(QtCore.QRect(28, 37, 16, 16))
        self.label_8.setStyleSheet("   background-color:rgb(120, 0, 0);\n"
"    border-radius: 5px;\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.lbl = QtWidgets.QLabel(self.cam_wdgt)
        self.lbl.setGeometry(QtCore.QRect(350, 160, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setObjectName("lbl")
        self.listEMP = QtWidgets.QListWidget(self.cam_wdgt)
        self.listEMP.setGeometry(QtCore.QRect(300, 210, 261, 171))
        self.listEMP.setStyleSheet("    QListWidget {\n"
"        background-color: rgb(207, 201, 201);\n"
"        border-radius: 8px;\n"
"    }\n"
"    \n"
"    QListWidget::item {\n"
"        background-color: #D9D9D9;\n"
"        border-radius: 5px; \n"
"        padding: 5px; \n"
"        margin-bottom: 2px; \n"
"    }\n"
"    \n"
"    QListWidget::item:selected {\n"
"        background-color: #A5A5BD; \n"
"        color: white; \n"
"    }")
        self.listEMP.setObjectName("listEMP")
        self.cam_proj = QtWidgets.QLabel(self.cam_wdgt)
        self.cam_proj.setGeometry(QtCore.QRect(310, 20, 231, 131))
        self.cam_proj.setStyleSheet("border-radius: 6px;\n"
"background-color: rgb(170, 170, 127)")
        self.cam_proj.setText("")
        self.cam_proj.setObjectName("cam_proj")
        self.Vdo = QtWidgets.QPushButton(self.cam_wdgt)
        self.Vdo.setGeometry(QtCore.QRect(518, 127, 20, 20))
        self.Vdo.setStyleSheet("background-color:none;")
        self.Vdo.setText("")
        self.Vdo.setObjectName("Vdo")
        self.bane_persson = QtWidgets.QPushButton(self.cam_wdgt)
        self.bane_persson.clicked.connect(self.open_ban)
        self.bane_persson.setGeometry(QtCore.QRect(30, 330, 121, 41))
        self.bane_persson.setStyleSheet("QPushButton{\n"
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
        self.bane_persson.setObjectName("bane_persson")
        self.lbl2 = QtWidgets.QLabel(self.cam_wdgt)
        self.lbl2.setGeometry(QtCore.QRect(20, 300, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl2.setFont(font)
        self.lbl2.setObjectName("lbl2")
        MainWindow.setCentralWidget(self.center)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.widget.mousePressEvent = self.mouseclick
        self.widget.mouseMoveEvent = self.mousemove

        self.rapport.clicked.connect(self.open_rapport)

    def open_rapport(self):
        from rapport import Ui_rapport
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_rapport()
        self.work.setupUi(self.work_window)
        self.work_window.show()
        MainWindow.hide()

    def mouseclick(self, event):
        if event.button() == Qt.LeftButton:
            self.mouseclick = event.globalPos()
            self.mousemove = event.globalPos() - MainWindow.pos()
    
    def mousemove(self, event):
        if event.buttons() == Qt.LeftButton:
                position = event.globalPos()
                diff = position - self.mouseclick
                MainWindow.move(diff)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dashboard.setText(_translate("MainWindow", "Tableau de bord"))
        self.employee.setText(_translate("MainWindow", "Employée           "))
        self.rapport.setText(_translate("MainWindow", "Rapport               "))
        self.chat.setText(_translate("MainWindow", "Chat                     "))
        self.terminer.setText(_translate("MainWindow", "Quitter                 "))
        self.label.setText(_translate("MainWindow", "Face smart project"))
        self.recherche.setPlaceholderText(_translate("MainWindow", "Rechercher ici ..."))
        self.userName.setText(_translate("MainWindow", "user name"))
        self.cam.setText(_translate("MainWindow", "Camera               "))
        self.themr.setText(_translate("MainWindow", "Théme                 "))
        self.profil.setText(_translate("MainWindow", "Profil                    "))
        self.label_4.setText(_translate("MainWindow", "Employée Non Performer"))
        self.label_5.setText(_translate("MainWindow", "Personne Banné"))
        self.label_2.setText(_translate("MainWindow", "Employée Performer"))
        self.lbl.setText(_translate("MainWindow", "Liste Des Employées Absents"))
        self.bane_persson.setText(_translate("MainWindow", "Ajouter"))
        self.lbl2.setText(_translate("MainWindow", "Pour Banné Un Perssone"))

    def open_ban(self):
         from banée import Ui_Form
         self.work_window = QtWidgets.QMainWindow()
         self.work = Ui_Form()
         self.work.setupUi(self.work_window)
         self.work_window.show()
         def hide():
             self.work_window.hide()
         self.work.close.clicked.connect(hide)
         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_camera()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
