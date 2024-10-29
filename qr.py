import qrcode
from tkinter import *
from tkinter import filedialog

def browse():
    
     direccc =filedialog.askdirectory(title="Save the video ") 
     directory.delete(0,END)
     directory.insert(0,direccc)
     
def generate():
    link1=link.get()
    folder=directory.get()
    qraaa=qrcode.make(link1)
    qraaa.save(folder+"\\qrcode.png")
    
    
screen=Tk()
screen.geometry("350x400")
screen.title("Qr code generator")
titre=Label(screen,text="Qrcode Genrator ",font="arial 20 bold")
titre.pack(pady=10)
dd=Label(screen,text="Directory folder",font="arial 14 bold")
dd.place(x=80,y=90)
directory=Entry(screen,font="georgia 15")
directory.place(x=0,y=125)
aa=Label(screen,text="Link ",font="arial 14 bold ")
aa.place(x=80,y=175)
directory_btn=Button(screen,text="browse",font="georgia 13",bg="grey",fg="black",command=browse)
directory_btn.place(x=255,y=125)
link=Entry(screen,font="georgia 15")
link.place(x=0,y=205)
generate_btn=Button(screen,text="Generate ",font="georgia 13",bg="grey",fg="black",command=generate)
generate_btn.place(x=255,y=205)

screen.mainloop()