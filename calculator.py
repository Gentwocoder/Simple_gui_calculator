# import all modules
import tkinter as tk
from tkinter import *

# initialize screen
window = tk.Tk()

# window.geometry("500x650")
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
entry = Entry(font=11, width=33, textvariable=e1)

# Empty labels to give space between the input and the buttons
empty_label = Label(background="black")
empty_label1 = Label(background="black")

# Create the buttons
btn1 = Button(text="1", font=6, bg="red", command=lambda:press(1), width=6)
btn2 = Button(text="2", font=6, bg="red", command=lambda:press(2), width=6)
btn3 = Button(text="3", font=6, bg="red", command=lambda:press(3), width=6)
btn4 = Button(text="4", font=6, bg="red", command=lambda:press(4), width=6)
btn5 = Button(text="5", font=6, bg="red", command=lambda:press(5), width=6)
btn6 = Button(text="6", font=6, bg="red", command=lambda:press(6), width=6)
btn7 = Button(text="7", font=6, bg="red", command=lambda:press(7), width=6)
btn8 = Button(text="8", font=6, bg="red", command=lambda:press(8), width=6)
btn9 = Button(text="9", font=6, bg="red", command=lambda:press(9), width=6)
btn10 = Button(text="0", font=6, bg="red", command=lambda:press(0), width=6)
btn11 = Button(text="+", font=6, bg="red", command=lambda:press("+"), width=6)
btn12 = Button(text="-", font=6, bg="red", command=lambda:press("-"), width=6)
btn13 = Button(text="x", font=6, bg="red", command=lambda:press("*"), width=6)
btn14 = Button(text="/", font=6, bg="red", command=lambda:press("/"), width=6)
btn18 = Button(text=".", font=6, bg="red", command=lambda:press("."), width=6)
btn17 = Button(text="mod", font=6, bg="red", command=lambda:press("%"), width=6)
btn15 = Button(text="=", font=6, bg="red", command=equalpress, width=6)
btn16 = Button(text="C", font=6, bg="red", command=clear, width=6)

empty_label.grid(row=0 ,column=0)
entry.grid(row=1, column=0, columnspan=4)
empty_label1.grid(row=2, column=0)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=4, column=0)
btn5.grid(row=4, column=1)
btn6.grid(row=4, column=2)
btn7.grid(row=5, column=0)
btn8.grid(row=5, column=1)
btn9.grid(row=5, column=2)
btn10.grid(row=6, column=1)
btn11.grid(row=3, column=3)
btn12.grid(row=4, column=3)
btn13.grid(row=5, column=3)
btn14.grid(row=6, column=3)
btn15.grid(row=6, column=2)
btn16.grid(row=7, column=1)
btn17.grid(row=7, column=2)
btn18.grid(row=6, column=0)

window.mainloop()

