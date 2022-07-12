# Include all the needed libraries
import cv2
import easyocr
import matplotlib.pyplot as plt
import collections
import messagebox

# Funcion to run the easyocr on the input image
def recognize_text(img_path):
    # Define the reader and pass the image to the reader
    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)


# Function to Overlay the recognized text on image using OpenCV
def overlay_ocr_text(img_path, save_name, infoarray):

    # Load image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Image display details
    dpi = 80
    fig_width, fig_height = int(img.shape[0] / dpi), int(img.shape[1] / dpi)
    plt.figure()
    f, axarr = plt.subplots(1, 2, figsize=(fig_width, fig_height))
    axarr[0].imshow(img)

    # Recognize text
    result = recognize_text(img_path)

    # If OCR prob is over 0.7, overlay bounding box and text
    for (bbox, text, prob) in result:
        if prob >= 0.7:
            # Get top-left and bottom-right bbox vertices
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = (int(top_left[0]), int(top_left[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

            # Create a rectangle for bbox display
            cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=10)

            # Put recognized text
            cv2.putText(img=img, text=text, org=(top_left[0], top_left[1] - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, color=(255, 0, 0), thickness=8)

            # Add info into array
            text2 = text.upper()
            infoarray.append(text2)

    # Show and save image
    axarr[1].imshow(img)

    # Return array that contains all necessary information abstracted from Image
    return infoarray

# Function to flatten an array
def flatten(iterable):
    for el in iterable:
        if isinstance(el, collections.Iterable) and not isinstance(el, str):
            yield from flatten(el)
        else:
            yield el

# Main function to execute all code
def main():

    # Notifying user that the cross verification is starting
    messagebox.showinfo("Success", "Cross-Verification process will start after you press OK. Please wait for the processsing, you will be given a prompt " +
                                   "when the processing has been completed ")

    # Create empty arrays to store information in
    VaccinationPassInformation = []
    LicenceInformation = []

    # Load Images
    IdentityImage = "ImageData/IdentityImage.PNG"
    MyCovidVaccinationPassImage = "ImageData/MyCovidVaccinationPassImage.PNG"

    # Running overlay on image
    Array1 = overlay_ocr_text(MyCovidVaccinationPassImage, "MyVaccinaitonPassExample-WithOcrOverlay", VaccinationPassInformation)
    Array2 = overlay_ocr_text(IdentityImage, "License-WithOcrOverlay", LicenceInformation)

    # Perform flattening of the arrays
    a = flatten(Array1)
    b = flatten(Array2)

    # Store the common elements from each image into an array i.e. the First Name, Last Name, D.O.B. should be the overlap between the two images
    common_elements = list(set(a).intersection(set(b)))

    # Conditional check to ensure that the overlap is present | A minimum for two common elements should be present
    NumberOfElements = len(common_elements)

    if NumberOfElements == 3 or NumberOfElements == 4 or NumberOfElements == 2:

        img = cv2.imread(IdentityImage)
        cv2.imwrite("DF_Database/" + str(common_elements) + ".PNG", img)
        messagebox.showinfo("Success", "Verification Completed for: " + str(common_elements))