from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QColor, QPen, QBitmap
import connection

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 408)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.add_widget = QtWidgets.QWidget(Form)
        self.add_widget.setGeometry(QtCore.QRect(60, 60, 361, 301))
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
        self.PIc.setGeometry(QtCore.QRect(50, 40, 91, 91))
        self.PIc.setStyleSheet("background-color:  rgb(141, 141, 141);\n"
"border-radius: 45px;")
        self.PIc.setText("")
        self.PIc.setObjectName("PIc")
        self.prenom = QtWidgets.QLineEdit(self.add_widget)
        self.prenom.setGeometry(QtCore.QRect(200, 70, 141, 20))
        self.prenom.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.prenom.setObjectName("prenom")
        self.cin = QtWidgets.QLineEdit(self.add_widget)
        self.cin.setGeometry(QtCore.QRect(30, 160, 141, 20))
        self.cin.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.cin.setObjectName("cin")
        self.email = QtWidgets.QLineEdit(self.add_widget)
        self.email.setGeometry(QtCore.QRect(200, 100, 141, 20))
        self.email.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.email.setObjectName("email")
        self.nom = QtWidgets.QLineEdit(self.add_widget)
        self.nom.setGeometry(QtCore.QRect(200, 40, 141, 20))
        self.nom.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.nom.setText("")
        self.nom.setObjectName("nom")
        self.fonction = QtWidgets.QLineEdit(self.add_widget)
        self.fonction.setGeometry(QtCore.QRect(30, 190, 141, 20))
        self.fonction.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.fonction.setObjectName("fonction")
        self.tache = QtWidgets.QLineEdit(self.add_widget)
        self.tache.setGeometry(QtCore.QRect(200, 190, 141, 20))
        self.tache.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.tache.setObjectName("tache")
        self.group = QtWidgets.QLineEdit(self.add_widget)
        self.group.setGeometry(QtCore.QRect(200, 160, 141, 20))
        self.group.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.group.setObjectName("group")
        self.tel = QtWidgets.QLineEdit(self.add_widget)
        self.tel.setGeometry(QtCore.QRect(200, 130, 141, 20))
        self.tel.setStyleSheet("background-color:#e0e0e0; \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"padding: 2px 0 2px 2px;")
        self.tel.setObjectName("tel")
        self.ajouter = QtWidgets.QPushButton(self.add_widget)
        self.ajouter.setGeometry(QtCore.QRect(100, 240, 171, 35))
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
        self.close.setGeometry(QtCore.QRect(330, 10, 13, 13))
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
            Form.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.add_widget)
        self.reduit.clicked.connect(reduir)
        self.reduit.setGeometry(QtCore.QRect(310, 10, 13, 13))
        self.reduit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 0);\n"
"     border-radius: 6px; border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(84, 255, 90);\n"
"}")
        self.reduit.setText("")
        self.reduit.setObjectName("reduit")
        self.add_widget.mousePressEvent = self.mouseclick
        self.add_widget.mouseMoveEvent = self.mousemove

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.selected_photo_path = None
        self.ajouter.clicked.connect(self.update)    

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
                        self.selected_photo_path = path
                        affiche = QPixmap(path)
                        circule = self.cercle(affiche.scaled(91, 91))
                        self.PIc.setPixmap(circule)
                        self.PIc.setStyleSheet("border-radius: 45px;")
                   except Exception as error:
                        print("Erreur: ",error)     


        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.affiche(self.cin)
        Form.setWindowTitle(_translate("Form", "Form"))
        self.prenom.setPlaceholderText(_translate("Form", "Saisie Prénom"))
        self.cin.setPlaceholderText(_translate("Form", "Saisie CIN"))
        self.email.setPlaceholderText(_translate("Form", "Saisie Email"))
        self.nom.setPlaceholderText(_translate("Form", "Saisie Nom"))
        self.fonction.setPlaceholderText(_translate("Form", "Saisie Fonction"))
        self.tache.setPlaceholderText(_translate("Form", "Saisie Tache"))
        self.group.setPlaceholderText(_translate("Form", "Saisie Group"))
        self.tel.setPlaceholderText(_translate("Form", "Saisie Tel"))
        self.ajouter.setText(_translate("Form", "Modifier"))

    def affiche(self, cin):  
         try:    
                conn = connection.connection
                cursor = conn.cursor()

                query = "select cin, nom, prenom, email, tel, fonction, tache, groups, photo from EMP where cin = ? "  

                cursor.execute(query, (cin, ))
                result = cursor.fetchone()
                
                if result:
                        self.cin.setText(cin)
                        self.nom.setText(result[1])
                        self.prenom.setText(result[2])
                        self.email.setText(result[3])
                        self.tel.setText(result[4])
                        self.fonction.setText(result[5])
                        self.tache.setText(result[6])
                        self.group.setText(result[7])
                        photo_path = result[8]

                        if photo_path:
                             affiche = QPixmap(photo_path)
                             circuler = self.cercle(affiche.scaled(91, 91))
                             self.PIc.setPixmap(circuler)
                             self.PIc.setStyleSheet("border-radius: 45px;")
                             self.PIc.setScaledContents(True)

                cursor.close()        

         except Exception as error:
              print("Erreur: ", error)

    def update(self):
         try:
              cin = self.cin.text()
              nom = self.nom.text()
              prenom = self.prenom.text()
              email = self.email.text()
              tel = self.tel.text()
              fonction = self.fonction.text()
              tache = self.tache.text()
              group = self.group.text()
              photo = self.selected_photo_path
              
              conn = connection.connection
              cursor = conn.cursor()
              query = "update EMP set cin = ?, nom = ?, prenom = ?, email = ?, tel = ?, fonction = ?, tache = ?, groups = ?, photo = ? where cin = ?;"
              values = (cin, nom, prenom, email, tel, fonction, tache, group, photo)
              print("values: ", values)
              cursor.execute(query, (cin, nom, prenom, email, tel, fonction, tache, group, photo, cin))

              conn.commit()
              print("Update successful")
         except Exception as error:
              print("erreur: ",error)
         finally:
              cursor.close()
              conn.close()
              self.add_widget.hide()                
       
    def mouseclick(self, event):
        if event.button() == Qt.LeftButton:
                self.mouseClickPos = event.globalPos()
                self.mouseMovePos = Form.pos()

    def mousemove(self, event):
        if event.buttons() == Qt.LeftButton:
                diff = event.globalPos() - self.mouseClickPos
                Form.move(self.mouseMovePos + diff)    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
