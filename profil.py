from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QColor, QPen, QBitmap
import connection

class Ui_profile(object):
    def setupUi(self, profile):
        profile.setObjectName("profile")
        profile.resize(675, 540)
        self.profil_wdgt = QtWidgets.QWidget(profile)
        profile.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        profile.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.profil_wdgt.setGeometry(QtCore.QRect(130, 110, 421, 311))
        self.profil_wdgt.setStyleSheet("width: 190px;\n"
"height: 254px;\n"
"border-radius: 20px;\n"
"background: #e0e0e0;\n"
"box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;\n"
"border: 2px solid rgba(224, 224, 224, 0.5); \n"
"\n"
"")
        self.profil_wdgt.setObjectName("profil_wdgt")
        self.PIc = QtWidgets.QLabel(self.profil_wdgt)
        self.PIc.setGeometry(QtCore.QRect(30, 20, 151, 151))
        self.PIc.setStyleSheet("background-color:  rgb(141, 141, 141);\n"
"border-radius: 75px;")
        self.PIc.setText("")
        self.PIc.setObjectName("PIc")
        self.email = QtWidgets.QLineEdit(self.profil_wdgt)
        self.email.setGeometry(QtCore.QRect(240, 120, 151, 20))
        self.email.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.profil_wdgt)
        self.password.setGeometry(QtCore.QRect(240, 200, 151, 20))
        self.password.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.password.setObjectName("password")
        self.ajouter = QtWidgets.QPushButton(self.profil_wdgt)
        self.ajouter.setGeometry(QtCore.QRect(130, 250, 171, 35))
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
        self.close = QtWidgets.QPushButton(self.profil_wdgt)
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
        self.reduit = QtWidgets.QPushButton(self.profil_wdgt)
        self.reduit.setGeometry(QtCore.QRect(370, 10, 13, 13))
        self.reduit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(84, 255, 90);\n"
"}")
        self.reduit.setText("")
        self.reduit.setObjectName("reduit")
        self.Nom = QtWidgets.QLineEdit(self.profil_wdgt)
        self.Nom.setGeometry(QtCore.QRect(240, 40, 151, 20))
        self.Nom.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.Nom.setObjectName("Nom")
        self.cin = QtWidgets.QLineEdit(self.profil_wdgt)
        self.cin.setGeometry(QtCore.QRect(30, 200, 151, 20))
        self.cin.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.cin.setObjectName("cin")
        self.tel = QtWidgets.QLineEdit(self.profil_wdgt)
        self.tel.setGeometry(QtCore.QRect(240, 160, 151, 20))
        self.tel.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.tel.setObjectName("tel")
        self.prenom = QtWidgets.QLineEdit(self.profil_wdgt)
        self.prenom.setGeometry(QtCore.QRect(240, 80, 151, 20))
        self.prenom.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.prenom.setObjectName("prenom")

        def reduit():
            profile.showMinimized()

        self.reduit.clicked.connect(reduit)
        self.ajouter.clicked.connect(self.update)
        
        self.retranslateUi(profile)
        QtCore.QMetaObject.connectSlotsByName(profile)

        self.name = None
        self.pic_path = None

        self.PIc.mousePressEvent = self.select_pic

    def set_user_info(self, name, pic_path):
        self.name = name
        self.pic_path = pic_path
        self.select_profile(self.name, self.pic_path)

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

    def retranslateUi(self, profile):
        _translate = QtCore.QCoreApplication.translate
        profile.setWindowTitle(_translate("profile", "Form"))
        self.email.setPlaceholderText(_translate("profile", "Saisie email"))
        self.password.setPlaceholderText(_translate("profile", "Saisie password"))
        self.ajouter.setText(_translate("profile", "Modifier"))
        self.Nom.setPlaceholderText(_translate("profile", "Saisie Nom"))
        self.cin.setPlaceholderText(_translate("profile", "Saisie CIN"))
        self.tel.setPlaceholderText(_translate("profile", "Saisie tel"))
        self.prenom.setPlaceholderText(_translate("profile", "Saisie Prenom"))

    def select_pic(self, event):
        if event.button() == Qt.LeftButton:
            file = QFileDialog()
            file.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff)")
            if file.exec_():
                try:
                    path = file.selectedFiles()[0]
                    self.pic_path = path
                    affiche = QPixmap(path)
                    circele = self.cercle(affiche.scaled(151, 151))
                    self.PIc.setPixmap(circele)
                    self.PIc.setStyleSheet("border-radius: 75px;")
                except Exception as error:
                    print("Erreur: ", error)

    def select_profile(self, name, pic_path):
        try:
            conn = connection.connection
            cursor = conn.cursor()
            query = "SELECT nom, prenom, photo, pass_word, cin, email, tel FROM log_in WHERE nom = ? AND photo = ?"
            cursor.execute(query, (name, pic_path))
            profil = cursor.fetchone()

            if profil:
                self.cin.setText(profil[4])
                self.Nom.setText(profil[0])
                self.prenom.setText(profil[1])
                self.email.setText(profil[5])
                self.tel.setText(profil[6])
                self.password.setText(profil[3])
                photo_path = profil[2]

                if photo_path:
                    affiche = QPixmap(photo_path)
                    circuler = self.cercle(affiche.scaled(151, 151))
                    self.PIc.setPixmap(circuler)
            else:
                print("rien!!!")
            cursor.close()
        except Exception as error:
            print("Erreur: ", error)
            self.profil_wdgt.close()

    def update(self):
        cin = self.cin.text()
        nom = self.Nom.text()
        prenom = self.prenom.text()
        email = self.email.text()
        tel = self.tel.text()
        password = self.password.text()
        photo_path = self.pic_path

        conn = connection.connection
        cursor = conn.cursor()
        query = "UPDATE log_in SET cin = ?, nom = ?, prenom = ?, email = ?, tel = ?, pass_word = ?, photo = ? WHERE nom = ? AND photo = ?"
        cursor.execute(query, (cin, nom, prenom, email, tel, password, photo_path, self.name, self.pic_path))
        conn.commit()
        cursor.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile = QtWidgets.QWidget()
    ui = Ui_profile()
    ui.setupUi(profile)
    profile.show()
    sys.exit(app.exec_())
