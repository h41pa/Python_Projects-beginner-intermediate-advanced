from tkinter import *
from gtts import gTTS
from playsound import playsound

#   Initialized window

root = Tk()
root.title('Text to Speech')
root.geometry('350x350')
root.resizable(0, 0)
root.config(bg='ghost white')

#   heading (bottom also)
Label(root, text='TEXT_TO_SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='h41pa', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

#   Label
Label(root, text='Entry Text: ', font='arial 12 bold', bg='white smoke').place(x=20, y=60)

#   variable text
Text = StringVar()

#  Entry label
Entry(root, textvariable=Text, width=50).place(x=20, y=100)


# def functions

def Text_To_Speech():
    Message = Text.get()
    speech = gTTS(text=Message)
    speech.save('textspeech.mp3')
    playsound('textspeech.mp3')


def Exit():
    root.destroy()


def Reset():
    Text.set('')


#Button
Button(root, text='PLAY', command=Text_To_Speech, font='arial 15 bold', width=4).place(x=25, y=140)
Button(root, text='EXIT', command=Exit, font='arial 15 bold', bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', command=Reset, font='arial 15 bold').place(x=175, y=140)

#   infinite loop to run program
root.mainloop()
playsound('textspeech.mp3')