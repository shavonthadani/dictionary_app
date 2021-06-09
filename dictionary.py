from tkinter import *
from PIL import Image, ImageTk
import dictionaryBackend
from gifObject import ImageLabel
import threading


def loadDef():
    lbl_word['text'], lbl_def['text'] = dictionaryBackend.translate(input.get())
    lbl_def_image.lift()
    lbl_word.lift()
    lbl_def.lift()
    lbl_prompt.lift()
    txt_input.delete(0,END)
    txt_input.lift()



def searchDef(event):
    if '\'' not in input.get() and '"' not in input.get():
        global gif
        gif = ImageLabel(window)
        gif.load('page_flip.gif')
        load_def_thread = threading.Thread(target=loadDef)
        load_def_thread.start()
        gif.grid(row=0,column=0)



def createGUI():
    global window
    window =Tk()
    window.wm_title("Dictionary")

    window.bind('<Return>',searchDef)

    def_pic = ImageTk.PhotoImage(Image.open("page.png"))
    global lbl_def_image
    lbl_def_image = Label(image=def_pic)
    lbl_def_image.image = def_pic
    lbl_def_image.grid(row=0,column=0)



    start_pic = ImageTk.PhotoImage(Image.open("start_pic.png"))
    global lbl_image
    lbl_image = Label(image=start_pic)
    lbl_image.image = start_pic
    lbl_image.grid(row=0,column=0)
    start_pic = ImageTk.PhotoImage(Image.open("start_pic.png"))
    lbl_image = Label(image=start_pic)
    lbl_image.image = start_pic
    lbl_image.grid(row=0,column=0)

    global input
    input = StringVar()
    global lbl_prompt
    lbl_prompt = Label(text = "Enter a word:",bg = "#90D395")
    lbl_prompt.place(x=250,y=53)
    global txt_input
    txt_input = Entry(textvariable=input)
    txt_input.place(x=350,y=50)
    input = StringVar()
    lbl_prompt = Label(text = "Enter a word:",bg = "#90D395")
    lbl_prompt.place(x=250,y=53)
    txt_input = Entry(textvariable=input)
    txt_input.place(x=350,y=50)

    #output variables
    global lbl_word
    lbl_word = Label(font="helvetica 20", wraplength=175, justify="left")
    lbl_word.place(x=220,y=200)
    lbl_word.lower()

    global lbl_def
    lbl_def = Label(font="helvetica 10", wraplength=175, justify="left")
    lbl_def.place(x=420,y=200)
    lbl_def.lower()

    window.mainloop()
createGUI()
