import Face_vid as fy
u= input("Enter your user name: ").upper()
import face_recognition  
import os
from os import listdir

ke = []
kn = []
temporary = []
folder_dir = "c:\MyThings\Face_Recg\Images"
fol = folder_dir+'/'+ u
# rgb_frame = []
for images in os.listdir(fol):
    Imag = face_recognition.load_image_file(fol+"/"+images)
    rgb_frame = Imag[:, :, ::-1]
    print(rgb_frame)
    # face_locations = face_recognition.face_locations(rgb_frame)
    # temporary += face_recognition.face_encodings(rgb_frame,face_locations)
    temporary += face_recognition.face_encodings(Imag)
    kn.append(images)
ke.append(temporary)
tolerace = [0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45]
pem ={}
for x in tolerace:
    temp = fy.Temp(x,ke,kn,2)
    pem[x] = temp
sum = 0
count = 0
for i in pem:
    sum+=pem[i]
    count+=1
print("Average acc: ",sum/count)