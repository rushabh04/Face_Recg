from PIL import Image,ImageDraw
import face_recognition

image = face_recognition.load_image_file("../Images/parshvi.jpg")

face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph ".format(len(face_locations)))

pil_image = Image.fromarray(image)
draw= ImageDraw.Draw(pil_image)

for face_location in face_locations:

    top,right,bottom,left = face_location
    top=top-40
    right=right+12
    bottom=bottom+10
    left=left-17
    print("Top:{} Right:{} Bottom:{} Left:{}".format(top,right,bottom,left))
    draw.rectangle(((left,top),(right,bottom)),outline=(0,255,0))

pil_image.show()