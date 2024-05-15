import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
import connection


class Ui_add_Projet(object):
    def setupUi(self, add_Projet):
        add_Projet.setObjectName("add_Projet")
        add_Projet.resize(675, 540)
        add_Projet.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        add_Projet.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.add_widget = QtWidgets.QWidget(add_Projet)
        self.add_widget.setGeometry(QtCore.QRect(110, 90, 421, 371))
        self.add_widget.setStyleSheet("width: 190px;\n"
"height: 254px;\n"
"border-radius: 20px;\n"
"background: #e0e0e0;\n"
"box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;\n"
"border: 2px solid rgba(224, 224, 224, 0.5); \n"
"\n"
"")
        self.add_widget.setObjectName("add_widget")
        self.ajouter = QtWidgets.QPushButton(self.add_widget)
        self.ajouter.setGeometry(QtCore.QRect(130, 310, 171, 35))
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
        self.close.setGeometry(QtCore.QRect(390, 10, 13, 13))
        self.close.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 60, 63);\n"
"    border-radius: 6px;\n"
"    border: none; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(255, 90, 93);\n"
"}")
        self.close.setText("")
        self.close.setObjectName("close")
        self.reduit_btn = QtWidgets.QPushButton(self.add_widget)
        self.reduit_btn.setGeometry(QtCore.QRect(370, 10, 13, 13))
        self.reduit_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(84, 255, 90);\n"
"}")
        self.reduit_btn.setText("")
        self.reduit_btn.setObjectName("reduit")
        self.reduit_btn.clicked.connect(add_Projet.showMinimized)
        self.Nom = QtWidgets.QLineEdit(self.add_widget)
        self.Nom.setGeometry(QtCore.QRect(40, 49, 351, 21))
        self.Nom.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.Nom.setObjectName("Nom")
        self.description = QtWidgets.QTextEdit(self.add_widget)
        self.description.setGeometry(QtCore.QRect(40, 160, 351, 81))
        self.description.setStyleSheet("background-color:#e0e0e0; \n"
"border:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.description.setObjectName("description")
        self.datedebu = QtWidgets.QDateTimeEdit(self.add_widget)
        self.datedebu.setGeometry(QtCore.QRect(40, 120, 141, 22))
        self.datedebu.setStyleSheet("border:2px solid rgba(46,82,101,200);")
        self.datedebu.setObjectName("datedebu")
        self.datefin = QtWidgets.QDateTimeEdit(self.add_widget)
        self.datefin.setGeometry(QtCore.QRect(243, 120, 141, 22))
        self.datefin.setStyleSheet("border:2px solid rgba(46,82,101,200);")
        self.datefin.setObjectName("datefin")
        self.label = QtWidgets.QLabel(self.add_widget)
        self.label.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.label.setStyleSheet("color: rgb(122, 122, 122);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.add_widget)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 71, 16))
        self.label_2.setStyleSheet("color: rgb(122, 122, 122);")
        self.label_2.setObjectName("label_2")
        self.cahiercharge = QtWidgets.QPushButton(self.add_widget)
        self.cahiercharge.setGeometry(QtCore.QRect(50, 260, 161, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cahiercharge.setFont(font)
        self.cahiercharge.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(141, 141, 141);")
        self.cahiercharge.setObjectName("cahiercharge")

        self.retranslateUi(add_Projet)
        QtCore.QMetaObject.connectSlotsByName(add_Projet)

        self.ajouter.clicked.connect(self.add)

    def retranslateUi(self, add_Projet):
        _translate = QtCore.QCoreApplication.translate
        add_Projet.setWindowTitle(_translate("add_Projet", "Form"))
        self.ajouter.setText(_translate("add_Projet", "Ajouter"))
        self.Nom.setPlaceholderText(_translate("add_Projet", "Saisie Nom du Projet"))
        self.description.setPlaceholderText(_translate("add_Projet", "Description du projet"))
        self.label.setText(_translate("add_Projet", "Date Début"))
        self.label_2.setText(_translate("add_Projet", "Date Fin"))
        self.cahiercharge.setText(_translate("add_Projet", " Cahier de charge"))

        
        self.cahiercharge.mousePressEvent = self.add_projet_libel

    def add_projet_libel(self, event):
        file_path, _ = QFileDialog.getOpenFileName(self.add_widget, "Sélectionner un projet", "", "Fichiers PDF (*.pdf);;Fichiers Word (*.docx);;Fichiers TXT (*.txt);;Fichiers PowerPoint (*.pptx)")
        if file_path:
            file_extension = file_path.split(".")[-1].lower()
            if file_extension in ["pdf", "docx", "txt", "pptx"]:
                print("Chemin du fichier sélectionné :", file_path)
                self.cahiercharge.setStyleSheet("color: green;")
            else:
                print("Format de fichier non pris en charge.")


    def add(self):
        Nom = self.Nom.text()
        description = self.description.toPlainText()
        datedebu = self.datedebu.dateTime().toString(Qt.ISODate)
        datefin = self.datefin.dateTime().toString(Qt.ISODate)
        cahiercharge = self.cahiercharge.text()

        conn = connection.connection
        cursor = conn.cursor()

        query3 = """INSERT INTO Projet (Nom, description, datedebu, datefin, cahiercharge) 
VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query3, (Nom, description, datedebu, datefin, cahiercharge))
        conn.commit() 
        self.add_widget.close()



if __name__  == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    add_Projet = QtWidgets.QWidget()
    ui = Ui_add_Projet()
    ui.setupUi(add_Projet)
    add_Projet.show()
    sys.exit(app.exec_())
