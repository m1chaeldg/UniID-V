#import read
import IDScanner
import FaceScanner
import face_recognition
import numpy as np


ID_image = face_recognition.load_image_file("IDScanned.jpg")
ID_face_encoding = face_recognition.face_encodings(ID_image)[0]

known_face_encodings = [
    ID_face_encoding,
]


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
    import UniformDetector
else:
    {
        print("Not Matched")
    }