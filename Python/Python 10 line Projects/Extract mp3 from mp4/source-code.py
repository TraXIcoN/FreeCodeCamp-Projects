#previous version was not working this is new gui based version 

# Importing necessary packages
import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from moviepy.editor import *
import datetime
import  time

def Widgets(): 
    Convert_button = Button(root,text="Select File",command=converter,width=20,bg="red",pady=10,padx=25,
    font="Helvetica, 13")
    Convert_button.grid(row=4,column=2,pady=20,padx=20)

#function to select the video file  
def Browse():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Mp4 files","*.mp4*"),("all files","*.*")))
    print(filename)
    return filename

#fucntion to convert the video to audio
def converter():
    path=Browse()
    time.sleep(2)
    video =  VideoFileClip(path)
    audio=video.audio 
    #generating file name 
    date=datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    #saving the audio file
    try:
        audio.write_audiofile(f'{date}.mp3')
        messagebox.showinfo("success",'successfully converted ! 😃')
    #handling errors
    except Exception as e:
        messagebox.showerror('Failed ',f"Unable to download because {e}")

 
# Creating object of tk class
root = tk.Tk()
# Setting the title, background color
# and size of the tkinter window
root.geometry("520x280")
root.title("mp4 to mp3 converter")
root.config(background="black")
#calling the function
Widgets() 
root.mainloop()