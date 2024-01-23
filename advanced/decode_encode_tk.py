from tkinter import *
import base64

root = Tk()

root.geometry('500x300')
# root.resizable(0,0)
root.title("Message Encode and Decode")
root.config(bg='blue')
# Label

Label(root, text='--- ENCODE DECODE ---', fg='red', font='arial 20 bold').pack()
Label(root, text='By h41pa', fg='green', font='arial 18 bold').pack(side=BOTTOM)

# define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#######define function#####

# function to encode

def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)


def Mode():
    if mode.get() == 'e':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == 'd':
        Result.set(Decode(private_key.get(), Text.get()))

    else:
        Result.set('Invalid Mode')


def Exit():
    root.destroy()


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


#################### Label and Button #############

# Message
Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

# key
Label(root, text='KEY', font='arial 12 bold').place(x=60, y=90)
Entry(root, textvariable=private_key, bg='ghost white', font='arial 12').place(x=290, y=90)

# mode
Label(root, text='MODE(e-necode, d-decode)', font='arial 12 bold',).place(x=60, y=120)
Entry(root, textvariable=mode, font='arial 12', bg='ghost white').place(x=290, y=120)

#result
Entry(root, font='arial 12 bold', textvariable=Result, bg='ghost white').place(x=290, y=150)

######result button
Button(root, font='arial 10 bold', text='RESULT', padx=2, bg='LightGray', command=Mode).place(x=60, y=150)

#reset button

Button(root, font='arial 11 bold', text='RESET',width=6, command= Reset, bg='LimeGreen', padx=2).place(x=80, y=190)

#exit button

Button(root, font='arial 11 bold', text='EXIT!', width=6, command=Exit, bg='OrangeRed',padx=2, pady=2).place(x=180, y=190)

root.mainloop()
