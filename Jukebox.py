import sqlite3
import tkinter

conn = sqlite3.connect("music.sqlite")

<<<<<<< HEAD

class Scrollbox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)
    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky="nsw", rowspan=rowspan)
        self["yscrollcommand"]=self.scrollbar.set

=======
>>>>>>> parent of 05c5ae4 (We are creating a class that includes it's own scrollbar. It will inherit most of it's functionality.)
mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry("1024x768")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# Labels
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# Artist Listbox
artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# Album Listbox
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# Song Listbox
songLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an album",))
songList = tkinter.Listbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# Main loop
mainWindow.mainloop()
print("Closing db connection")
conn.close()