from tkinter import *
from PIL import Image, ImageTk
import dictionaryBackend
from gifObject import ImageLabel
import threading
import re
import readonlyText


def loadDef():
    dic_word = dictionaryBackend.translate(input.get())
    lbl_word['text'] = dic_word[0]
    try:
        txt_def.delete("1.0","end")
    except:
        pass
    txt_def.insert(END,dic_word[1])
    dictionaryBackend.closeConn()
    dictionaryBackend.closeConn()
    lbl_def_image.lift()
    lbl_word.lift()
    txt_def.lift()
    scrollbar.lift()
    lbl_prompt.lift()
    ent_input.delete(0,END)
    ent_input.lift()



def searchDef(event):
    if re.search(r"^[a-zA-Z ]+$",input.get()) != None:
        load_def_thread = threading.Thread(target=loadDef)
        load_def_thread.start()
        gif.lift()




def createGUI():
    global window
    window =Tk()
    window.wm_title("Dictionary")

    global gif
    gif = ImageLabel(window)
    gif.load('page_flip.gif')
    gif.grid(row=0,column=0)



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
    global ent_input
    ent_input = Entry(textvariable=input)
    ent_input.place(x=350,y=50)
    input = StringVar()
    lbl_prompt = Label(text = "Enter a word:",bg = "#90D395")
    lbl_prompt.place(x=250,y=53)
    ent_input = Entry(textvariable=input)
    ent_input.place(x=350,y=50)

    #output variables
    global lbl_word
    lbl_word = Label(font="helvetica 20", wraplength=175, justify="left")
    lbl_word.place(x=220,y=200)
    lbl_word.lower()

    global txt_def
    txt_def = readonlyText.ROText(font="helvetica 10", height=20, width=30, wrap= WORD, borderwidth=0)
    txt_def.bind("<Key>", lambda e: "break")
    txt_def.place(x=420,y=200)
    global scrollbar
    scrollbar = Scrollbar(window)
    scrollbar.place(x=600,y=200)
    txt_def.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=txt_def.yview)
    scrollbar.lower()
    txt_def.lower()

    window.bind('<Return>',searchDef)
    window.mainloop()
createGUI()
