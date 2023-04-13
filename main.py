import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import Image
#

#import cv2
#import matplotlib.pyplot as plt

import tkinter as tk
# from tkinter import ttk
#from PIL import Image


root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")


def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    # convert height into meter
    m = h / 100
    bmi = round(float(w / m ** 2), 1)
   # print(bmi)
    label1.config(text=bmi)

    #you can change value

    if bmi<=18.5:
        lable2.config(text="Underweight!")
        lable3.config(text="you have lower weight than normal body!.")

    elif bmi > 18.5 and bmi <25:
        lable2.config(text="Normal!")
        lable3.config(text="it indicates that you are healthy!.")
    elif bmi>25 and bmi <30:
        lable2.config(text="OverWeight!")
        lable3.config(text="It indicates that a person is\n slightly overweight! \n A doctor may advise  to lose some \n weight for health.")

    else:
        lable2.config(text="Obes!")
        lable3.config(text="Health may be at risk, if thay do not \n lose weight!.")




# Icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# Top
top = PhotoImage(file="top.png")
top_image = Label(root, image=top, bg="#f0f1f5")
top_image.place(x=-10, y=-10)

# bottom boxes
Label(root, width=72, height=18, bg="#264f58" ).pack(side=BOTTOM)

# two boxes
box = PhotoImage(file="box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# scale
scale = PhotoImage(file="scale.png")
Label(root, image=scale, bg="#264f58").place(x=20, y=310)

#level man
man = PhotoImage(file="man.png")
Label(root, image=man, bg="#264f58").place(x=80, y=410)



#image = Image.open('bg1.png')
#new_image = image.resize((400, 400))
#new_image.save('image_400.jpg')
#Label(root, image=image_400.jpg).place(x=100, y=310)

# ##########################    Slider 01 ###########################

current_value = tkinter.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    Height.set(get_current_value())

#    img = (Image.open("man.png"))
#    resized_image = img.resize((50,10+size))
#    photo2 = ImageTK.PhotoImage(resized_image)
#    mealevel.config(image=photo2)
#    mealevel.image=photo2

# Command to change bg color of scale

Label(root,text="Height - CM" ,font="arial 15 bold",bg="#fff",fg="#264f58").place(x=80,y=120)


style = ttk.Style()
style.configure("TScale", bg="white")
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed,
                   variable=current_value).place(x=80, y=250)

#####################################################################


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    Slider 02  @@@@@@@@@@@@@@@@@@@@@@@@@@@


current_value2 = tkinter.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_changed(event):
    Weight.set(get_current_value2())


# Command to change bg color of scale
Label(root,text="Weight - KG" ,font="arial 15 bold",bg="#fff",fg="#264f58").place(x=300,y=120)
style2 = ttk.Style()
style2.configure("TScale", bg="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed,
                    variable=current_value2).place(x=300, y=250)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Entry box
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

#bg
image = PhotoImage(file="bg123.png")
#bgImage=cv2.imread("bg1.png")
#img_75 = cv2.resize(bgImage, None, fx = 0.75, fy = 0.75)
#cv2.resize(bgImage, (300,300))
Label(root, image=image,bg="#264f58" ).place(x=120, y=380)


# level
mealevel = Label(root, bg="#264f58").place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=320, y=340)

label1 = Label(root, font="arial 60 bold", bg="#264f58", fg="#fff")
label1.place(x=125, y=305)

lable2 = Label(root,font="arial 20 bold",bg="#264f58",fg="#fff")
lable2.place(x=280,y=400)

lable3 = Label(root,font="arial 10 bold",bg="#264f58",fg="#fff")
lable3.place(x=200,y=450)



Label(root,text="ALL AUTHORITY! 2023" ,font="arial 10 bold",fg="#264f58").place(x=200,y=530)
Label(root,text="Deverlop By Sehan Chathurange" ,font="arial 10 bold",bg="#264f58",fg="#fff").place(x=200,y=550)


root.mainloop()
