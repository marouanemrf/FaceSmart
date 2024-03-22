
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import connection
class Ui_work(object):
    def setupUi(self, work):
        work.setObjectName("work")
        work.resize(767, 470)
        work.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        work.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(work)
        self.centralwidget.setObjectName("centralwidget")
        self.form = QtWidgets.QWidget(self.centralwidget)
        self.form.setGeometry(QtCore.QRect(20, 30, 811, 371))
        self.form.setObjectName("form")
        self.menu = QtWidgets.QLabel(self.form)
        self.menu.setGeometry(QtCore.QRect(0, 0, 161, 371))
        self.menu.setStyleSheet("background-color: rgb(165, 165, 189); border-radius: 0.3em;")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        self.label_2 = QtWidgets.QLabel(self.form)
        self.label_2.setGeometry(QtCore.QRect(60, 0, 101, 22))
        self.label_2.setStyleSheet("color:rgb(136, 117, 117);")
        self.label_2.setObjectName("label_2")
        self.bord = QtWidgets.QPushButton(self.form)
        self.bord.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\bord.png'))
        self.bord.setGeometry(QtCore.QRect(0, 91, 161, 30))
        self.bord.setStyleSheet("QPushButton {\n"
"  width: 10em;\n"
"  height: 3.5em;\n"
"\n"
"  background-color:transparent ;\n"
"  color: black;\n"
"  border-radius: 0.3em;\n"
"  font-size: 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  \n"
"    background-color: rgb(226, 216, 255);\n"
"}\n"
"")
        self.bord.setObjectName("bord")
        self.chat = QtWidgets.QPushButton(self.form)
        self.chat.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\messenger.png'))
        self.chat.setGeometry(QtCore.QRect(0, 203, 161, 30))
        self.chat.setStyleSheet("QPushButton {\n"
"  width: 10em;\n"
"  height: 3.5em;\n"
"\n"
"  background-color:transparent ;\n"
"  color: black;\n"
"  border-radius: 0.3em;\n"
"  font-size: 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  \n"
"    background-color: rgb(226, 216, 255);\n"
"}\n"
"")
        self.chat.setObjectName("chat")
        self.raport = QtWidgets.QPushButton(self.form)
        self.raport.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\raport.png'))
        self.raport.setGeometry(QtCore.QRect(0, 147, 161, 30))
        self.raport.setStyleSheet("QPushButton {\n"
"  width: 10em;\n"
"  height: 3.5em;\n"
"\n"
"  background-color:transparent ;\n"
"  color: black;\n"
"  border-radius: 0.3em;\n"
"  font-size: 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  \n"
"    background-color: rgb(226, 216, 255);\n"
"}\n"
"")
        self.raport.setObjectName("raport")
        self.traveaux = QtWidgets.QPushButton(self.form)
        self.traveaux.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\work.png'))
        self.traveaux.setGeometry(QtCore.QRect(0, 175, 161, 30))
        self.traveaux.setStyleSheet("QPushButton {\n"
"  width: 10em;\n"
"  height: 3.5em;\n"
"\n"
"  background-color:transparent ;\n"
"  color: black;\n"
"  border-radius: 0.3em;\n"
"  font-size: 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  \n"
"    background-color: rgb(226, 216, 255);\n"
"}\n"
"\n"
"")
        self.traveaux.setObjectName("traveaux")
        self.end = QtWidgets.QPushButton(self.form)
        self.end.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\exit.png'))
        self.end.setGeometry(QtCore.QRect(0, 259, 161, 30))
        self.end.setStyleSheet("QPushButton {\n"
"  width: 10em;\n"
"  height: 3.5em;\n"
"\n"
"  background-color:transparent ;\n"
"  color: black;\n"
"  border-radius: 0.3em;\n"
"  font-size: 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  \n"
"    background-color: rgb(226, 216, 255);\n"
"}\n"
"")
        self.end.setObjectName("end")
        self.profil = QtWidgets.QPushButton(self.form)
        self.profil.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\user.png'))
        self.profil.setGeometry(QtCore.QRect(0, 231, 161, 30))
        self.profil.setStyleSheet("QPushButton {\n"
"  width: 10em;\n"
"  height: 3.5em;\n"
"\n"
"  background-color:transparent ;\n"
"  color: black;\n"
"  border-radius: 0.3em;\n"
"  font-size: 10px;\n"
"  font-weight: bold;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"  \n"
"    background-color: rgb(226, 216, 255);\n"
"}\n"
"")
        self.profil.setObjectName("profil")
        self.emp = QtWidgets.QPushButton(self.form)
        self.emp.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\employee.png'))
        self.emp.setGeometry(QtCore.QRect(0, 119, 161, 30))
        self.emp.setStyleSheet("QPushButton {\n"
        "  width: 10em;\n"
        "  height: 3.5em;\n"
        "\n"
        "  background-color:transparent ;\n"
        "  color: black;\n"
        "  border-radius: 0.3em;\n"
        "  font-size: 10px;\n"
        "  font-weight: bold;\n"
        "  cursor: pointer;\n"
        "}\n"
        "\n"
        "QPushButton::hover {\n"
        "  \n"
        "    background-color: rgb(226, 216, 255);\n"
        "}    \n"
        "\n"
        "")
        self.emp.setObjectName("emp")
        self.wight = QtWidgets.QLabel(self.form)
        self.wight.setGeometry(QtCore.QRect(160, 0, 651, 371))
        self.wight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wight.setText("")
        self.wight.setObjectName("wight")
        self.account = QtWidgets.QLabel(self.form)
        self.pic = QPixmap('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\user.png').scaled(50,50)
        self.account.setPixmap(self.pic)
        self.account.resize(50,50)
        self.account.move(695,2)
        work.setCentralWidget(self.centralwidget)

        self.accountName = QtWidgets.QLabel('USER NAME',self.form)
        self.accountName.move(694,52)

        self.search = QtWidgets.QLineEdit(self.form)
        self.search.setStyleSheet("""
        QLineEdit {                               
                max-width: 220px;
                padding: 0px 12px; 
                border-radius: 8px;
                border: 1px solid #000000;
                outline: none;
                box-shadow: 0px 0px 20px -18px;                  
        }
        """)
        self.search.setAlignment(QtCore.Qt.AlignCenter)  
        self.search.resize(650, 20)
        self.search.move(300, 7)
        
        self.searchBtn = QtWidgets.QPushButton(self.form)
        self.searchBtn.setStyleSheet("""
        QPushButton{ 
        border: none;
        }
        QPushButton:hover{
         border: #B3D9E4;                           
        }                                                         
""")
        self.searchBtn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\notification.png'))
        self.searchBtn.move(580,7)


        self.statusbar = QtWidgets.QStatusBar(work)
        self.statusbar.setObjectName("statusbar")
        work.setStatusBar(self.statusbar)

        self.retranslateUi(work)
        QtCore.QMetaObject.connectSlotsByName(work)

    def retranslateUi(self, work):
        _translate = QtCore.QCoreApplication.translate
        work.setWindowTitle(_translate("work", "MainWindow"))
        self.label_2.setText(_translate("work", "SmartFAceProject"))
        self.bord.setText(_translate("work", "Tableau de bord"))
        self.chat.setText(_translate("work", "Chat"))
        self.raport.setText(_translate("work", "Raports"))
        self.traveaux.setText(_translate("work", "Traveaux"))
        self.end.setText(_translate("work", "Términer"))
        self.profil.setText(_translate("work", "Profil"))
        self.emp.setText(_translate("work", "Employe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    work = QtWidgets.QMainWindow()
    ui = Ui_work()
    ui.setupUi(work)
    work.show()
    sys.exit(app.exec_())
