
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *
from  ViewBooks import *

# Add your own database name and password here to reflect in the code
mypass = 'yourpass'
mydatabase = 'libraryproject'

con = pymysql.connect(host='localhost', user='root', password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title('Library Tk')
root.minsize(width=400,height=400)
root.geometry('600x500')

# Take n greater than 0.25 and less than 5
same = True
n = 0.25

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.LANCZOS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)
Canvas1.config(bg='blue', width= newImageSizeWidth, height= newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="  Welcome to \n Test Library", bg='black', fg='white', font='Courier 15 bold')
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text='Add Books Details', bg='black', fg='white', font='Arial 12', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text='Delete Book', bg='black', fg='white', font='Arial 12', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root, text='View Book List', bg='black', fg='white', font=('Arial',12), command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text='Issue Book to Student', bg='black', fg='white', font='Arial 12', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text='Return Book', bg='black', fg='white', font='Arial 12', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text='Exit', bg='red', fg='black', font='Arial 12', command=root.destroy)
btn6.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.1)
root.mainloop()