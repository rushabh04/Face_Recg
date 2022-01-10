import face_recognition  
import numpy as np
import cv2

vedion_cap = cv2.VideoCapture(0)
parshvi_face_encodings = face_recognition.face_encodings(
    face_recognition.load_image_file("..\Images/parshvi.jpg"))[0]
rushabh_face_encodings = face_recognition.face_encodings(
    face_recognition.load_image_file("..\Images/rushabh.jpg"))[0]
# rushabhside1_face_encodings = face_recognition.face_encodings(
#     face_recognition.load_image_file("..\Images/Rushabh_side.jpg"))[0]
# rushabhside2_face_encodings = face_recognition.face_encodings(
#     face_recognition.load_image_file("..\Images/Rushabh_side2.jpg"))[0]
mahira_face_encodings = face_recognition.face_encodings(
    face_recognition.load_image_file("..\Images/Mahira.jpg"))[0]




known_face_encodings = [ 
    parshvi_face_encodings,
    rushabh_face_encodings,
    mahira_face_encodings
    ]

known_face_names = [
        "Parshvi",
        "Rushabh",
        "Mahira"
    ]
# print(rushabh_face_encodings)
import time as t
time = t.time()
print((t.time()-time))
while True:
         
    ret,frame = vedion_cap.read()
        
    rgb_frame = frame[:, :, ::-1]
        
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)

    for (top,right,bottom,left), face_encoding in zip(face_locations,face_encodings) :
        for known_face_encoding in known_face_encodings :
            print(np.linalg.norm(known_face_encoding-face_encodings))
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
    # if True in matches:
    #     break
            
    cv2.imshow('Vedio',frame)

    if cv2.waitKey(1) &0xFF == ord('q'):
        break
    if (t.time()-time)>10:
        break

vedion_cap.release()
cv2.destroyAllWindows()