#This is created by Mohammed Obeidi
#The purpose is to extract just the face from an image enhance it and make it ready to be used to predict the direction it is facing.

#imports
import cv2
import os

#get the absolute path to the cascade classifier files
cascade_face_path = os.path.abspath('haarcascade_frontalface_default.xml')
cascade_profile_path = os.path.abspath('haarcascade_profileface.xml')

#check if the cascade classifier file exists
if not os.path.exists(cascade_face_path):
    print("Cascade classifier face file not found")
    exit()
    
#check if the cascade classifier file exists
if not os.path.exists(cascade_profile_path):
    print("Cascade classifier profile file not found")
    exit()

#function to crop the image and check if a face is detected
def cl():
    #read the input image
    img = cv2.imread('captured_image.jpg')

    #check if the image is successfully loaded
    if img is None:
        print("Failed to load image")
        exit()

    #convert the image to grayscale needed to detect face
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #load the cascade classifier
    face_cascade = cv2.CascadeClassifier(cascade_face_path)
    profile_cascade = cv2.CascadeClassifier(cascade_profile_path)

    #check if the cascade classifiers are loaded successfully
    if face_cascade.empty():
        print("Failed to load cascade face classifier")
        exit()
        
    #check if the cascade classifier is loaded successfully
    if profile_cascade.empty():
        print("Failed to load cascade profile classifier")
        exit()

    #detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    if len(faces) == 0:
        #no faces detected trying profile faces
        faces = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        
    if len(faces) == 0:
        #no faces, or profile faces detected
        return False

    #draw rectangles around the faces and crop the faces
    for (x, y, w, h) in faces:
        #the rectangle box highlighting the face
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 0)
        #the face after cropping it out
        face = img[y:y+h, x:x+w]
        #resize the face image to 255 pixels by 255 pixels and convert to grayscale
        face = cv2.resize(face, (255, 255))
        #saving the resized and sharpened face image as a jpg to be used later
        cv2.imwrite('face.jpg', face)

    return True
