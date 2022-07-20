# import all modules
import tkinter as tk
from tkinter import *

# initialize screen
window = tk.Tk()

window.geometry("500x650")
window.config(bg="black")
window.resizable(width=False, height=False)
window.title("Simple calculator")

# globally declare the expression variable
expression = ""

def press(num):
    global expression
    expression += str(num)
    e1.set(expression)

# function for the equals button
def equalpress():
    try:
 
        global expression
        total = str(eval(expression))
 
        e1.set(total)
        expression = ""
    except:
        e1.set(" error ")
        expression = ""

# function to clear input
def clear():
    global expression
    expression = ""
    e1.set("")

# def reset_all():
#     entry.delete(0, 'end')

e1 = StringVar()

# This is for the input
entry = Entry(font=11, width=25, justify="center", textvariable=e1)

# Empty labels to give space between the input and the buttons
empty_label = Label(background="black")
empty_label1 = Label(background="black")
empty_label2 = Label(background="black")
empty_label3 = Label(background="black")
empty_label4 = Label(background="black")
empty_label5 = Label(background="black")

# Create the buttons
btn1 = Button(text="1", font=6, bg="red", command=lambda:press(1))
btn2 = Button(text="2", font=6, bg="red", command=lambda:press(2))
btn3 = Button(text="3", font=6, bg="red", command=lambda:press(3))
btn4 = Button(text="4", font=6, bg="red", command=lambda:press(4))
btn5 = Button(text="5", font=6, bg="red", command=lambda:press(5))
btn6 = Button(text="6", font=6, bg="red", command=lambda:press(6))
btn7 = Button(text="7", font=6, bg="red", command=lambda:press(7))
btn8 = Button(text="8", font=6, bg="red", command=lambda:press(8))
btn9 = Button(text="9", font=6, bg="red", command=lambda:press(9))
btn10 = Button(text="0", font=6, bg="red", command=lambda:press(0))
btn11 = Button(text="+", font=6, bg="red", command=lambda:press("+"))
btn12 = Button(text="-", font=6, bg="red", command=lambda:press("-"))
btn13 = Button(text="x", font=6, bg="red", command=lambda:press("*"))
btn14 = Button(text="/", font=6, bg="red", command=lambda:press("/"))
btn18 = Button(text=".", font=6, bg="red", command=lambda:press("."))
btn17 = Button(text="mod", font=6, bg="red", command=lambda:press("%"))
btn15 = Button(text="=", font=6, bg="red", command=equalpress)
btn16 = Button(text="C", font=6, bg="red", command=clear)

empty_label.pack()
entry.pack()
empty_label1.pack()
empty_label2.pack()
empty_label3.pack()
empty_label4.pack()
empty_label5.pack()
btn1.place(x=140, y=150)
btn2.place(x=200, y=150)
btn3.place(x=260, y=150)
btn4.place(x=140, y=210)
btn5.place(x=200, y=210)
btn6.place(x=260, y=210)
btn7.place(x=140, y=270)
btn8.place(x=200, y=270)
btn9.place(x=260, y=270)
btn10.place(x=200, y=330)
btn11.place(x=320, y=150)
btn12.place(x=320, y=210)
btn13.place(x=320, y=270)
btn14.place(x=320, y=330)
btn15.place(x=260, y=330)
btn16.place(x=140, y=330)
btn17.place(x=260, y=390)
btn18.place(x=200, y=390)

window.mainloop()
