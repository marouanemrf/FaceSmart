from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection


class Ui_rapp(object):
    def setupUi(self, rapp):
        rapp.setObjectName("rapp")
        rapp.resize(702, 557)
        rapp.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        rapp.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.rapp = QtWidgets.QWidget(rapp)
        self.rapp.setGeometry(QtCore.QRect(100, 60, 421, 381))
        self.rapp.setStyleSheet("width: 190px;\n"
"height: 254px;\n"
"border-radius: 20px;\n"
"color:black;\n"
"background: #e0e0e0;\n"
"box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;\n"
"border: 2px solid rgba(224, 224, 224, 0.5); \n"
"\n"
"")
        self.rapp.setObjectName("rapp")
        self.ajoutRapp_6 = QtWidgets.QPushButton(self.rapp)
        self.ajoutRapp_6.setGeometry(QtCore.QRect(130, 320, 171, 35))
        self.ajoutRapp_6.setStyleSheet("QPushButton{\n"
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
        self.ajoutRapp_6.setObjectName("ajoutRapp_6")
        self.close_5 = QtWidgets.QPushButton(self.rapp)
        self.close_5.setGeometry(QtCore.QRect(390, 10, 13, 13))
        self.close_5.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 60, 63);\n"
"    border-radius: 6px;\n"
"    border: none; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(255, 90, 93);\n"
"}")
        self.close_5.setText("")
        self.close_5.setObjectName("close_5")
        def reduit():
            rapp.showMinimized()
        self.reduit_5 = QtWidgets.QPushButton(self.rapp)
        self.reduit_5.clicked.connect(reduit)
        self.reduit_5.setGeometry(QtCore.QRect(373, 10, 13, 13))
        self.reduit_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(84, 255, 90);\n"
"}")
        self.reduit_5.setText("")
        self.reduit_5.setObjectName("reduit_5")
        self.NomG_5 = QtWidgets.QLineEdit(self.rapp)
        self.NomG_5.setGeometry(QtCore.QRect(40, 49, 351, 21))
        self.NomG_5.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:grey;\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.NomG_5.setText("")
        self.NomG_5.setObjectName("NomG_5")
        self.comment_5 = QtWidgets.QTextEdit(self.rapp)
        self.comment_5.setGeometry(QtCore.QRect(40, 150, 351, 81))
        self.comment_5.setStyleSheet("background-color:#e0e0e0; \n"
"border:2px solid rgba(46,82,101,200);\n"
"color:grey;\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.comment_5.setObjectName("comment_5")
        self.label_5 = QtWidgets.QLabel(self.rapp)
        self.label_5.setGeometry(QtCore.QRect(50, 260, 111, 31))
        self.label_5.setStyleSheet("border-radius: 5px;\n"
"font: 81 6pt \"Rockwell Extra Bold\";\n"
"background-color: rgb(141, 141, 141);\n"
"color:black;\n"
"border:none;\n"
"font-weight: bold;\n"
"text-align: center;\n"
"")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.rapp)
        self.comboBox.setGeometry(QtCore.QRect(40, 110, 351, 22))
        self.comboBox.setStyleSheet("border-bottom:2px solid rgba(46,82,101,200);")
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.rapp)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 71, 20))
        self.label_6.setStyleSheet("color: rgb(143, 143, 143);")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(rapp)
        QtCore.QMetaObject.connectSlotsByName(rapp)
        self.selected_fil_path = None

        self.select =  self.proj_select()
        self.label_5.mousePressEvent = self.add_rapp_libel

        self.ajoutRapp_6.clicked.connect(self.ajouter)


    def add_rapp_libel(self, event):
        file_path, _ = QFileDialog.getOpenFileName(self.label_5, "", "", "Fichiers PDF (*.pdf);;Fichiers Word (*.docx);;Fichiers TXT (*.txt);;Fichiers PowerPoint (*.pptx)")
        if file_path:
            file_extension = file_path.split(".")[-1].lower()
            if file_extension in ["pdf", "docx", "txt", "pptx"]:
                print("Chemin du fichier sélectionné :", file_path)
                self.label_5.setStyleSheet("color: green;")
            else:
                print("Format de fichier non pris en charge.")

    def retranslateUi(self, rapp):
        _translate = QtCore.QCoreApplication.translate
        rapp.setWindowTitle(_translate("rapp", "rapp"))
        self.ajoutRapp_6.setText(_translate("rapp", "Ajouter"))
        self.NomG_5.setPlaceholderText(_translate("rapp", "Nom de Gestionnaire"))
        self.comment_5.setHtml(_translate("rapp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.comment_5.setPlaceholderText(_translate("rapp", "Ajouter Un Commentaire"))
        self.label_5.setText(_translate("rapp", "                  Rapport"))
        self.label_6.setText(_translate("rapp", "Nom Projet"))

    def ajouter(self):
        conn = connection.connection
        cursor = conn.cursor()
        rapp = self.NomG_5.text()
        titre_proj = self.comboBox.currentText()
        descreption = self.comment_5.toPlainText()
        rapp_fil = self.selected_fil_path 


        query_select = "SELECT id FROM Projet WHERE Nom = ?"
        cursor.execute(query_select, (titre_proj, ))
        row = cursor.fetchone()

        if row is not None:
            rapp_id = row[0]  

        query_insert = """INSERT INTO rapport (NomG, id_Proj, comment, Rapport) 
                          VALUES (?, ?, ?, ?);
                       """
        try:
            cursor.execute(query_insert, (rapp, rapp_id, descreption, rapp_fil))
            conn.commit()
        except Exception as e:
            print("erreur: ", e)
        finally:
            self.rapp.close()           

    def proj_select(self):
        conn = connection.connection
        cursor = conn.cursor()
        
        query = """
    SELECT Nom 
    FROM projet 
    WHERE dateFin > getdate();
"""
        cursor.execute(query)
        titles = cursor.fetchall()

        for title in titles:
            self.comboBox.addItem(title[0])   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rapp = QtWidgets.QWidget()
    ui = Ui_rapp()
    ui.setupUi(rapp)
    rapp.show()
    sys.exit(app.exec_())
