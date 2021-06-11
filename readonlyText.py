from tkinter import *

# This is the list of all default command in the "Text" tag that modify the text
commandsToRemove = (
"<Control-Key-h>",
"<Meta-Key-Delete>",
"<Meta-Key-BackSpace>",
"<Meta-Key-d>",
"<Meta-Key-b>",
"<<Redo>>",
"<<Undo>>",
"<Control-Key-t>",
"<Control-Key-o>",
"<Control-Key-k>",
"<Control-Key-d>",
"<Key>",
"<Key-Insert>",
"<<PasteSelection>>",
"<<Clear>>",
"<<Paste>>",
"<<Cut>>",
"<Key-BackSpace>",
"<Key-Delete>",
"<Key-Return>",
"<Control-Key-i>",
"<Key-Tab>",
"<Shift-Key-Tab>"
)


class ROText(Text):
    tagInit = False

    def init_tag(self):
        """
        Just go through all binding for the Text widget.
        If the command is allowed, recopy it in the ROText binding table.
        """
        for key in self.bind_class("Text"):
            if key not in commandsToRemove:
                command = self.bind_class("Text", key)
                self.bind_class("ROText", key, command)
        ROText.tagInit = True


    def __init__(self, *args, **kwords):
        Text.__init__(self, *args, **kwords)
        if not ROText.tagInit:
            self.init_tag()

        # Create a new binding table list, replace the default Text binding table by the ROText one
        bindTags = tuple(tag if tag!="Text" else "ROText" for tag in self.bindtags())
        self.bindtags(bindTags)

#text = ROText()

#text.insert("1.0", """A long text with several
#lines
#in it""")


#text.pack()

#text.mainloop()
