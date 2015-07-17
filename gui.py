# coding: utf-8
"""
GUI layout for part 3 of project
"""

from tkinter import *
import tkinter.messagebox
import tkinter.colorchooser

IMAGE = "./Games/boy.png"

root = Tk()
root.title("Network")


def colorchoice():
    """
    Tk app to choose colour
    """
    chosen_colour = tkinter.colorchooser.askcolor(parent=root)
    return chosen_colour[1]


def changefgto(label_widget):
    """
    Changes foreground of label to a chosen colour
    :param label_widget: Label tkinter App
    """
    color = colorchoice()
    label_widget["fg"] = color

CONTEXT_MENU_COLOR = "black"

"""
label = Label(root, text="This is a colour change test", font=("ComicSans", 20))
label.pack()

bye = Button(root, text="Exit", command=root.destroy)
bye.pack(side=BOTTOM)

change = Button(root, text="Change colour", command=lambda label_widget=label: changefgto(label_widget))
change.pack()

root.mainloop()
"""
topFrame = Frame(root)
topFrame.pack(side=TOP, expand="yes", fill=BOTH)

# image = PhotoImage(file=IMAGE)
# imageLabel = Label(topFrame, image=image)
# imageLabel.pack(side=LEFT)

canvas = Canvas(topFrame, bd=4, relief=SUNKEN, width=600, height=300)
canvas.pack(side=LEFT, expand="yes", fill=BOTH)

infoFrame = LabelFrame(topFrame, text="Node information", labelanchor="n", font="Calibri 20 italic", bd=0, relief=SUNKEN, width=300)
infoFrame.pack_propagate(0)
infoFrame.pack(side=RIGHT, fill=Y)
b = Label(infoFrame, text="Steps")
b.pack()


menu = Frame(root, relief=GROOVE, bg="lightblue", bd=6)
menu.pack(side=BOTTOM, expand="yes", fill=BOTH)

layout = LabelFrame(menu, text="Network Layout", font="courier 10 bold", labelanchor="n", padx=5, bd=4, relief=RIDGE, fg=CONTEXT_MENU_COLOR)
layout.pack(side=LEFT, fill=BOTH)
layoutListe = Listbox(layout, activestyle="dotbox", height=3)
layoutListe.insert(1, "Circular")
layoutListe.insert(2, "Shell")
layoutListe.insert(3, "Random")
layoutListe.pack()

nodeWidth = LabelFrame(menu, text = "Node Width", font="courier 10 bold", labelanchor="n", padx=5, bd=4, relief=RIDGE, fg=CONTEXT_MENU_COLOR)
nodeWidth.pack(side=LEFT, fill=BOTH)
nodeScale = Scale(nodeWidth, relief=SOLID, troughcolor="white", from_=1, to=50) # Comment on met par défault ?
nodeScale.pack(expand="yes", fill=BOTH)

edgeWidth = LabelFrame(menu, text = "Edge Width", font="courier 10 bold", labelanchor="n", padx=5, bd=4, relief=RIDGE, fg=CONTEXT_MENU_COLOR)
edgeWidth.pack(side=LEFT, fill=BOTH)
edgeScale = Scale(edgeWidth, relief=SOLID, troughcolor="white", from_=1, to=10) # Comment on met par défault ?
edgeScale.pack(expand="yes", fill=BOTH)

delay = LabelFrame(menu, text = "Step Delay", font="courier 10 bold", labelanchor="n", padx=5, bd=4, relief=RIDGE, fg=CONTEXT_MENU_COLOR)
delay.pack(side=LEFT, fill=BOTH)
delayScale = Scale(delay, relief=SOLID, troughcolor="white", from_=0, to=3) # Comment on met par défault ?
delayScale.pack(expand="yes", fill=BOTH)

selection = LabelFrame(menu, text="Selection Policy", font="courier 10 bold", labelanchor="n", padx=5, bd=4, relief=RIDGE, fg=CONTEXT_MENU_COLOR)
selection.pack(side=LEFT, fill=BOTH)
selectionListe = Listbox(selection, activestyle="dotbox", height=3)
selectionListe.insert(1, "Random")
selectionListe.pack()

modifType = LabelFrame(menu, text="Error Function", font="courier 10 bold", labelanchor="n", padx=5, bd=4, relief=RIDGE, fg=CONTEXT_MENU_COLOR)
modifType.pack(side=LEFT, fill=BOTH)
modifTypeListe = Listbox(modifType, activestyle="dotbox", height=3)
modifTypeListe.insert(1, "None")
modifTypeListe.insert(2, "Incremental")
modifTypeListe.insert(3, "BitFlip")
modifTypeListe.pack()
errorProba = Label(modifType, text="--Error probability--", pady=2, height=3)
errorProba.pack()
modifProbaScale = Scale(modifType, relief=SOLID, troughcolor="white", from_=0, to=1.0, resolution=0.1, orient=HORIZONTAL) # par default?
modifProbaScale.pack(side=TOP)

updatePolicy = LabelFrame(menu, text="Update Policy", font="courier 10 bold", labelanchor="n", padx=5, bd=4, relief=RIDGE, fg=CONTEXT_MENU_COLOR)
updatePolicy.pack(side=LEFT,  fill=BOTH)
updatePolicyListe = Listbox(updatePolicy, activestyle="dotbox", height=3)
updatePolicyListe.insert(1, "Random")
updatePolicyListe.insert(2, "Stable")
updatePolicyListe.insert(3, "Rewrite")
updatePolicyListe.pack()

ButtonFrame = LabelFrame(menu, text="       Menu       ", font="courier 10 bold", labelanchor="n", padx=5, bd=4, relief=RIDGE, fg=CONTEXT_MENU_COLOR)
ButtonFrame.pack(side=LEFT, expand="yes", fill=BOTH)
newNode = Button(ButtonFrame, text="New Node", width=14, bd=5)
newNode.pack(expand="yes")
propagate= Button(ButtonFrame, text="Propagate", width=14, bd=5)
propagate.pack(expand="yes")
run = Button(ButtonFrame, text="Run", width=14, bd=5)
run.pack(expand="yes")
reset = Button(ButtonFrame, text="Reset Steps", width=14, bd=5)
reset.pack(expand="yes")

root.mainloop()