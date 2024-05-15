from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import face_recognition
import glob
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime, timedelta
import sys
import dlib
import connection


class Ui_cam(object):
    def __init__(self) -> None:
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.detected_faces = set()
        self.conn = connection.connection

        self.widget = QtWidgets.QWidget()
        self.setupUi(self.widget)

        self.known_faces = []
        self.known_names = []

        self.registered_faces = 'registred/'

        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        layout.addWidget(self.captur)

        self.load_known_faces()

        self.timer = QTimer()
        self.timer.timeout.connect(self.capture_face)
        self.timer.start(30)

        self.detecteur = dlib.get_frontal_face_detector()
        model_path = "shape_predictor_68_face_landmarks.dat"
        self.predicteur = dlib.shape_predictor(model_path)

        self.face_detect_time = None
        self.face_leave_time = None

        self.arrive = []
        self.depart = []

        self.duree = []
        self.rowPosition = 0

    def load_known_faces(self):
        for name in os.listdir(self.registered_faces):
            images_mask = os.path.join(self.registered_faces, name, '*.jpg')
            images_paths = glob.glob(images_mask)
            for image in images_paths:
                encoding = self.get_encoding(image)
                if encoding is not None:
                    self.known_faces.append(encoding)
                    self.known_names.append(name)

    def get_encoding(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            return face_encodings[0]
        return None

    def point_id(self, rgb, frame):
        faces = self.detecteur(rgb)
        for face in faces:
            landmarks = self.predicteur(rgb, face)
            for i in range(68):
                x = landmarks.part(i).x
                y = landmarks.part(i).y
                cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    def capture_face(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame_rgb)
        self.point_id(frame_rgb, frame)

        for face in faces:
            top, right, bottom, left = face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            encoding = face_recognition.face_encodings(frame_rgb, [face])[0]

            matches = face_recognition.compare_faces(self.known_faces, encoding)
            name = "inconnue"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_names[first_match_index]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 128, 0), 2)

                if name == 'banned':
                    cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
                    cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                    continue

                self.update_presence(face, name)

            cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 128, 0) if name != "inconnue" else (0, 0, 255), 2)

        frame = cv2.resize(frame, (640, 480))
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.captur.setPixmap(pixmap)

    def update_presence(self, face, name):
        self.time(face, name)
        cursor = self.conn.cursor()
        query = "SELECT cin, nom, temp_arrive, temp_depart, duree FROM EMP WHERE cin = ?;"
        cursor.execute(query, (name,))
        result = cursor.fetchall()

        self.presence.setRowCount(len(result))
        for row, data in enumerate(result):
            if data is not None:
                cin, nom, heurArrive, heurDepart, duree = data
                self.presence.setItem(row, 0, QTableWidgetItem(str(cin)))
                self.presence.setItem(row, 1, QTableWidgetItem(nom))
                self.presence.setItem(row, 2, QTableWidgetItem(str(heurArrive)))
                self.presence.setItem(row, 3, QTableWidgetItem(str(heurDepart)))
                self.presence.setItem(row, 4, QTableWidgetItem(str(duree)))

    def time(self, face, name):
        cursor = self.conn.cursor()
        current_time = datetime.now().strftime("%H:%M:%S")

        if face:
            if self.face_detect_time is None:
                self.face_detect_time = current_time
                self.arrive.append(self.face_detect_time)
                arrive = min(self.arrive)
                query = "UPDATE EMP SET temp_arrive = ? WHERE cin = ?;"
                cursor.execute(query, (arrive, name))
                self.conn.commit()
            else:
                if self.face_leave_time is None:
                    self.face_leave_time = current_time
                    self.depart.append(self.face_leave_time)
                    depart = max(self.depart)
                    query1 = "UPDATE EMP SET temp_depart = ? WHERE cin = ?;"
                    cursor.execute(query1, (depart, name))
                    self.conn.commit()

                    self.face_leave_time = None
                    self.face_detect_time = None

                    arrive = datetime.strptime(min(self.arrive), "%H:%M:%S")
                    depart = datetime.strptime(max(self.depart), "%H:%M:%S")
                    self.update_duration(arrive, depart, name)

    def update_duration(self, arrive, depart, name):
        cursor = self.conn.cursor()
        duree_personne = depart - arrive
        self.duree.append(duree_personne)
        total = sum(d.total_seconds() for d in self.duree)
        total_duration = timedelta(seconds=total)
        total_duration_str = str(total_duration)
        query2 = "UPDATE EMP SET duree = ? WHERE cin = ?;"
        cursor.execute(query2, (total_duration_str, name))
        self.conn.commit()

    def list_abs(self):
        cursor = self.conn.cursor()
        query = "SELECT cin, nom FROM EMP WHERE temp_arrive IS NULL;"
        cursor.execute(query)
        result = cursor.fetchall()

        self.absance.setRowCount(len(result))
        for row, data in enumerate(result):
            cin, nom = data
            self.absance.setItem(row, 0, QTableWidgetItem(cin))
            self.absance.setItem(row, 1, QTableWidgetItem(nom))

    def setupUi(self, cam):
        cam.setObjectName("cam")
        cam.resize(869, 588)
        cam.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        cam.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(cam)
        self.widget.setGeometry(QtCore.QRect(20, 10, 841, 581))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-radius: 9px;")
        self.widget.setObjectName("widget")

        def reduit():
            cam.showMinimized()

        self.reduit = QtWidgets.QPushButton(self.widget)
        self.reduit.clicked.connect(reduit)
        self.reduit.setGeometry(QtCore.QRect(806, 10, 12, 12))
        self.reduit.setStyleSheet("QPushButton{\nbackground-color: rgb(0, 170, 0);\nborder-radius: 6px;\nborder: none;\n}\nQPushButton:pressed{\nbackground-color: rgb(0, 255, 0);\n}")
        self.reduit.setText("")
        self.reduit.setObjectName("reduit")

        self.close = QtWidgets.QPushButton(self.widget)
        self.close.setGeometry(QtCore.QRect(820, 10, 12, 12))
        self.close.setStyleSheet("QPushButton{\nbackground-color: rgb(170, 0, 0);\nborder-radius: 6px;\nborder: none;\n}\nQPushButton:pressed{\nbackground-color: rgb(255, 0, 0);\n}")
        self.close.setText("")
        self.close.setObjectName("close")

        self.captur = QtWidgets.QLabel(self.widget)
        self.captur.setGeometry(QtCore.QRect(120, 20, 591, 301))
        self.captur.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.captur.setText("")
        self.captur.setObjectName("captur")

        self.absance = QtWidgets.QTableWidget(self.widget)
        self.absance.setGeometry(QtCore.QRect(600, 370, 211, 192))
        self.absance.setStyleSheet("QTableWidget {\nbackground-color: rgb(226, 226, 226);\nborder-radius: 10px;\n}\nQTableWidget::item {\nbackground-color: rgb(176, 111, 255);\n}")
        self.absance.setObjectName("absance")
        self.absance.setColumnCount(2)
        self.absance.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.absance.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.absance.setHorizontalHeaderItem(1, item)

        self.presence = QtWidgets.QTableWidget(self.widget)
        self.presence.setGeometry(QtCore.QRect(30, 370, 511, 192))
        self.presence.setStyleSheet("QTableWidget {\nbackground-color: rgb(226, 226, 226);\nborder-radius: 10px;\n}\nQTableWidget::item {\nbackground-color: rgb(176, 111, 255);\n}")
        self.presence.setObjectName("presence")
        self.presence.setColumnCount(5)
        self.presence.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(4, item)

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 340, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(610, 340, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(cam)
        QtCore.QMetaObject.connectSlotsByName(cam)
        self.list_abs()

    def retranslateUi(self, cam):
        _translate = QtCore.QCoreApplication.translate
        cam.setWindowTitle(_translate("cam", "cam"))
        item = self.absance.horizontalHeaderItem(0)
        item.setText(_translate("cam", "CIN"))
        item = self.absance.horizontalHeaderItem(1)
        item.setText(_translate("cam", "Nom"))
        item = self.presence.horizontalHeaderItem(0)
        item.setText(_translate("cam", "CIN"))
        item = self.presence.horizontalHeaderItem(1)
        item.setText(_translate("cam", "NOM"))
        item = self.presence.horizontalHeaderItem(2)
        item.setText(_translate("cam", "Heure d'arrivee"))
        item = self.presence.horizontalHeaderItem(3)
        item.setText(_translate("cam", "Heure de depart"))
        item = self.presence.horizontalHeaderItem(4)
        item.setText(_translate("cam", "Temps de Travail"))
        self.label_2.setText(_translate("cam", "Liste de présence"))
        self.label_3.setText(_translate("cam", "Liste d'absence"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cam = QtWidgets.QWidget()
    ui = Ui_cam()
    ui.setupUi(cam)
    cam.show()
    sys.exit(app.exec_())
