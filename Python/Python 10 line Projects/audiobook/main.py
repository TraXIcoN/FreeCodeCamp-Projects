#GUI based audiobook
#Imported required libraries
import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
import pyttsx3
import PyPDF2
from PyPDF2 import PdfFileReader

#for speak function
engine=pyttsx3.init("sapi5")
#sapi5 helps to enhance sppech-text recognition
#get some properties of pyttsx3
voices=engine.getProperty('voices')
engine.getProperty('rate')
engine.getProperty('volume')
#change the rate of reading a/q to you  
# suggestion : put it <150
engine.setProperty('rate', 165)
#this changes the volume level 
engine.setProperty('volume',200 )
engine.setProperty('voices' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function to show buttons appearing on screen 
def Widgets(): 
    pdf_selector = Button(root,text="Select the PDF",command=PDFreader,width=20,bg="red",pady=10,padx=25,
    font="Helvetica, 13")
    pdf_selector.grid(row=4,column=2,pady=20,padx=20)

#function to select the PDF file  
def Browse():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("PDF files","*.pdf*"),("all files","*.*")))
    print(filename)
    return filename


#Function to read pages of file
def PDFreader():
    #getting file path for pdf
    file_path=Browse()
    print(file_path)
    # Creating a pdf file object.
    pdf = open(file_path, "rb")
    # Creating pdf reader object.
    pdf_reader = PyPDF2.PdfFileReader(pdf)
    # Checking total number of pages in a pdf file.
    total_pages = pdf_reader.numPages
    #loop for reading the file from 4th page to last
    for page_no in range(0,total_pages):
        page=pdf_reader.getPage(page_no)
        text=page.extractText()
        print(text)
        speak(text)
    pdf.close()
 
# Creating object of tk class
root = tk.Tk()
# Setting the title, background color
# and size of the tkinter window
root.geometry("520x280")
root.title("Audiobook")
root.config(background="black")
#calling the function
Widgets() 
root.mainloop()