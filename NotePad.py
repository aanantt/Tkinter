import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename

root = tk.Tk()
root.title("NotePad")


def Open(event=None):
    blank.delete("1.0", tk.END)
    file = askopenfile(mode='r', filetypes=[('text files', '*.txt')])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)


def save(event=None):
    notepad = blank.get("1.0", "end-1c")
    file = asksaveasfilename(title="Save", filetypes=[('text files', '*.txt')])
    try:
        with open(file, 'w') as data:
            data.write(notepad)
    except (FileNotFoundError, TypeError) as f:
        pass


menubar = tk.Menu(root)
root.config(menu=menubar)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=Open)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Exit", command=root.quit)
blank = tk.Text(root, font=("arail", 10))
blank.pack()
root.bind("<Control-o>", Open)
root.bind("<Control-s>", save)
root.mainloop()
