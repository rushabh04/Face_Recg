from PIL import Image,ImageDraw,ImageFont
import face_recognition

parshvi_image = face_recognition.load_image_file("../Images/parshvi.jpg")
parshvi_face_encodings = face_recognition.face_encodings(parshvi_image)[0]

rushabh_image = face_recognition.load_image_file("..\Images/rushabh.jpg")
rushabh_face_encodings = face_recognition.face_encodings(parshvi_image)[0]

known_face_encodings = [
        parshvi_face_encodings,
        rushabh_face_encodings
]
known_face_names = [
        "Parshvi",
        "Rushabh"
]


image = face_recognition.load_image_file("../Images/rushabh.jpg")

face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)


pil_image = Image.fromarray(image)
draw= ImageDraw.Draw(pil_image)

for (top,right,bottom,left), face_encodings in zip(face_locations,face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
    name = "Unknown"

    if True in matches:
        index_of_match = matches.index(True)
        name = known_face_names[index_of_match]
        text_w,text_h = draw.textsize(name)
        draw.rectangle(((left,top - text_h -10),(right,bottom)),outline=(0,255,0))
        draw.text((left-6, bottom - text_h + 5 ),name,font=ImageFont.truetype("../Fonts/DellaRespira-Regular.ttf",30) ,fill=(225,225,225))
del draw
pil_image.show()


    
