# Include all the needed libraries
import cv2
import numpy as np
import face_recognition
import os

# Variable intialization
path = 'DF_Database/'
images = []
DatasetNames = []
myList = os.listdir(path)

# For loop to iterate from all images in Data folder
for data in myList:
    curImg = cv2.imread(f'{path}/{data}')
    images.append(curImg)
    DatasetNames.append(os.path.splitext(data)[0])

# Function to find encodings
def FindEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = FindEncodings(images)

def main():

    # Intialize the Webcam
    cap = cv2.VideoCapture(0)

    # Loop to run webcam frame by frame
    while True:
        success, img = cap.read()

        # Reducing size of image to process to lower computation level
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        # Find the encodings of potential more than one Face
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        # Loop to iterate through the Encodings
        for encodeFace, faceLocation in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            # Locate the matching Index
            matchIndex = np.argmin(faceDis)

            # Display a bounding box on the matching index
            if matches[matchIndex]:
                name = DatasetNames[matchIndex]

                y1, x2, y2, x1 = faceLocation
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                cv2.rectangle(img, (x1, y1), (x2, y2), (128, 0, 128), 2)
                cv2.putText(img, "Verified Personal", (x1 + 6, y2 + 25 ), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        # Run and show webcam
        cv2.imshow('Running Vaccination Verification System', img)
        cv2.waitKey(1)

        # Conditional check to close webcam window when user prompts
        if cv2.getWindowProperty('Running Vaccination Verification System', cv2.WND_PROP_VISIBLE) < 1:
            break
        key = cv2.waitKey(1) & 0xFF

        # If the `q` key was pressed, break from the loop
        if key == ord('q'):
            break

    cap.release()