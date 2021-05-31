# Importing the Libraries
import pyttsx3
import pdfplumber
import PyPDF2
from tkinter import *
from tkinter.filedialog import askopenfilename


def fileLocation():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    global file
    file = askopenfilename()  # open the dialog GUI


def maleButton():
    global Voice_Choice
    Voice_Choice = "Male"


def femaleButton():
    global Voice_Choice
    Voice_Choice = "Female"


def convertText2Speech():
    # Creating a PDF File Object
    pdfFileObj = open(file, 'rb')

    # Create a PDF File Reader Object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Get the number of pages
    pages = pdfReader.numPages

    # Create a pdfplumber object and loop through the No.Of Pages in PDF file
    with pdfplumber.open(file) as pdf:
        # Loop Through The Number Of Pages
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            # Checking Option for the User
            if Voice_Choice == "Male":
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
            elif Voice_Choice == "Female":
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
            else:
                voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
            speaker = pyttsx3.init()
            speaker.setProperty('volume', vol.get())
            speaker.setProperty('voice', voice_id)
            speaker.say(text)
            speaker.runAndWait()


# Creating the GUI
root = Tk()
root.title("AudioBook")
root.geometry("1280x720")
# Step 1 Text
# Create text widget and specify size.
T = Text(root, height=5, width=52)

# Create label
l = Label(root, text="Step 1 : Select Location")
l.config(font=("Courier", 14))
l.pack()

fileButton = Button(root, text="Select Location", command=fileLocation)
fileButton.pack(pady=20)

# Step 1 Text
# Create text widget and specify size.
T = Text(root, height=5, width=52)

# Create label
l2 = Label(root, text="Step 2 : Select Gender Voice")
l2.config(font=("Courier", 14))
l2.pack()

MaleButton = Button(root, text="Male", command=maleButton)
MaleButton.pack(pady=20)

FemaleButton = Button(root, text="Female", command=femaleButton)
FemaleButton.pack(pady=20)

l4 = Label(root, text="Step 3 : Set Your Desirable Volume")
l4.config(font=("Courier", 14))
l4.pack(pady=20)

vol = Scale(
    from_=0,
    to=100,
    orient=HORIZONTAL,
    resolution=1,
)
vol.pack()

# Create label
l3 = Label(root, text="Step 4 : Press Convert to Convert pdf to Voice")
l3.config(font=("Courier", 14))
l3.pack(pady=20)

ConvertButton = Button(root, text="Convert", command=convertText2Speech)
ConvertButton.pack(pady=20)
root.mainloop()
