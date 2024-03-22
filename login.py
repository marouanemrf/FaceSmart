from PyQt5 import QtCore, QtGui, QtWidgets
import connection

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 600)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.close_btn.setGeometry(QtCore.QRect(660, 0, 10, 10))
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
        self.rduit_btn.setGeometry(QtCore.QRect(645, 0, 10, 10))
        self.rduit_btn.setStyleSheet("QPushButton#rduit_btn{\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton#rduit_btn:hover{\n"
"    background-color: rgb(84, 255, 90);\n"
"}")
        self.rduit_btn.setText("")
        def reduire(self):
            MainWindow.showMinimized()
        
        self.rduit_btn.clicked.connect(reduire)
        self.rduit_btn.setObjectName("rduit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/Enterprise-architecture.png\"/></p></body></html>"))
        self.login_word.setText(_translate("MainWindow", "LOG IN"))
        self.login_btn.setText(_translate("MainWindow", "LOGIN"))
        self.label_name.setText(_translate("MainWindow", "UserName"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Welcome to the team,"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
