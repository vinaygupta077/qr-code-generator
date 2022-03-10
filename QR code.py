from nturl2path import url2pathname
from tkinter import font
import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *

main = Tk()
main.geometry("500x300")
main.config(background="#92A8D1")
main.resizable(False,False)
main.title("QR Code generator")
main.iconbitmap("C:\\Users\\HP\\OneDrive\\Desktop\\py\\QR\\QR.ico")


def QRgenerate():
        gen = pyqrcode.create(entry_main.get())
        gen.png(entry_main1.get()+".png",scale=20)
        

label = Label(main, text = "Drop your link here : ",fg="Black", font=("Arial",10,font.ITALIC,font.BOLD))
label.place(x=20,y=20)
label.config(background="#92A8D1")

entry_main = Entry(main, bg="white",fg="black",font=("Arial",20,"bold"))
entry_main.place(x=20,y=50)

label1 = Label(main,text="File Name : ",fg="Black", font=("Arial",10,font.ITALIC,font.BOLD))
label1.place(x=20,y=100)
label1.config(background="#92A8D1")

entry_main1 = Entry(main, bg="white",fg="black",font=("Arial",20,"bold"))
entry_main1.place(x=20,y=130)

label2 = Label(main,text="© 2022 Vinay Gupta",fg="black",font=("Arial",7,font.ITALIC))
label2.place(x=400,y=280)
label2.config(background="#92A8D1")

button = Button(main,text= "Generate QR Code",bg ="Orange",fg = "black",height=2, width=15, borderwidth=5,font =("Arial",10,font.BOLD,font.ITALIC),command=QRgenerate)
button.place(x=20,y=200)

main.mainloop()