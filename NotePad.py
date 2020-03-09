from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfilename

root = Tk()
root.title("NotePad")


def Open():
    blank.delete("1.0", END)
    file = askopenfile(mode='r', filetypes=[('text files', '*.txt')])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)


def save():
    notepad = blank.get("1.0", "end-1c")
    file = asksaveasfilename(title="Save", filetypes=[('text files', '*.txt')])
    with open(file, 'w') as data:
        data.write(notepad)


menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar )
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=Open)
filemenu.add_command(label="Save", command=save )
filemenu.add_command(label="Exit", command=root.quit)
blank = Text(root, font=("arail", 10))
blank.pack()
root.mainloop()
