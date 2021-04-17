import tkinter
from tkinter import *
from tkinter import filedialog
import pyttsx3

root = Tk()

root.title("Text to speech convertor")
root.geometry("500x310")
root.resizable(width=False,height=False)
def upload():
    ro = Tk()
    ro.title("Text file to speech convertor")
    ro.geometry("500x350")
    ro.resizable(width=False,height=False)
    menubar = Menu(ro)
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'File',menu=file)
    file.add_command(label='Back', command=ro.destroy)
    description = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Project made by', menu = description)
    description.add_command(label = 'CMPN D7A',command=None)
    description.add_command(label = '39-Yash kriplani-D7A',command=None)
    description.add_command(label = '69-Varun Tripathy-D7A',command=None)
    description.add_command(label = '72-Shubham Zope-D7A',command=None)

    ro.config(menu=menubar)

    myLabel1 = Label(ro, text="Text file to speech conventor", width="50", pady=10, fg="#26001b", bg="#51c4d3", font="bold")
    myLabel1.pack(side=TOP)
    def open_txt():
        text_file = filedialog.askopenfilename(initialdir="C:/Users/shubu/Desktop/sem4/python/", title="Open text files", filetypes=(("Text file", "*.txt"), ))
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        TBox1.insert(END, stuff)
        text_file.close()




    TBox1 = Text(ro,height=15,width=300,bg="#d3f2ee")
    TBox1.pack()
    upload = Button(ro, text="Upload file",command=open_txt, width="100",font="bold", anchor="w")
    upload.place(x=0,y=250)

    def speaktex():
        engine = pyttsx3.init()
        voice = engine.getProperty("voices")
        engine.setProperty("voices",voice[1].id)

        if not TBox1.get("1.0","end-1c"):
            engine.say("Upload a txt file and click on speak button")
            engine.runAndWait()
        else:
            text1 = TBox1.get("1.0","end-1c")
            engine.say(text1)
            engine.runAndWait()



    myButton1 = Button(ro, text="Speak the entered text",command=speaktex, width="100", pady=15, fg="white", bg="#18aff5", font="bold")
    myButton1.pack(side = BOTTOM)
    ro.mainloop()

menubar = Menu(root)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File',menu=file)
file.add_command(label='Upload File',command=upload)
file.add_command(label='Exit', command=root.destroy)

description = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Project made by', menu = description)
description.add_command(label = 'CMPN D7A',command=None)
description.add_command(label = '39-Yash kriplani-D7A',command=None)
description.add_command(label = '69-Varun Tripathy-D7A',command=None)
description.add_command(label = '72-Shubham Zope-D7A',command=None)

root.config(menu=menubar)

myLabel = Label(root, text="Text to speech conventor", width="50", pady=10, fg="#26001b", bg="#51c4d3", font="bold")
myLabel.pack(side=TOP)
    
label1 = Label(root, text="Enter some text here",width="100", pady=10, fg="red", font=("Arial", 10))
label1.pack()
TBox = Text(root,height=10,width=300,bg="#d3f2ee")
TBox.pack()

p1 = PhotoImage(file = 'miclogo.png')
root.iconphoto(False, p1)

def speaktext():
    engine = pyttsx3.init()
    voice = engine.getProperty("voices")
    engine.setProperty("voices",voice[1].id)

    if not TBox.get("1.0","end-1c"):
        engine.say("Enter some text and then click on speak button ")
        engine.runAndWait()
    else:
        text = TBox.get("1.0","end-1c")
        engine.say(text)
        engine.runAndWait()


myButton = Button(root, text="Speak the entered text",command=speaktext, width="100", pady=15, fg="white", bg="#18aff5", font="bold")
myButton.pack(side = BOTTOM)

root.mainloop()