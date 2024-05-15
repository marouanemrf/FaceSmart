from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_quitter(object):
    def setupUi(self, quitter):
        quitter.setObjectName("quitter")
        quitter.resize(609, 465)
        self.qitter = QtWidgets.QWidget(quitter)
        quitter.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        quitter.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.qitter.setGeometry(QtCore.QRect(110, 120, 351, 171))
        self.qitter.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.483, radius:2, fx:0.568182, fy:0.585, stop:0.352273 rgba(253, 255, 244, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 10px;")
        self.qitter.setObjectName("qitter")
        self.question = QtWidgets.QLabel(self.qitter)
        self.question.setStyleSheet("background-color: none;")
        self.question.setGeometry(QtCore.QRect(70, 20, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.question.setFont(font)
        self.question.setObjectName("question")
        self.non = QtWidgets.QPushButton(self.qitter)
        self.non.setGeometry(QtCore.QRect(10, 100, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.non.setFont(font)
        self.non.setStyleSheet("QPushButton{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.483, radius:2, fx:0.568182, fy:0.585, stop:0.352273 rgba(253, 255, 244, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 170, 255);\n"
"}\n"
"\n"
"")
        self.non.setObjectName("non")
        self.oui = QtWidgets.QPushButton(self.qitter)
        self.oui.setGeometry(QtCore.QRect(190, 100, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.oui.setFont(font)
        self.oui.setStyleSheet("QPushButton{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.483, radius:2, fx:0.568182, fy:0.585, stop:0.352273 rgba(253, 255, 244, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(205, 170, 255);\n"
"}\n"
"\n"
"")
        self.oui.setObjectName("oui")

        self.retranslateUi(quitter)
        QtCore.QMetaObject.connectSlotsByName(quitter)

    def retranslateUi(self, quitter):
        _translate = QtCore.QCoreApplication.translate
        quitter.setWindowTitle(_translate("quitter", "Form"))
        self.question.setText(_translate("quitter", "Vous voulez vraiment quitter ??"))
        self.non.setText(_translate("quitter", "NON"))
        self.oui.setText(_translate("quitter", "OUI"))

    def logOut(self):
        from login import Ui_logIn

        self.logout = QtWidgets.QMainWindow()
        self.ui = Ui_logIn()
        self.close = Ui_quitter()
        self.ui.setupUi(self.logout)
        self.logout.show()
        quitter.hide()        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quitter = QtWidgets.QWidget()
    ui = Ui_quitter()
    ui.setupUi(quitter)
    quitter.show()
    sys.exit(app.exec_())
