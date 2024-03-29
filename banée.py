from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 408)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.add_widget = QtWidgets.QWidget(Form)
        self.add_widget.setGeometry(QtCore.QRect(90, 10, 271, 361))
        self.add_widget.setStyleSheet("width: 190px;\n"
"height: 254px;\n"
"border-radius: 20px;\n"
"background: #e0e0e0;\n"
"box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;\n"
"border: 2px solid rgba(224, 224, 224, 0.5); \n"
"\n"
"")
        self.add_widget.setObjectName("add_widget")
        self.PIc = QtWidgets.QLabel(self.add_widget)
        self.PIc.setGeometry(QtCore.QRect(70, 40, 121, 121))
        self.PIc.setStyleSheet("background-color:  rgb(141, 141, 141);\n"
"border-radius: 60px;")
        self.PIc.setText("")
        self.PIc.setObjectName("PIc")
        self.cin = QtWidgets.QLineEdit(self.add_widget)
        self.cin.setGeometry(QtCore.QRect(60, 180, 151, 20))
        self.cin.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.cin.setObjectName("cin")
        self.cause = QtWidgets.QLineEdit(self.add_widget)
        self.cause.setGeometry(QtCore.QRect(60, 260, 151, 20))
        self.cause.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.cause.setObjectName("cause")
        self.ajouter = QtWidgets.QPushButton(self.add_widget)
        self.ajouter.setGeometry(QtCore.QRect(50, 300, 171, 35))
        self.ajouter.setStyleSheet("QPushButton{\n"
"background-color:  rgb(141, 141, 141);\n"
"border:none;\n"
"color: white;\n"
"border-radius: 7px;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(180, 180, 180);\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"\n"
"\n"
"")
        self.ajouter.setObjectName("ajouter")
        self.close = QtWidgets.QPushButton(self.add_widget)
        self.close.setGeometry(QtCore.QRect(240, 10, 13, 13))
        self.close.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 60, 63);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(255, 90, 93);\n"
"}")
        self.close.setText("")
        self.close.setObjectName("close")
        self.reduit = QtWidgets.QPushButton(self.add_widget)
        self.reduit.setGeometry(QtCore.QRect(220, 10, 13, 13))
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
        self.Nom = QtWidgets.QLineEdit(self.add_widget)
        self.Nom.setGeometry(QtCore.QRect(60, 220, 151, 20))
        self.Nom.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.Nom.setObjectName("Nom")
        self.add_widget.mousePressEvent = self.mouseclick
        self.add_widget.mouseMoveEvent = self.mousemove

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        def reduir():
            Form.showMinimized()

        self.reduit.clicked.connect(reduir)

    def mouseclick(self, event):
        if event.button() == Qt.LeftButton:
            self.mouseclick = event.globalPos()
            self.mousemove = event.globalPos() - Form.pos()
    
    def mousemove(self, event):
        if event.buttons() == Qt.LeftButton:
                position = event.globalPos()
                diff = position - self.mouseclick
                Form.move(diff)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cin.setPlaceholderText(_translate("Form", "Saisie CIN"))
        self.cause.setPlaceholderText(_translate("Form", "Saisie Cause"))
        self.ajouter.setText(_translate("Form", "Banée"))
        self.Nom.setPlaceholderText(_translate("Form", "Saisie Nom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
