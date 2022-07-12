# Include all the needed libraries
import cv2
import OCR_Image_Analysis
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
from DeepFace_Algorithm import main
from Identification_Image_Page import Identification_Image

# Main class containing all functions for GUI functionality
class Automated_Vaccination_Verification:
    def __init__(self, root):

        # Defining Tkinter window specifications
        self.root=root
        self.root.geometry("1024x668+0+0")
        self.root.minsize(1024, 668)
        self.root.maxsize(1024, 668)
        self.root.title("A.I. Enabled Vaccination Verification")
        self.root.iconbitmap("GUI/MainIcon.ico")

        # Main window frame
        mainFrame = Frame(self.root, width=1024, height=768)
        mainFrame.pack()

        # Background Image
        backgroundImage = PhotoImage(file ="GUI/MainHomePage.png")
        label1 = Label(mainFrame, image=backgroundImage)
        label1.place(x=0, y=0)
        label1.pack()

        # Vaccination button
        vaccinationImage = PhotoImage(file ="GUI/VaccinationVerificantion.png")
        button1 = Button(mainFrame, image=vaccinationImage, command=partial(self.ReadPassImage), cursor='hand2')
        button1.place(x = 110, y =220, width=220, height= 260)

        # Identification button
        indentificationButton = PhotoImage(file ="GUI/IdentityVerification.png")
        button2 = Button(mainFrame, image=indentificationButton, command= self.IdentificationWindow, cursor='hand2')
        button2.place(x=407, y=220, width=220, height=260)

        #Upload Verification Details button
        verificationButton = PhotoImage(file ="GUI/UploadVerificationDetails.png")
        button3 = Button(mainFrame, image=verificationButton, command = lambda : OCR_Image_Analysis.main(), cursor='hand2')
        button3.place(x=700, y=220, width=220, height=260)

        # Run Verification button
        runverificationButton = PhotoImage(file="GUI/RunVerificationSystem.png")
        button4 = Button(mainFrame, image=runverificationButton, command= lambda : main(), cursor='hand2')
        button4.place(x=240, y=525, width=550, height= 50)

        # Running the main tkinter loop
        self.root.mainloop()

    # Read Vaccination Pass Image and save to project directory
    def ReadPassImage(self):
        filepath = filedialog.askopenfilename(title="Open",
                                              filetypes=(
                                                  ("all files", "*.*"), ("PNG File", "*.png"), ("JPG File", "*.jpg")))
        file = filepath
        MyCovidVaccinationPassImage = cv2.imread(file)
        cv2.imwrite("ImageData/MyCovidVaccinationPassImage.PNG", MyCovidVaccinationPassImage)
        messagebox.showinfo("Success", "My Covid Vaccination Pass Image has been added successfully")

    # Function to open Identification window
    def IdentificationWindow(self):

        self.new_window = Toplevel(self.root)
        self.app = Identification_Image(self.new_window)


# Running main
if __name__ == '__main__':
    root=Tk()
    obj = Automated_Vaccination_Verification(root)
    root.mainloop()