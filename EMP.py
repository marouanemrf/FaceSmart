from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection

class RechercgeManager(QObject):
    rechercheChange = pyqtSignal(str)
    def __init__(self):
        super().__init__()
  
class Ui_EMP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recherche_manager = RechercgeManager()

    def setupUi(self, EMP):
        EMP.setObjectName("EMP")
        EMP.resize(905, 575)
        EMP.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        EMP.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center = QtWidgets.QWidget(EMP)
        self.center.setObjectName("center")
        self.widget = QtWidgets.QWidget(self.center)
        self.widget.setGeometry(QtCore.QRect(30, 10, 802, 501))
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
        self.employee.setStyleSheet("\n"
"\n"
"background-color:#D9D9D9;\n"
"border-radius: 0px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"\n"
"")
        self.employee.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\group.png'))        
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
        self.userName.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
                              "border:none;\n"
                              "font-weight: bold;")
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
        def reduir():
            EMP.showMinimized()
        self.reduit.clicked.connect(reduir)    
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
        self.EMPWidget = QtWidgets.QWidget(self.widget)
        self.EMPWidget.setGeometry(QtCore.QRect(194, 90, 605, 381))
        self.EMPWidget.setObjectName("EMPWidget")
        self.EMPTable = QtWidgets.QTableWidget(self.EMPWidget)
        self.EMPTable.setGeometry(QtCore.QRect(0, 80, 601, 301))
        self.EMPTable.setStyleSheet("QTableWidget {\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: rgb(176, 111, 255); \n"
"}\n"
"")
        self.EMPTable.setObjectName("EMPTable")
        self.EMPTable.setColumnCount(6)
        self.EMPTable.setRowCount(0)
        Cin = QtWidgets.QTableWidgetItem()
        self.EMPTable.setHorizontalHeaderItem(0, Cin)
        nom = QtWidgets.QTableWidgetItem()
        self.EMPTable.setHorizontalHeaderItem(1, nom)
        prenom = QtWidgets.QTableWidgetItem()
        self.EMPTable.setHorizontalHeaderItem(2, prenom)
        fonction = QtWidgets.QTableWidgetItem()
        self.EMPTable.setHorizontalHeaderItem(3, fonction)
        date = QtWidgets.QTableWidgetItem()
        self.EMPTable.setHorizontalHeaderItem(4, date)
        action = QtWidgets.QTableWidgetItem()
        self.EMPTable.setHorizontalHeaderItem(5, action)
        self.Ajouter = QtWidgets.QPushButton(self.EMPWidget)
        self.Ajouter.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\add.png'))
        self.Ajouter.setGeometry(QtCore.QRect(494, 30, 91, 23))
        self.Ajouter.setStyleSheet("QPushButton{\n"
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
        self.Ajouter.setObjectName("Ajouter")
        EMP.setCentralWidget(self.center)
        self.menubar = QtWidgets.QMenuBar(EMP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")
        EMP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EMP)
        self.statusbar.setObjectName("statusbar")
        EMP.setStatusBar(self.statusbar)

        self.retranslateUi(EMP)
        QtCore.QMetaObject.connectSlotsByName(EMP)

        self.Ajouter.clicked.connect(self.add_emp)
        self.recherche_btn.clicked.connect(self.rechercher)
        self.recherche_manager.rechercheChange.connect(self.rechercher)
        self.recherche.textChanged.connect(self.recherche_manager.rechercheChange.emit)

        self.name = None
        self.pic_path = None
        
        self.dashboard.clicked.connect(lambda: self.open_Dash(self.name, self.pic_path))
        self.rapport.clicked.connect(lambda: self.open_rappot(self.name, self.pic_path))
        self.cam.clicked.connect(lambda: self.open_camera(self.name, self.pic_path))
        self.terminer.clicked.connect(self.close)
        self.profil.clicked.connect(lambda: self.open_profile(self.name, self.pic_path))
        
        self.select_emp()

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

    def retranslateUi(self, EMP):
        _translate = QtCore.QCoreApplication.translate
        EMP.setWindowTitle(_translate("EMP", "EMP"))
        self.dashboard.setText(_translate("EMP", "Tableau de bord"))
        self.employee.setText(_translate("EMP", "Employée           "))
        self.rapport.setText(_translate("EMP", "Rapport               "))
        self.terminer.setText(_translate("EMP", "Quitter                 "))
        self.label.setText(_translate("EMP", "Face smart project"))
        self.recherche.setPlaceholderText(_translate("EMP", "Rechercher ici ..."))
        self.userName.setText(_translate("EMP", "user name"))
        self.cam.setText(_translate("EMP", "Camera               "))
        self.themr.setText(_translate("EMP", "Théme                 "))
        self.profil.setText(_translate("EMP", "Profil                    "))
        Cin = self.EMPTable.horizontalHeaderItem(0)
        Cin.setText(_translate("EMP", "CIN"))
        nom = self.EMPTable.horizontalHeaderItem(1)
        nom.setText(_translate("EMP", "NOM"))
        prenom = self.EMPTable.horizontalHeaderItem(2)
        prenom.setText(_translate("EMP", "PRENOM"))
        fonction = self.EMPTable.horizontalHeaderItem(3)
        fonction.setText(_translate("EMP", "FONCTION"))
        date = self.EMPTable.horizontalHeaderItem(4)
        date.setText(_translate("EMP", "DATE DEBUT"))
        action = self.EMPTable.horizontalHeaderItem(5)
        action.setText(_translate("EMP", "ACTION"))
        self.Ajouter.setText(_translate("EMP", "Ajouter"))

    def add_emp(self):
        from add_emp import Ui_add
        self.work_window = QtWidgets.QWidget()
        self.ui = Ui_add()
        self.ui.setupUi(self.work_window)
        self.work_window.show()  
        self.select_emp()  
        def close():
            self.work_window.hide()
        self.ui.close.clicked.connect(close) 
        
    def select_emp(self):
        conn =  connection.connection
        cursor = conn.cursor()
        query = """
select cin, nom, prenom, fonction, date_debut from EMP;
"""     
        cursor.execute(query)
        table = cursor.fetchall()
        
        self.EMPTable.setRowCount(len(table))

        for row_num, line in enumerate(table):
            for col_num, data in enumerate(line):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.EMPTable.setItem(row_num, col_num, item)

            widget = QtWidgets.QWidget()
            widget.setStyleSheet("background-color: none;")
            layout = QtWidgets.QGridLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)

            view = QtWidgets.QPushButton()
            view.setStyleSheet("background-color: none; border: none;")
            view.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\view.png'))
            view.clicked.connect(self.open_view)

            delete = QtWidgets.QPushButton() 
            delete.setStyleSheet("background-color: none; border: none;")
            delete.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\bin.png'))
            delete.clicked.connect(self.delete_emp)

            layout.addWidget(view, 0, 0, alignment=QtCore.Qt.AlignCenter)
            layout.addWidget(delete, 0, 1, alignment=QtCore.Qt.AlignCenter)
            self.EMPTable.setCellWidget(row_num, 5, widget)

    def open_view(self):
        from Udt_EMP import Ui_Form

        self.workSpace = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.workSpace)
        self.workSpace.show()

        def hide():
            self.workSpace.hide()

        self.ui.close.clicked.connect(hide)

        line = self.EMPTable.currentRow()
        cin_item = self.EMPTable.item(line, 0)
        print("cin_item: ", cin_item)

        if cin_item is not None:
            
            cin = cin_item.text()
            print("cin: ", cin)
            self.ui.affiche(cin)
            self.select_emp()
        
    def delete_emp(self): 
        try:
            line = self.EMPTable.currentRow()
            if line != -1:
                cin_item = self.EMPTable.item(line, 0)
                print("cin: ", cin_item)
                if cin_item is not None:  
                    cin = cin_item.text()
                    print(cin)
                    conn = connection.connection
                    cursor = conn.cursor()
                    query = "DELETE FROM EMP WHERE cin = ?;"
                    cursor.execute(query, (cin, ))
                    conn.commit()
                    self.select_emp()
        except Exception as error:
                print("erreur: ", error)


    def rechercher(self, text):
        conn = connection.connection
        cursor = conn.cursor()

        query = "SELECT cin, nom, prenom, fonction, date_debut FROM EMP WHERE cin LIKE ? OR nom LIKE ? OR prenom LIKE ? OR fonction LIKE ? OR date_debut LIKE ?"
        search_text = f"%{text}%"
        cursor.execute(query, (search_text, search_text, search_text, search_text, search_text))
        table = cursor.fetchall()
        
        self.EMPTable.setRowCount(len(table))

        for row_num, line in enumerate(table):
            for col_num, data in enumerate(line):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.EMPTable.setItem(row_num, col_num, item)
             
            widget = QtWidgets.QWidget()
            widget.setStyleSheet("background-color: none;")
            layout = QtWidgets.QGridLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)

            view = QtWidgets.QPushButton()
            view.setStyleSheet("background-color: none; border: none;")
            view.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\view.png'))
            view.clicked.connect(self.open_view)

            delete = QtWidgets.QPushButton() 
            delete.setStyleSheet("background-color: none; border: none;")
            delete.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\bin.png'))
            delete.clicked.connect(self.delete_emp)

            layout.addWidget(view, 0, 0, alignment=QtCore.Qt.AlignCenter)
            layout.addWidget(delete, 0, 1, alignment=QtCore.Qt.AlignCenter)
            self.EMPTable.setCellWidget(row_num, 5, widget) 

    def close(self):
        from close import Ui_quitter
        self.Close = QtWidgets.QWidget()
        self.work = Ui_quitter()
        self.work.setupUi(self.Close)
        self.Close.show()
        def hide():
            self.work.logOut()
            EMP.hide()
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
        self.ui.set_user_info(name, pic_path)
        self.ui.setupUi(self.work_window)
        self.work_window.show()
        self.widget.hide()   

    def open_Dash(self, name, pic_path):
        from dashboard import Ui_dash
        self.work_window = QtWidgets.QMainWindow()
        self.ui = Ui_dash()
        self.ui.set_user_info(name, pic_path)
        self.ui.setupUi(self.work_window)
        self.work_window.show()
        self.widget.hide() 
                  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EMP = QMainWindow()
    ui = Ui_EMP()
    ui.setupUi(EMP)
    EMP.show()
    sys.exit(app.exec_())
