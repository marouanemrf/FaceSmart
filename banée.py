from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QColor, QPen, QBitmap
import connection


class Ui_banee(object):
    def setupUi(self, banee_personne):
        banee_personne.setObjectName("banee_personne")
        banee_personne.resize(464, 408)
        banee_personne.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        banee_personne.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.add_widget = QtWidgets.QWidget(banee_personne)
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
        self.PIc.mousePressEvent = self.select_pic
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
        self.close.clicked.connect(exit)
        self.close.setGeometry(QtCore.QRect(240, 10, 13, 13))
        self.close.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 60, 63);\n"
"    border-radius: 6px; border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(255, 90, 93);\n"
"}")
        self.close.setText("")
        self.close.setObjectName("close")
        def reduir():
            banee_personne.showMinimized()    
        self.reduit = QtWidgets.QPushButton(self.add_widget)
        self.reduit.clicked.connect(reduir)
        self.reduit.setGeometry(QtCore.QRect(220, 10, 13, 13))
        self.reduit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-radius: 6px; border: none;\n"
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

        self.retranslateUi(banee_personne)
        QtCore.QMetaObject.connectSlotsByName(banee_personne)

        self.ajouter.clicked.connect(self.bane)

        self.selcted_photo_path = ""

 
    def cercle(self, pixmap):
        diam = min(pixmap.width(), pixmap.height())
        circle = QPixmap(diam, diam)
        circle.fill(Qt.transparent)

        mask = QBitmap(diam, diam)
        mask.fill(Qt.white)

        paint = QPainter(mask)
        paint.setRenderHint(QPainter.Antialiasing, True)
        paint.setBrush(Qt.black)
        paint.drawEllipse(0, 0, diam, diam)
        paint.end()

        pixmap.setMask(mask)

        return pixmap



    def select_pic(self, event):
        if event.button() == Qt.LeftButton:
            file = QFileDialog()
            file.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff)")
            if file.exec_():
                try:
                    path = file.selectedFiles()[0]
                    self.selcted_photo_path = path
                    affiche = QPixmap(path)
                    circule = self.cercle(affiche.scaled(121, 121))
                    self.PIc.setPixmap(circule)
                    self.PIc.setStyleSheet("border-radius: 45px;")
                except Exception as error:
                    print("Error:",error)

    def bane(self):
         cin = self.cin.text()
         nom = self.Nom.text()
         cause = self.cause.text()
         photo = self.selcted_photo_path
         try:
             conn = connection.connection
             cursor = conn.cursor()
             query = """
INSERT INTO banee (cin, nom, cause, photo) VALUES (?, ?, ?, ?)
"""
             cursor.execute(query, (cin, nom, cause, photo))
             conn.commit()
         except Exception as error:
             print("error: ",error)
         finally:
             cursor.close()
             conn.close()
             self.add_widget.hide()

    def mouseclick(self, event):
        if event.button() == Qt.LeftButton:
            self.mouseclick = event.globalPos()
            self.mousemove = event.globalPos() - banee_personne.pos()
    
    def mousemove(self, event):
        if event.buttons() == Qt.LeftButton:
                position = event.globalPos()
                diff = position - self.mouseclick
                banee_personne.move(diff)
                
    def retranslateUi(self, banee_personne):
        _translate = QtCore.QCoreApplication.translate
        banee_personne.setWindowTitle(_translate("banee_personne", "banee_personne"))
        self.cin.setPlaceholderText(_translate("banee_personne", "Saisie CIN"))
        self.cause.setPlaceholderText(_translate("banee_personne", "Saisie Cause"))
        self.ajouter.setText(_translate("banee_personne", "Banée"))
        self.Nom.setPlaceholderText(_translate("banee_personne", "Saisie Nom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    banee_personne = QtWidgets.QWidget()
    ui = Ui_banee()
    ui.setupUi(banee_personne)
    banee_personne.show()
    sys.exit(app.exec_())
