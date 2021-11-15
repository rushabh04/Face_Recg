import  face_recognition
import  numpy as np
import  cv2
vedion_cap = cv2.VideoCapture(0)

while True:
    ret,frame = vedion_cap.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encode = face_recognition.face_encodings(rgb_frame,face_locations)

    for (top,right,bottom,left), face_encode in zip(face_locations,face_encode):

        cv2.rectangle(frame, (left,top),(right,bottom),(0,255,0),2)

    cv2.imshow('Vedio',frame)

    if cv2.waitKey(1) &0xFF == ord('q'):
        break

vedion_cap.release()
cv2.destroyAllWindows()