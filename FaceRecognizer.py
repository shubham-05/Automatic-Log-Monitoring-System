
import numpy as np

# Import OpenCV2 for image processing
import cv2
from database1 import retrieve
from database1 import insert
import sqlite3
# Load prebuilt model for Frontal Face
face_cascade = cv2.CascadeClassifier("HaarCascade/haarcascade_frontalface_default.xml")

# Create Local Binary Patterns Histograms for face recognization
recognize = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognize.read("Trainer/Trainer.yml")

# Initialize and start the video frame capture
camera = cv2.VideoCapture(0)

# Initilizing ID attribute
Id = 0

# Define the font type
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

# Loop
while 1:

    # Read the video frame
    ret, img = camera.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    # For each face in faces
    for (x, y, w, h) in faces:
        
        # Create rectangle around the face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 225, 225), 2)

        # Recognize the face belongs to which ID
        Id, conf = recognize.predict(gray[y:y + h, x:x + w])
        print str(Id)+" "+str(conf)
        # Check the ID if exist
        try:
            if(conf<60):
                Id = retrieve(Id)
                insert(Id)
            else:
                Id='Unknown'
        except sqlite3.Error,e:
            print 'here'
            Id='Unknown'
        cv2.rectangle(img, (x - 22, y - 45), (x + w + 15, y - 22), (0, 0, 0), -1)
        cv2.putText(img,"Name:" + str(Id), (x, y - 22), font, 1, (255, 255, 255), 2)

    # ID text which describe who is in the picture
    
    # Display the video frame with the bounded rectangle
    cv2.imshow('img', img)

    # If 'q' is pressed, close program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop the camera
camera.release()
# Close all windows
cv2.destroyAllWindows()