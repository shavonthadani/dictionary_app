from tkinter import *
from PIL import Image, ImageTk

import time
import os
from gifObject import ImageLabel


def searchDef(event):
        lbl_image.lower()
        lbl_prompt.lower()
        txt_input.lower()
        gif.lift()
        
        gif.lower()
        lbl_word.lift()
        lbl_def.lift()

def createGUI():

    window =Tk()
    window.wm_title("Dictionary")


    window.bind('<Return>',searchDef)

    def_pic = ImageTk.PhotoImage(Image.open("page.png"))
    global lbl_def_image
    lbl_def_image = Label(image=def_pic)
    lbl_def_image.image = def_pic
    lbl_def_image.grid(row=0,column=0)

    global gif
    gif = ImageLabel(window)
    gif.load('page_flip.gif')
    gif.grid(row=0,column=0)

    start_pic = ImageTk.PhotoImage(Image.open("start_pic.png"))
    global lbl_image
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

    #output
    global lbl_word
    lbl_word = Label(text = "WORD another word more words lots of words blah blah", font="helvetica 20", wraplength=175, justify="left")
    lbl_word.place(x=220,y=200)
    lbl_word.lower()

    global lbl_def
    lbl_def = Label(text="This is the definition blah blah blah asdfasdfasdfasdfasdfa", font="helvetica 15", wraplength=175, justify="left")
    lbl_def.place(x=420,y=200)
    lbl_def.lower()


    window.mainloop()
createGUI()
