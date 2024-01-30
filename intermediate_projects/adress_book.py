from tkinter import *

# initialize

root = Tk()
root.title('AddressBook')
# root.resizable(0, 0)
root.geometry('500x500')
root.config(bg='SlateGray2')
contactlist = [
    ['Rui', '0733000000'],
    ['Mikey', '0733004300'],
    ['Drew', '0733080090']
]

# variables
Name = StringVar()
Number = StringVar()

# create frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12, width=20)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)
select.config(font='arial 12 bold', fg='blue')


# function to get select value
def Selected():
    return int(select.curselection()[0])


# func to add new contact
def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()


# fun to edit existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def Edit():
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()


# to delete selected contact
def Delete():
    del contactlist[Selected()]
    Select_set()


# to view selected contact(first select then click on view button)
def View():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


# exit, empty name and number field funcs
def Exit():
    root.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


Select_set()


def RESET():
    Name.set('')
    Number.set('')


# define buttons labels and entry widget

Label(root, text='Name: ', font='arial 12 bold', bg='SlateGray2').place(x=30,y=20)
Entry(root, textvariable=Name).place(x=130,y=20)
Label(root, text='Number: ', font='arial 12 bold', bg='SlateGray2').place(x=30,y=70)
Entry(root, textvariable=Number).place(x=130,y=70)
Button(root, text='ADD', font='arial 12 bold', command=AddContact).place(x=50,y=110)
Button(root, text='VIEW', font='arial 12 bold', command=View).place(x=50, y=160)
Button(root, text='DELETE', font='arial 12 bold', command=Delete).place(x=50,y=210)
Button(root, text='EDIT', font='arial 12 bold', command=Edit).place(x=50,y=260)
Button(root, text='RESET', font='arial 12 bold', command=RESET).place(x=50,y=320)
Button(root, text='EXIT', font='arial 12 bold',command=Exit).place(x=50, y=380)
Label(root, text='By h41pa', font='arial 13 bold', bg='SlateGray2').place(x=200, y=450)
# loop
root.mainloop()
