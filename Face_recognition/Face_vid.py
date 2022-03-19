import face_recognition  
import numpy as np
import cv2

def Temp(i,known_face_encodings,known_face_names,tim):
    

    vedion_cap = cv2.VideoCapture(0)

    import time as t
    time = t.time()
    count1 = 0
    count2 = 0
    while True:
            
        ret,frame = vedion_cap.read()
            
        rgb_frame = frame[:, :, ::-1]
            
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame,face_locations)
        print(type(face_encodings))
        
        for known_face_encoding in known_face_encodings :
            for x in known_face_encoding:
                if (np.linalg.norm(x-face_encodings)) < i:
                    print(np.linalg.norm(x-face_encodings))

            for (top,right,bottom,left),face_encoding in zip(face_locations,face_encodings) :
                matches = face_recognition.compare_faces(known_face_encoding, face_encoding,i)
                name = "Unknown"
            print(matches)
            if True in matches:
                index_of_match = matches.index(True)
                name = known_face_names[index_of_match]
                count1+=1
            count2+=1

        # cv2.rectangle(frame, (left,bottom - 25), (right, bottom), (0,0,255) , cv2.FILLED)
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame,name, (left + 6, bottom - 6) ,font, 1.0, (255,255,255), 1)

        # cv2.imshow('Vedio',frame)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
        if (t.time()-time)>tim:
            break

    # vedion_cap.release()
    # cv2.destroyAllWindows()

    return count1*100/count2