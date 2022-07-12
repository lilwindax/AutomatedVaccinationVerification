# Include all the needed libraries
import cv2
import numpy as np
from tkinter import messagebox

# Define window width and height
widthImg = 640
heightImg = 640

# Initialize webcam
cap = cv2.VideoCapture(0) # Alter parameter value: 0 - Primary webcam, 1 - Secondary webcam
cap.set(10, 150)

# Define path for saving Licence Id Image
myPath = 'ImageData/'
saveData = True

# Function to perform Pre-processing to the Image
def PreProcessing(img):

    # Define 5x5 kernel
    kernel = np.ones((5, 5))

    # Convert Image to gray scale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)

    # Apply Canny Blur
    imgCanny = cv2.Canny(imgBlur, 200, 200)

    # Apply Dilation
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)

    # Apply Erosion
    imgThres = cv2.erode(imgDial, kernel, iterations=1)

    # Return Pre-processed Image
    return imgThres

# Function to find the biggest Contour in the image
def GetContours(img):

    # Variable initialization
    biggest = np.array([])
    maxArea = 0

    # Find all contours in Image
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # For loop to iterate through all contours in image
    for cnt in contours:

        # Calculate the area of the contour
        area = cv2.contourArea(cnt)

        # Condition check to see is contour area meets minimum area
        if area > 5000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    # Return the biggest contour
    return biggest

# Function to reorder the Contour
def Reorder(myPoints):

    # Apply reshaping
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)

    # Calculate new add points
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    # Calculate new diff points
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    # Return reordered contour
    return myPointsNew

# Function to wrap image
def GetWrap(img, biggest):

    # Get the reordered biggest contour
    biggest = Reorder(biggest)

    # Define points
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])

    # Create matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Generate output image
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    # Apply cropping to image
    imgCropped = imgOutput[20:imgOutput.shape[0] - 20, 20:imgOutput.shape[1] - 20]
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))

    # Return cropped image
    return imgCropped


def LicenceScanner():
    while True:

        # Run webcam and store its frames
        success, img = cap.read()

        # Resize Image to the predefined dimensions
        img = cv2.resize(img, (widthImg, heightImg))

        # Apply PrepProcessing to Image
        imgThres = PreProcessing(img)
        biggest = GetContours(imgThres)

        # Conditional check of biggest contour
        if biggest.size != 0:
            imgWarped = GetWrap(img, biggest)

            # Save Scanned Image and give prompt to user
            cv2.imwrite("ImageData/CaptureIdImage" + ".jpg", imgWarped)
            messagebox.showinfo("Success", "Identification Image has been saved successfully. Please close Web Cam Scanner window and restart program")
            cv2.waitKey(0)
            break

        # Display Webcam stream to user
        cv2.imshow("Web Cam Scanner", imgThres)

        # Conditional check to quit program
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break