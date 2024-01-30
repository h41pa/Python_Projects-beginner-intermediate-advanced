from tkinter import *
from pytube import YouTube
import re
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('Youtube Downloader !')

# Label
Label(root, text='Youtube Video Downloader', fg='red', font='arial 20 bold').pack()
Label(root, text='h41pa', font='arial 16 bold').pack(side=BOTTOM)
Label(root, text='Paste your link here:', font='arial 16 bold').pack()

# variable
link = StringVar()

# Entry
Entry(root, textvariable=link, width=70, bg='yellow').place(x=32, y=90)


# function to download
def Downloader():
    if not link.get():
        Label(root, text='Please enter a  valid youtube link !!!', font='arial 15 bold', fg='red', bg='yellow').place(x=90, y=120)
    else:
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        Label(root, text='Video downloaded !', font='arial 17 bold', fg='blue', bg='RosyBrown1').place(x=150, y=200)


def Exit():
    root.destroy()


# download button and reset
Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=3, command=Downloader).place(x=180,
                                                                                                            y=150)
Button(root, text='Exit', command=Exit, bg='OrangeRed', width=6, font='arial 14 bold').pack(side=BOTTOM)

# main loop
root.mainloop()
