from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection

class RechercgeManager(QObject):
    rechercheChange = pyqtSignal(str)
    def __init__(self):
        super().__init__()
  
class Ui_dash(object):
    def __init__(self):
        super().__init__()
        self.recherche_manager = RechercgeManager()   

    def setupUi(self, Dash):
        Dash.setObjectName("Dash")
        Dash.resize(851, 548)
        Dash.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Dash.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Dash)
        self.widget.setGeometry(QtCore.QRect(20, 20, 802, 501))
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
        self.dashboard.setStyleSheet("\n"
"background-color:#D9D9D9;\n"
"border-radius: 0px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);")
        self.dashboard.setObjectName("dashboard")
        self.employee = QtWidgets.QPushButton(self.widget)
        self.employee.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\group.png'))
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
        self.employee.setObjectName("employee")
        self.rapport = QtWidgets.QPushButton(self.widget)
        self.rapport.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\rapport.png'))
        self.rapport.setGeometry(QtCore.QRect(0, 223, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rapport.setFont(font)
        self.rapport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rapport.setStyleSheet("QPushButton{\n"
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
"")

        self.rapport.setObjectName("rapport")
        self.terminer = QtWidgets.QPushButton(self.widget)
        self.terminer.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\exit.png'))
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
        self.notification_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\not.png'))   
        self.notification_btn.setGeometry(QtCore.QRect(620, 30, 21, 21))
        self.notification_btn.setStyleSheet("        QPushButton{ \n"
"        border: none;\n"
"        }\n"
"        QPushButton:hover{\n"
"         border: #B3D9E4;                           \n"
"        }  ")
        self.notification_btn.setText("")
        self.notification_btn.setObjectName("notification_btn")
        self.recherche_btn = QtWidgets.QPushButton(self.widget)
        self.recherche_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\glass.png'))
        self.recherche_btn.setGeometry(QtCore.QRect(550, 31, 15, 15))
        self.recherche_btn.setStyleSheet("        QPushButton{ \n"
"        border: none;\n"
"        }\n"
"        QPushButton:hover{\n"
"         border: #B3D9E4;                           \n"
"        }  ")
        self.recherche_btn.setText("")
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
        def reduit():
             Dash.showMinimized()
        self.reduit.clicked.connect(reduit)
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
        self.cam = QtWidgets.QPushButton(self.widget)
        self.cam.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\camera.png'))
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
        self.cam.setObjectName("cam")
        self.themr = QtWidgets.QPushButton(self.widget)
        self.themr.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\theme.png'))
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
        self.hide_btn.setObjectName("hide_btn")
        self.hide_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\menu.png'))
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(200, 90, 591, 381))
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 111, 91))
        self.label_2.setStyleSheet("background-color: rgb(215, 188, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 111, 91))
        self.label_3.setStyleSheet("background-color: rgb(215, 188, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 111, 91))
        self.label_4.setStyleSheet("background-color: rgb(215, 188, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(63, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: none;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(72, 160, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: none;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(70, 280, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: none;")
        self.label_7.setObjectName("label_7")
        self.nmb_emp = QtWidgets.QLabel(self.widget_2)
        self.nmb_emp.setGeometry(QtCore.QRect(86, 80, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nmb_emp.setFont(font)
        self.nmb_emp.setStyleSheet("background-color: none")
        self.nmb_emp.setObjectName("nmb_emp")
        self.nmb_prj = QtWidgets.QLabel(self.widget_2)
        self.nmb_prj.setGeometry(QtCore.QRect(84, 190, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nmb_prj.setFont(font)
        self.nmb_prj.setStyleSheet("background-color: none")
        self.nmb_prj.setObjectName("nmb_prj")
        self.nmb_rap = QtWidgets.QLabel(self.widget_2)
        self.nmb_rap.setGeometry(QtCore.QRect(85, 310, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nmb_rap.setFont(font)
        self.nmb_rap.setStyleSheet("background-color: none")
        self.nmb_rap.setObjectName("nmb_rap")
        self.listadmin = QtWidgets.QTableWidget(self.widget_2)
        self.listadmin.setGeometry(QtCore.QRect(260, 90, 320, 230))
        self.listadmin.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: rgb(176, 111, 255); \n"
"}")
        self.listadmin.setObjectName("listadmin")
        self.listadmin.setColumnCount(3)
        self.listadmin.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listadmin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listadmin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listadmin.setHorizontalHeaderItem(2, item)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(260, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dash)
        QtCore.QMetaObject.connectSlotsByName(Dash)

        self.recherche_btn.clicked.connect(self.rechercher)
        self.recherche_manager.rechercheChange.connect(self.rechercher)
        self.recherche.textChanged.connect(self.recherche_manager.rechercheChange.emit)
         
        self.employee.clicked.connect(lambda: self.open_emp(self.name, self.pic_path))
        self.rapport.clicked.connect(lambda: self.open_rappot(self.name, self.pic_path))
        self.cam.clicked.connect(lambda: self.open_camera(self.name, self.pic_path))
        self.profil.clicked.connect(lambda: self.open_profile(self.name, self.pic_path))
        self.terminer.clicked.connect(self.close)

        self.name = None
        self.pic_path = None

        self.admin()
        self.emp_count() 
        self.rapport_count()
        self.project_count()

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

    def retranslateUi(self, Dash):
        _translate = QtCore.QCoreApplication.translate
        Dash.setWindowTitle(_translate("Dash", "Dash"))
        self.dashboard.setText(_translate("Dash", "Tableau de bord"))
        self.employee.setText(_translate("Dash", "Employée           "))
        self.rapport.setText(_translate("Dash", "Rapport               "))
        self.terminer.setText(_translate("Dash", "Quitter                 "))
        self.label.setText(_translate("Dash", "Face smart project"))
        self.recherche.setPlaceholderText(_translate("Dash", "Rechercher ici ..."))
        self.userName.setText(_translate("Dash", "user name"))
        self.cam.setText(_translate("Dash", "Camera               "))
        self.themr.setText(_translate("Dash", "Théme                 "))
        self.profil.setText(_translate("Dash", "Profil                    "))
        self.label_5.setText(_translate("Dash", "Employée"))
        self.label_6.setText(_translate("Dash", "Projet"))
        self.label_7.setText(_translate("Dash", "Rapport"))
        self.nmb_emp.setText(_translate("Dash", "5"))
        self.nmb_prj.setText(_translate("Dash", "5"))
        self.nmb_rap.setText(_translate("Dash", "5"))
        item = self.listadmin.horizontalHeaderItem(0)
        item.setText(_translate("Dash", "CIN"))
        item = self.listadmin.horizontalHeaderItem(1)
        item.setText(_translate("Dash", "Prénom"))
        item = self.listadmin.horizontalHeaderItem(2)
        item.setText(_translate("Dash", "Nom"))
        self.label_8.setText(_translate("Dash", "List Admin"))

    def admin(self):
        conn = connection.connection
        cursor = conn.cursor()

        select = "select cin, nom, prenom from log_in"
        cursor.execute(select)
        results = cursor.fetchall()

        row_count = len(results)
        self.listadmin.setRowCount(row_count)

        for row_index, row_data in enumerate(results):
                for col_index, col_data in enumerate(row_data):
                        self.listadmin.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def emp_count(self):
        conn = connection.connection
        cursor = conn.cursor()

        emp = "select count(*) from EMP"
        cursor.execute(emp)
        result = cursor.fetchone()
        count = str(result[0]) if result else "0"  
        self.nmb_emp.setText(count)

    def project_count(self):
         conn = connection.connection
         cursor = conn.cursor()

         project = "select count(*) from Projet"
         cursor.execute(project)
         result = cursor.fetchone()
         count = str(result[0]) if result else "0"  
         self.nmb_prj.setText(count)

    def rapport_count(self):
        conn = connection.connection
        cursor = conn.cursor()

        rapport = "select count(*) from Rapport"
        cursor.execute(rapport)
        result = cursor.fetchone()
        count = str(result[0]) if result else "0"  
        self.nmb_rap.setText(count)

    def rechercher(self, text):
        conn = connection.connection
        cursor = conn.cursor()

        rechercher = self.recherche.text()

        if not rechercher:
                self.admin()

        query = "SELECT cin, nom, prenom from log_in where cin LIKE ? OR nom LIKE ? OR prenom LIKE ?"
        search_text = f"%{text}%"
        cursor.execute(query, (search_text, search_text, search_text))
        table = cursor.fetchall()
        
        self.listadmin.setRowCount(len(table))

    def close(self):
        from close import Ui_quitter
        self.Close = QtWidgets.QWidget()
        self.work = Ui_quitter()
        self.work.setupUi(self.Close)
        self.Close.show()
        def hide():
            self.work.logOut()
            Dash.hide()
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

    def open_rappot(self, name, pic_path):
        from rapport import Ui_Rapport
        self.work_window = QtWidgets.QMainWindow()
        self.ui = Ui_Rapport()
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
    app = QtWidgets.QApplication(sys.argv)
    Dash = QtWidgets.QWidget()
    ui = Ui_dash()
    ui.setupUi(Dash)
    Dash.show()
    sys.exit(app.exec_())
