
from tkinter import *

root = Tk()
root.title("blabla")
root.geometry('400x400')
entry = Entry(root, width=20)
entry.pack()
def dowhatever():
    get_var = entry.get()
    result = '#' * int(get_var) + str(get_var)
    entry.delete(0,END)
    entry.insert(0, result)


Button(root, text='DOne', command=dowhatever).pack()



root.mainloop()