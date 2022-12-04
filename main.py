# import read
import IDScanner
import FaceScanner
import face_recognition
import numpy as np
import UniformScanner


class App:

    def Run(self):
        uniform_scanner = UniformScanner.UniformScanner()
        face_scanner = FaceScanner.FaceScanner()
        id_scanner = IDScanner.IDScanner()

        face_scanner.Scan()
        id_scanner.Scan()

        id_image = face_recognition.load_image_file("IDScanned.jpg")
        id_face_encoding = face_recognition.face_encodings(id_image)[0]

        image = face_recognition.load_image_file("FaceScanned.jpg")
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        matches = face_recognition.compare_faces(id_face_encoding, face_encodings)

        face_distances = face_recognition.face_distance(id_face_encoding, face_encodings)

        # best_match_index = np.argmin(face_distances)
        match = np.argmin(face_distances)
        if matches[match]:
            {
                print("Matched")
            }
            uniform_scanner.Scan()
        else:
            {
                print("Not Matched")
            }


# start the application
app = App()
app.Run()
