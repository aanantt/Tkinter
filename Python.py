import tkinter as tk
import pafy as p


root = tk.Tk()
link = tk.StringVar(root)
link.get()
title = tk.StringVar(root)
varTypes = tk.StringVar(root)


def getMedia():
    return p.new(link.get())


def VideoOptionBuilder():
    url = getMedia()
    videos = url.videostreams
    title.set(url.title)
    videotitle = tk.Label(root, text=title.get()).grid(row=2, column=1)
    varTypes.set(videos[0])
    typeMenu = tk.OptionMenu(root, varTypes, *videos)
    typeMenu.grid(row=3, column=1)
    download = tk.Button(root, text="Downloader", command=VideoDownloader).grid(row=4, column=1)


def VideoDownloader():
    url = getMedia()
    videotype = str(varTypes.get()).split(':')[1].split('@')[0]
    best = url.getbest(preftype=videotype)
    best.download()


def AudioOptionBuilder():
    url = getMedia()
    audios = url.audiostreams
    title.set(url.title)
    audiotitle = tk.Label(root, text=title.get()).grid(row=2, column=1, pady=20)
    varTypes.set(audios[0])
    typeMenu = tk.OptionMenu(root, varTypes, *audios)
    typeMenu.grid(row=3, column=1)
    download = tk.Button(root, text="Downloader", command=AudioDownloader).grid(row=4, column=1)


def AudioDownloader():
    url = getMedia()
    audios = url.getbest()
    audios.download()


def show():
    VideoOptionBuilder()
    AudioOptionBuilder()


# AudioOptionBuilder
root.geometry("600x300")
label = tk.Label(root, text=" Enter Your Link Here ").grid(row=0, column=0, padx=10)
entry = tk.Entry(root, width=45, textvariable=link).grid(row=0, column=1, padx=10)
video = tk.Button(root, command=VideoOptionBuilder, text="Get Video").grid(row=1, column=0, pady=10)
audio = tk.Button(root, command=AudioOptionBuilder, text="Get Audio").grid(row=1, column=1, pady=10)
root.mainloop()
