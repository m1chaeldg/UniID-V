#import read
import IDScanner
import FaceScanner
import face_recognition
import numpy as np
import UniformScanner


class App:

    def Run():
        uniformScanner = UniformScanner()
        faceScanner = FaceScanner()
        idScanner = IDScanner()

        faceScanner.Scan()
        idScanner.Scan()


        ID_image = face_recognition.load_image_file("IDScanned.jpg")
        ID_face_encoding = face_recognition.face_encodings(ID_image)[0]


        face_locations = []
        face_encodings = []

        image = face_recognition.load_image_file("FaceScanned.jpg")
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        matches = face_recognition.compare_faces(ID_face_encoding, face_encodings)

        face_distances = face_recognition.face_distance(ID_face_encoding, face_encodings)


        #best_match_index = np.argmin(face_distances)
        match = np.argmin(face_distances)
        if matches[match]:
            {
                print("Matched")
            }
            uniformScanner.Scan()
        else:
            {
                print("Not Matched")
            }

# start the application
app = App()
app.Run() 