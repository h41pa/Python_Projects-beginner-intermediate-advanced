from tkinter import *
import random, string
import pyperclip

#  initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Password Generator !!!')
root.config(bg='white')
# variables
pass_len = IntVar()
pass_str = StringVar()

#   heading
Label(root, text='PASSWORD GENERATOR', font='arial 15 bold', fg='red').pack()
Label(root, text='By h41pa', font='arial 14 italic bold').pack(side=BOTTOM)

#   select password length
Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
Spinbox(root, from_=6, to=12, textvariable=pass_len, width=15).pack()


#   define functions

def Generator():
    chars = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits)
    password = ''
    for i in range(pass_len.get()):
        password += random.choice(chars)
    pass_str.set(password)


def Exit():
    root.destroy()


def Copy():
    pyperclip.copy(pass_str.get())


#   button generate
Button(root, text='GENERATE PASSWORD', command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()

#   button copy
Button(root, text='COPY TO CLIPBOARD', command=Copy).pack(pady=5)

# exit button
Button(root, text='Exit!', command=Exit, font='arial 12 bold', bg='red', width=4).pack(side=BOTTOM)
#   loop to run program
root.mainloop()
