# Standard Function Basic Calculator 
# Author: Faisal Hossain

#To Do List:
#Finish button_M-RC (double click to clear memory)
#Error handle for empty decimal mathematical attempt
#Error handle when equal signed pressed without mathematical function
#Make the selected number flash when clicked
#Outline (border) the selected  math-opp button when clicked

from tkinter import *
from math import *

root = Tk()
root.minsize(170, 240) #Minium Window Size
root.title("Calculator")

#Reponsive Sizing
for x in range(4):
    root.columnconfigure(x, weight=1)

for y in range(7):
    root.rowconfigure(y, weight=1)

#Entry Box
e = Entry(root, width=15, borderwidth=5)
e.grid(row=0,columnspan=4, padx=10, pady=10, sticky=NSEW)

Mem = 0
Tax = None

#Button Functions
def button_num(number):
    """Button click function for numbers.
    Params: number (int) number representing the button
    Returns: (string) selected number(s) displayed as text on entry box
    """
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_CE():
    """Button click function to clear entry widget.
    Params:
    Returns: clears displayed value in entry box
    """
    e.delete(0,END)
    e.insert(0,str(0))

def button_MR():
    """Button click function to perform addition.
    Params:
    Returns: Clear the memory register (set to zero).
    """    
    global Mem
    e.delete(0,END)
    e.insert(0,str(Mem))


def button_MC(event):
    """Button click function to perform addition.
    Params:
    Returns: Clear the memory register (set to zero).
    """    
    global Mem
    Mem = 0

def button_Mminus():
    """Button click function to perform addition.
    Params:
    Returns: Subtract the displayed value from the memory
    """
    global Mem
    current = float(e.get())
    Mem -= current

def button_Mplus():
    """Button click function to perform addition.
    Params:
    Returns: Add the displayed value to the memory 
    """
    global Mem
    current = float(e.get())
    Mem += current

def button_Tset():
    """Button click function to perform addition.
    Params:
    Returns: Add the displayed value to the memory 
    """
    global Tax
    Tax = float(e.get())

def button_Tplus():
    """Button click function to perform addition.
    Params:
    Returns: Add the displayed value to the memory 
    """
    global Tax
    current = float(e.get())
    e.delete(0,END)
    e.insert(0,str(current+(current*Tax)))
    
def button_add():
    """Button click function to perform addition.
    Params:
    Returns: prepares entry box to add first and second number
    """
    global first_num
    global math
    math = "addition"
    first_num = e.get()
    e.delete(0,END) #change to flash
    
def button_subtract():
    """Button click function to perform subtraction.
    Params:
    Returns: prepares entry box to subtract first and second number
    """
    global first_num
    global math
    math = "subtraction"
    first_num = e.get()
    e.delete(0,END)

def button_multiply():
    """Button click function to perform multiplication.
    Params:
    Returns: prepares entry box to multiply first and second number
    """
    global first_num
    global math
    math = "multiplication"
    first_num = e.get()
    e.delete(0,END)

def button_divide():
    """Button click function to perform division.
    Params:
    Returns: prepares entry box to divide first and second number
    """
    global first_num
    global math
    math = "division"
    first_num = e.get()
    e.delete(0,END)
    
def button_percent():
    """Button click function to perform percentage.
    Params:
    Returns: percentage of the current number displayed on the entry box
    """
    current = float(e.get())
    e.delete(0,END)
    e.insert(0,str(current/100))    

def button_equal():
    """Button click function to equate mathematical operation.
    Params:
    Returns: performs mathematical operation of the first and second number
    """
    second_num = e.get()
    e.delete(0,END)
    
    if math == "addition":
        e.insert(0,str(float(first_num) + float(second_num)))
    elif math == "subtraction":
        e.insert(0,str(float(first_num) - float(second_num)))
    elif math == "multiplication":
        e.insert(0,str(float(first_num) * float(second_num)))
    elif math == "division":
        e.insert(0,str(float(first_num) / float(second_num)))

#Row 1 Buttons
buttonMRC    = Button(root, text="M-RC", padx=6, pady=5, command=button_MR).grid(row=1,column=0, sticky=NSEW)
#buttonMRC.bind('<Double-1>', button_MC)
buttonMminus = Button(root, text="M-", padx=15, pady=5, command=button_Mminus).grid(row=1,column=1, sticky=NSEW)
buttonMplus  = Button(root, text="M+", padx=15, pady=5, command=button_Mplus).grid(row=1,column=2, sticky=NSEW)
buttonCE     = Button(root, text="CE", padx=14, pady=5, command=button_CE, highlightbackground="#AC8D9F").grid(row=1,column=3, sticky=NSEW)

#Row 2 Buttons
buttonTaxset  = Button(root, text="TAX", padx=7, pady=5, command=button_Tset, highlightbackground="#4C897F").grid(row=2,column=0, sticky=NSEW)
buttonTaxplus = Button(root, text="+TAX", padx=8, pady=5, command=button_Tplus, highlightbackground="#4C897F").grid(row=2,column=1, sticky=NSEW)
buttonPrecent  = Button(root, text="%", padx=19, pady=5, command=button_percent).grid(row=2,column=2, sticky=NSEW)
buttonDivide   = Button(root, text="/", padx=22, pady=5, command=button_divide).grid(row=2,column=3, sticky=NSEW)

#Row 3 Buttons
button7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_num(7)).grid(row=3,column=0, sticky=NSEW)
button8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_num(8)).grid(row=3,column=1, sticky=NSEW)
button9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_num(9)).grid(row=3,column=2, sticky=NSEW)
buttonMultiply = Button(root, text="x",command=button_multiply, padx=20, pady=10).grid(row=3,column=3, sticky=NSEW)

#Row 4 Buttons
button4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_num(4)).grid(row=4,column=0, sticky=NSEW)
button5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_num(5)).grid(row=4,column=1, sticky=NSEW)
button6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_num(6)).grid(row=4,column=2, sticky=NSEW)
buttonMinus = Button(root, text="-", padx=21, pady=10, command=button_subtract).grid(row=4,column=3, sticky=NSEW)

#Row 5 Buttons
button1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_num(1)).grid(row=5,column=0, sticky=NSEW)
button2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_num(2)).grid(row=5,column=1, sticky=NSEW)
button3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_num(3)).grid(row=5,column=2, sticky=NSEW)
buttonPlus = Button(root, text="+", padx=20, pady=10, command=button_add).grid(row=5,rowspan=2,column=3, sticky=NSEW)

#Row 6 Buttons
button0       = Button(root, text="0", padx=20, pady=10, command=lambda: button_num(0)).grid(row=6,column=0, sticky=NSEW)
buttonDecimal = Button(root, text=".", padx=22, pady=10, command=lambda: button_num(".")).grid(row=6,column=1, sticky=NSEW)
buttonEqual   = Button(root, text="=", padx=20, pady=10, command=button_equal).grid(row=6,column=2, sticky=NSEW)
    
root.mainloop()
