#dictionary.py
#Shavon Thadani
#script contains the controller and dictionary classes and creates an instance of them to create a dictionary
#06/17/2021
from tkinter import *
from model import Model
import re
import threading
from PIL import Image, ImageTk
from gifObject import ImageLabel
import readonlyText
class View(Tk):

    def __init__(self, controller):
        #constructor
        self.controller = controller
        super().__init__()
        self.bind('<Return>',self.controller.on_return_key)
        self.wm_title("Dictionary")
        self.input = StringVar()
    #create page fliping gif for loading screen
    def _create_gif(self):
        self.gif = ImageLabel(self)
        self.gif.load('page_flip.gif')
        self.gif.grid(row=0,column=0)
    #create the pic for the definition
    def _create_def_pic(self):
        def_pic = ImageTk.PhotoImage(Image.open("page.png"))
        self.lbl_def_image = Label(self, image=def_pic)
        self.lbl_def_image.image = def_pic
        self.lbl_def_image.grid(row=0,column=0)
    #create the starting pic
    def _create_start_pic(self):
        start_pic = ImageTk.PhotoImage(Image.open("start_pic.png"))
        self.lbl_start_image = Label(self, image=start_pic)
        self.lbl_start_image.image = start_pic
        self.lbl_start_image.grid(row=0,column=0)
    #create the label to prompt the user to enter a word
    def _create_prompt_label(self):
        self.lbl_prompt = Label(self, text = "Enter a word:",bg = "#90D395")
        self.lbl_prompt.place(x=250,y=53)
    #create the entry box for the user to input a word
    def _create_entry(self):
        self.ent_input = Entry(self, textvariable=self.input)
        self.ent_input.place(x=350,y=50)
    #create the label to display the word in the dictionary
    def _create_word_label(self):
        self.lbl_word = Label(self, font="helvetica 20", wraplength=175, justify="left")
        self.lbl_word.place(x=220,y=200)
        self.lbl_word.lower()
    #create the textbox with scrollbar for the definition
    def _create_txt_with_scroll(self):
        self.txt_def = readonlyText.ROText(self, font="helvetica 10", height=20, width=30, wrap= WORD, borderwidth=0)
        self.txt_def.bind("<Key>", lambda e: "break")
        self.txt_def.place(x=420,y=200)
        self.scrollbar = Scrollbar(self)
        self.scrollbar.place(x=600,y=200)
        self.txt_def.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.txt_def.yview)
        self.scrollbar.lower()
        self.txt_def.lower()
    def main(self):
        self._create_gif()
        self._create_def_pic()
        self._create_start_pic()
        self._create_prompt_label()
        self._create_entry()
        self._create_word_label()
        self._create_txt_with_scroll()
        self.mainloop()

class Controller:
    #constructor
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()
    #thread to retrieve the definition from database and change the position of widgets to display the definition
    def loadDef(self):
        dic_word = self.model.translate(self.view.input.get())
        self.view.lbl_word['text'] = dic_word[0]
        try:
            self.view.txt_def.delete("1.0","end")
        except:
            pass
        self.view.txt_def.insert(END,dic_word[1])
        self.view.lbl_def_image.lift()
        self.view.lbl_word.lift()
        self.view.txt_def.lift()
        self.view.scrollbar.lift()
        self.view.lbl_prompt.lift()
        self.view.ent_input.delete(0,END)
        self.view.ent_input.lift()
    #method gets executed by the return key event. If the word contains of only alphabet or spaces, it will start a thread. It will also display the gif as a loading screen.
    def on_return_key(self, event):
        if re.search(r"^[a-zA-Z ]+$",self.view.input.get()) != None:
            load_def_thread = threading.Thread(target=self.loadDef)
            load_def_thread.start()
            self.view.gif.lift()
if __name__ == '__main__':
    dictionary = Controller()
    dictionary.main()
