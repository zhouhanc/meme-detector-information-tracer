import face_recognition
import numpy as np

def get_faceencode(paths):
    face_encodings=[]
    for path in paths:
    # Load an image with one or more faces
        image = face_recognition.load_image_file(path)

    # Find all face locations in the image
        face_locations = face_recognition.face_locations(image)
    # Generate face encodings for all faces in the image
        face_encoding = face_recognition.face_encodings(image, face_locations)
        if len(face_encoding) > 0:
            face_encoding = face_encoding[0]
            face_encodings.append(face_encoding)
        else:
            face_encodings.append(np.zeros(128))
    return face_encodings