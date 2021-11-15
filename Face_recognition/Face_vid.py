import face_recognition  
import numpy as np
import cv2
vedion_cap = cv2.VideoCapture(0)

parshvi_image = face_recognition.load_image_file("..\Images/parshvi.jpg")
parshvi_face_encodings = face_recognition.face_encodings(parshvi_image)[0]

rushabh_image = face_recognition.load_image_file("..\Images/rushabh.jpg")
rushabh_face_encodings = face_recognition.face_encodings(rushabh_image)[0]

known_face_encodings = [ 
    parshvi_face_encodings,
    rushabh_face_encodings,
    ]

known_face_names = [
        "Parshvi",
        "Rushabh"
]

while True:
         
    ret,frame = vedion_cap.read()
        
    rgb_frame = frame[:, :, ::-1]
        
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)

    for (top,right,bottom,left), face_encoding in zip(face_locations,face_encodings) :
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        print(matches)
        name = "Unknown"
        if True in matches:
            index_of_match = matches.index(True)
            name = known_face_names[index_of_match]

        cv2.rectangle(frame, (left,bottom - 25), (right, bottom), (0,0,255) , cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name, (left + 6, bottom - 6) ,font, 1.0, (255,255,255), 1)
        print("Found ",name ,"on camera")
        break 
            
    cv2.imshow('Vedio',frame)

    if cv2.waitKey(1) &0xFF == ord('q'):
        break

vedion_cap.release()
cv2.destroyAllWindows()