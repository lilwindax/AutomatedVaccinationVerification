# Include all the needed libraries
import cv2
import License_ID_Scanner
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from functools import partial

# Main class containing all functions for GUI functionality
class Identification_Image:
    def __init__(self, root):

        # Defining Tkinter window specifications
        self.root=root
        self.root.geometry("1024x668+0+0")
        self.root.minsize(1024, 668)
        self.root.maxsize(1024, 668)
        self.root.title("Upload Identification Image")
        self.root.iconbitmap("GUI/MainIcon.ico")

        # Main window frame
        mainFrame = Frame(self.root, width=1024, height=768)
        mainFrame.pack()

        # Background Image
        img = cv2.imread("GUI/UploadExistingImage.png")
        img = cv2.resize(img, (220, 260))
        cv2.imwrite("GUI/UploadExistingImage.png", img)
        backgroundImage = PhotoImage(file ="GUI/UploadIdImage.png")
        label1 = Label(mainFrame, image=backgroundImage)
        label1.place(x=0, y=0)
        label1.pack()

        # Capture New Id Image button
        captureNewId = PhotoImage(file ="GUI/CaptureNewImage.png")
        button1 = Button(mainFrame, image=captureNewId, command = lambda : (License_ID_Scanner.LicenceScanner()), cursor='hand2')
        button1.place(x = 220, y =260, width=220, height= 260)

        # Upload Existing Id Image button
        uploadExistingId = PhotoImage(file ="GUI/UploadExistingImage.png")
        button2 = Button(mainFrame, image=uploadExistingId, command=partial(self.ReadIdImage), cursor='hand2')
        button2.place(x=610, y=260, width=220, height=260)

        # Running the main tkinter loop
        self.root.mainloop()


    # Read Identification Image and save to project directory
    def ReadIdImage(self):
        filepath = filedialog.askopenfilename(title="Open",
                                              filetypes=(
                                                  ("all files", "*.*"), ("PNG File", "*.png"), ("JPG File", "*.jpg")))
        file = filepath
        IdentityImage = cv2.imread(file)
        cv2.imwrite("ImageData/IdentityImage.PNG", IdentityImage)
        messagebox.showinfo("Success", "Identification Image has been added successfully")


if __name__ == '__main__':
    root=Tk()
    obj = Identification_Image(root)
    root.mainloop()
