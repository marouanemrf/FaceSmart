from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection

class Ui_Rapport(object):
    def setupUi(self, Rapport):
        Rapport.setObjectName("Rapport")
        Rapport.resize(905, 575)
        Rapport.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Rapport.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center = QtWidgets.QWidget(Rapport)
        self.center.setObjectName("center")
        self.widget = QtWidgets.QWidget(self.center)
        self.widget.setGeometry(QtCore.QRect(40, 10, 802, 501))
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
        self.dashboard.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\dashboard.png'))
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
        self.rapport.setStyleSheet("\n"
"background-color:#D9D9D9;\n"
"border-radius: 0px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"\n"
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
        self.close_btn.clicked.connect(exit)
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
        def reduit():
            Rapport.showMinimized()
        self.reduit.clicked.connect(reduit)    
        self.cam = QtWidgets.QPushButton(self.widget)
        self.cam.setGeometry(QtCore.QRect(0, 260, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cam.setFont(font)
        self.cam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cam.setStyleSheet("QPushButton{\n"
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
        self.rapportwdgt = QtWidgets.QWidget(self.widget)
        self.rapportwdgt.setGeometry(QtCore.QRect(196, 80, 601, 411))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rapportwdgt.setFont(font)
        self.rapportwdgt.setObjectName("rapportwdgt")
        self.addraport = QtWidgets.QPushButton(self.rapportwdgt)
        self.addraport.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\add.png'))
        self.addraport.setGeometry(QtCore.QRect(494, 220, 90, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addraport.setFont(font)
        self.addraport.setStyleSheet("QPushButton{\n"
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
        self.addraport.setObjectName("addraport")
        self.addprojet = QtWidgets.QPushButton(self.rapportwdgt)
        self.addprojet.setGeometry(QtCore.QRect(494, 10, 90, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addprojet.setFont(font)
        self.addprojet.setStyleSheet("QPushButton{\n"
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
        self.addprojet.setObjectName("addprojet")
        self.addprojet.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\add.png'))
        self.label_2 = QtWidgets.QLabel(self.rapportwdgt)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.rapportwdgt)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listProjet = QtWidgets.QTableWidget(self.rapportwdgt)
        self.listProjet.setGeometry(QtCore.QRect(90, 50, 420, 131))
        self.listProjet.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: rgb(176, 111, 255); \n"
"}")
        self.listProjet.setObjectName("listProjet")
        self.listProjet.setColumnCount(4)
        self.listProjet.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listProjet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listProjet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listProjet.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listProjet.setHorizontalHeaderItem(3, item)
        self.lisrapport = QtWidgets.QTableWidget(self.rapportwdgt)
        self.lisrapport.setGeometry(QtCore.QRect(136, 260, 315, 131))
        self.lisrapport.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: rgb(176, 111, 255); \n"
"}")
        self.lisrapport.setObjectName("lisrapport")
        self.lisrapport.setColumnCount(3)
        self.lisrapport.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lisrapport.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lisrapport.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lisrapport.setHorizontalHeaderItem(2, item)
        Rapport.setCentralWidget(self.center)
        self.menubar = QtWidgets.QMenuBar(Rapport)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")
        Rapport.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Rapport)
        self.statusbar.setObjectName("statusbar")
        Rapport.setStatusBar(self.statusbar)

        self.retranslateUi(Rapport)
        QtCore.QMetaObject.connectSlotsByName(Rapport)

        self.name = None
        self.pic_path = None

        self.dashboard.clicked.connect(lambda: self.open_Dash(self.name, self.pic_path))
        self.employee.clicked.connect(lambda: self.open_emp(self.name, self.pic_path))
        self.cam.clicked.connect(lambda: self.open_camera(self.name, self.pic_path))
        self.terminer.clicked.connect(self.close)
        self.profil.clicked.connect(lambda: self.open_profile(self.name, self.pic_path))

        self.addprojet.clicked.connect(self.add_proj)
        self.addraport.clicked.connect(self.add_rap)

        self.afficher_proj()
        self.afficher_rapp()

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


    def retranslateUi(self, Rapport):
        _translate = QtCore.QCoreApplication.translate
        Rapport.setWindowTitle(_translate("Rapport", "Rapport"))
        self.dashboard.setText(_translate("Rapport", "Tableau de bord"))
        self.employee.setText(_translate("Rapport", "Employée           "))
        self.rapport.setText(_translate("Rapport", "Rapport               "))
        self.terminer.setText(_translate("Rapport", "Quitter                 "))
        self.label.setText(_translate("Rapport", "Face smart project"))
        self.recherche.setPlaceholderText(_translate("Rapport", "Rechercher ici ..."))
        self.userName.setText(_translate("Rapport", "user name"))
        self.cam.setText(_translate("Rapport", "Camera               "))
        self.themr.setText(_translate("Rapport", "Théme                 "))
        self.profil.setText(_translate("Rapport", "Profil                    "))
        self.addraport.setText(_translate("Rapport", "Rapport"))
        self.addprojet.setText(_translate("Rapport", "Projet"))
        self.label_2.setText(_translate("Rapport", "List du rapport"))
        self.label_3.setText(_translate("Rapport", "List du projet"))
        item = self.listProjet.horizontalHeaderItem(0)
        item.setText(_translate("Rapport", "Nom"))
        item = self.listProjet.horizontalHeaderItem(1)
        item.setText(_translate("Rapport", "Date début"))
        item = self.listProjet.horizontalHeaderItem(2)
        item.setText(_translate("Rapport", "Date fin"))
        item = self.listProjet.horizontalHeaderItem(3)
        item.setText(_translate("Rapport", "Action"))
        item = self.lisrapport.horizontalHeaderItem(0)
        item.setText(_translate("Rapport", "Gestionnaire"))
        item = self.lisrapport.horizontalHeaderItem(1)
        item.setText(_translate("Rapport", "Projet"))
        item = self.lisrapport.horizontalHeaderItem(2)
        item.setText(_translate("Rapport", "Action")) 

    def afficher_proj(self):
        conn = connection.connection
        cursor = conn.cursor()
        query = """
SELECT nom, datedebu, datefin FROM Projet WHERE datefin > getdate() ;
""" 
        cursor.execute(query)
        result = cursor.fetchall()

        self.listProjet.setRowCount(len(result))

        for row, data in enumerate(result):
            nom = data[0]
            datedebut = data[1]
            datefin = data[2]

            nom_item = QTableWidgetItem(str(nom))
            datedebut_item = QTableWidgetItem(str(datedebut))
            datefin_item = QTableWidgetItem(str(datefin))

            self.listProjet.setItem(row, 0, nom_item)
            self.listProjet.setItem(row, 1, datedebut_item)
            self.listProjet.setItem(row, 2, datefin_item)

            delete_button = QPushButton() 
            delete_button.setIcon(QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\bin.png'))
            delete_button.setStyleSheet("background-color: none; border: none;")
            delete_button.clicked.connect(self.delete_projet)

            self.listProjet.setCellWidget(row, 3, delete_button)

    def afficher_rapp(self):
        conn = connection.connection
        cursor = conn.cursor()

        query = """
        SELECT rapport.NomG, projet.nom AS nom
        FROM rapport
        INNER JOIN projet ON rapport.id_Proj = projet.id;
"""
        cursor.execute(query)
        result = cursor.fetchall()

        self.lisrapport.setRowCount(len(result))

        for row, data in enumerate(result):
            nom = data[0]
            projet = data[1]

            nom_item = QTableWidgetItem(str(nom))
            projet_item = QTableWidgetItem(str(projet))

            self.lisrapport.setItem(row, 0, nom_item)
            self.lisrapport.setItem(row, 1, projet_item)

            delete_button = QPushButton() 
            delete_button.setIcon(QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\bin.png'))
            delete_button.setStyleSheet("background-color: none; border: none;")
            delete_button.clicked.connect(self.delete_rapp)

            self.lisrapport.setCellWidget(row, 2, delete_button) 

    def delete_projet(self):
        try: 
             line = self.listProjet.currentRow()
             if line != -1:
                  nom_item = self.listProjet.item(line, 0)
                  print("nom: ", nom_item)
                  if nom_item is not None:
                       nom = nom_item.text()
                       print("nom: ", nom)
                       conn = connection.connection
                       cursor = conn.cursor()
                       query = "DELETE FROM projet WHERE Nom = ?;"
                       cursor.execute(query, (nom,))
                       conn.commit()
                       self.afficher_proj()

        except Exception as e:
            print("erreur: ", e)

    def delete_rapp(self):
        try: 
             line = self.lisrapport.currentRow()
             if line != -1:
                  nom_item = self.lisrapport.item(line, 0)

                  print("nom: ", nom_item)
                  if nom_item is not None:
                       nom = nom_item.text()
                       print("nom: ", nom)
                       conn = connection.connection
                       cursor = conn.cursor()
                       query = "DELETE FROM rapport WHERE NomG = ?;"
                       cursor.execute(query, (nom,))
                       conn.commit()
                       self.afficher_rapp()

        except Exception as e:
             print("erreur: ", e)

    def add_proj(self):
        from add_projet import Ui_add_Projet
        self.workSpace = QtWidgets.QWidget()
        self.work = Ui_add_Projet()
        self.work.setupUi(self.workSpace)
        self.workSpace.show()

        def close():
            self.workSpace.close()

        self.work.close.clicked.connect(close)      

    def add_rap(self):
        from add_rapp import Ui_rapp
        self.workSpace = QtWidgets.QWidget()
        self.work = Ui_rapp()
        self.work.setupUi(self.workSpace)
        self.workSpace.show()

        def close():
            self.workSpace.close()

        self.work.close_5.clicked.connect(close) 

    def close(self):
        from close import Ui_quitter
        self.Close = QtWidgets.QWidget()
        self.work = Ui_quitter()
        self.work.setupUi(self.Close)
        self.Close.show()
        def hide():
            self.work.logOut()
            Rapport.hide()
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

    def open_camera(self, name, pic_path):
        from camera import Ui_camera
        self.work_window = QtWidgets.QMainWindow()
        self.ui = Ui_camera()
        self.ui.setupUi(self.work_window)
        self.ui.set_user_info(name, pic_path)
        self.work_window.show()
        self.widget.hide()   

    def open_Dash(self, name, pic_path):
        from dashboard import Ui_dash
        self.work_window = QtWidgets.QMainWindow()
        self.ui = Ui_dash()
        self.ui.setupUi(self.work_window)
        self.ui.set_user_info(name, pic_path)
        self.work_window.show()
        self.widget.hide() 

    def open_emp(self, name, pic_path):
        from EMP import Ui_EMP
        self.work_window = QtWidgets.QMainWindow()
        self.ui = Ui_EMP()
        self.ui.setupUi(self.work_window)
        self.ui.set_user_info(name, pic_path)
        self.work_window.show()
        self.widget.hide() 
 

if __name__ == "__main__":
    import sys
    from EMP import Ui_EMP
    app = QtWidgets.QApplication(sys.argv)
    Rapport = QtWidgets.QMainWindow()
    ui = Ui_Rapport()
    ui.setupUi(Rapport)
    Rapport.show()
    sys.exit(app.exec_())