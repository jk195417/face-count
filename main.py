from PIL import Image
import face_recognition as fr


image = fr.load_image_file('/Users/Xin/Downloads/nsysu_xmas.JPG')

pil_image = Image.fromarray(image)
pil_image.show()

face_locations = fr.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
