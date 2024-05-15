import cv2 
import os
import face_recognition
import glob
from datetime import datetime, timedelta
import dlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import connection

class camera(QLabel):
    def __init__(self, label):
        super().__init__()
        self. label = label
        
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("Error: Failed to open camera.")
        else:
            print("Camera opened successfully.")

        self.known_faces = []
        self.known_names = []

        self.registered_faces = 'registred/'

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        for name in os.listdir(self.registered_faces):
            images_mask = os.path.join(self.registered_faces, name, '*.jpg')
            images_paths = glob.glob(images_mask)
            for image_path in images_paths:
                encoding = self.get_encoding(image_path)
                if encoding is not None:
                    self.known_faces.append(encoding)
                    self.known_names.append(name)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

        self.detecteur = dlib.get_frontal_face_detector()
        model_path = "C:\\Users\\hp\\Desktop\\easy_facial_recognition-master\\easy_facial_recognition-master\\pretrained_model\\shape_predictor_68_face_landmarks.dat"

        try:
            self.predictor = dlib.shape_predictor(model_path)
        except RuntimeError as e:
            print("erreur: ", e)
            sys.exit(1)

        self.face_detect_time = None
        self.face_leave_time = None
        self.last_detection_day = None

        self.duree = []

        self.conn = connection.connection

    def get_encoding(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)
        if len(face_encoding) > 0:
            return face_encoding[0]
        return None
    
    def update_frame(self):
        print("Updating frame...")
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame_rgb)

        print('frame size: ', frame_rgb.shape)
        print('label size: ', self.label.size())

        self.point_id(frame_rgb, frame)

        for face in faces:
            top, right, bottom, left = face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            encoding = face_recognition.face_encodings(frame_rgb, [face])[0]

            rst = face_recognition.compare_faces(self.known_faces, encoding)

            if any(rst):
                name = self.known_names[rst.index(True)]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 128, 0), 2)
                cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 128, 0), 2)

            else:
                name = 'inconnue'
                cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            self.time(faces, name)
            frame = cv2.resize(frame, (640, 480))
            image = QImage(frame_rgb, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.setPixmap(pixmap)

    def point_id(self, rgb, frame):
        faces = self.detecteur(rgb)
        for face in faces:
            landmarks = self.predictor(rgb, face)

            for i in range(68):
                x = landmarks.part(i).x
                y = landmarks.part(i).y
                cv2.circle(frame, (x, y), 1, (128, 128, 128), -1)

    def time(self, faces, name):
        total_duration = None
        if faces:
            if self.face_detect_time is None:
                self.face_detect_time = datetime.now()
                self.last_detection_day = self.face_detect_time.strftime("%H:%M:%S")
            
            if self.face_leave_time is None and self.face_detect_time is not None:
                if self.last_detection_day == datetime.now().date():
                    self.face_leave_time = datetime.now()
                    duree_personne = self.face_leave_time - self.face_detect_time
                    self.duree.append(duree_personne)
                    total_seconds = sum(d.total_seconds() for d in self.duree)
                    total_duration = timedelta(seconds=total_seconds)
                    self.face_detect_time = None
                    self.face_leave_time = None

        cursor = self.conn.cursor()

        insert = """
    UPDATE EMP 
    SET temp_depart = CONVERT(VARCHAR, ?), 
        temp_arrive = CONVERT(VARCHAR, ?), 
        duree = ? 
    WHERE cin = ?;
"""
        cursor.execute(insert, (self.last_detection_day, self.face_leave_time, total_duration, name))

        self.conn.commit()

        today = datetime.now().date()
        update = "UPDATE EMP SET temp_depart = NULL, temp_arrive = NULL, duree = NULL WHERE CAST(temp_depart AS TIME) < CAST(? AS TIME);"
        cursor.execute(update, (today,))













