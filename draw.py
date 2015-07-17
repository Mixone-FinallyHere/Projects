# coding: utf-8 
# !usr\bin\python
"""
File description.
"""
__author__ = 'Miguel Terol Espino - mteroles'
__date__ = '05/02/2015'

from tkinter import *
import tkinter.colorchooser

"""
def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return

master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<B1-Motion>', motion)
msg.pack()
mainloop()
"""
canvas_width = 500
canvas_height = 500
SIZE = 4
COLOUR = "black"


def colorchoice():
    """
    Tk app to choose colour
    """
    chosen_colour = tkinter.colorchooser.askcolor(parent=master)
    return chosen_colour[1]


def paint(event):
    x1, y1 = (event.x - SIZE), (event.y - SIZE)
    x2, y2 = (event.x + SIZE), (event.y + SIZE)
    canvas.create_oval(x1, y1, x2, y2, fill=COLOUR, outline=COLOUR)


def change_size():
    global SIZE
    SIZE = edgeScale.get()


def change_colour():
    global COLOUR
    COLOUR = colorchoice()


master = Tk()
master.title("~~~~Paint~~~~ \Mixone Edition/")

menu = LabelFrame(master, relief=RIDGE, bd=6, text="Options", labelanchor="n", font="chiller 25")
menu.pack(side=BOTTOM, expand="yes", fill=BOTH)

canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack(expand=YES, fill=BOTH)
canvas.bind('<B1-Motion>', paint)

brush_size = LabelFrame(menu, text="Brush Size", font="courier 10 bold", relief=RIDGE, fg="black", labelanchor="n")
brush_size.pack(side=LEFT, fill=Y)
edgeScale = Scale(brush_size, troughcolor="white", from_=1, to=10, orient=HORIZONTAL)
edgeScale.pack(side=TOP, fill=X)
scale_button = Button(brush_size, text="Change brush size", command=change_size, font="courier 8 italic")
scale_button.pack(side=BOTTOM)

brush_colour = LabelFrame(menu, text="Brush colour", font="courier 10 bold", relief=RIDGE, fg="black", labelanchor="n")
brush_colour.pack(side=RIGHT, fill=Y)
colour_button = Button(brush_colour, text="Change brush colour",
                       command=change_colour, font="courier 8 italic", height=4)
colour_button.pack()

message = Label(master, text="press and drag the mouse to draw", font="arial 8 italic")
message.pack(side=BOTTOM)

master.mainloop()
