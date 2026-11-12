from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

r = Tk()
r.geometry("400x300")
r. title("main")

upload = Image.open("app_img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(r, image=image, bg="light blue")
label.place(x=180, y=20)

l1 = Label(
    r,text="Hey User! Welcome to Denomination Counter Application",bg="light blue"
)
label.place(relx=0.5, y=340, anchoor=CENTER)

def msg():
    msgbox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"

    ) 
    if msgbox =="ok":
        pass