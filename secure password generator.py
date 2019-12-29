#Secure Password Generator
#Author: Faisal Hossain

#To Do List
#Fix error handling(1) for genPass function
#Finish 'Remember Password'

from tkinter import *
import random

root = Tk()
root.title("Password Generator")

e = Entry(root,width= 35)
e.grid(row=0,columnspan=2,pady=5)

def genPass():
    """Button click function to generate password based on user's selections.
    Params: 
    Returns: (string) randomly generated password displayed as text on entry box
    """
    t=""
    abc="abcdefghijklmnopqrstuvwxy"
    sym="!@#$%&*-_+="
    num="0123456789"
    sim="il1Lo0|OI"
    ambig="""{}[]()/\'"`~,;:.<>"""
    z=""
    if varSym.get() == 1:
        z+= sym
    if varNum.get() == 1:
        z+= num
    if varLower.get() == 1:
        z+= abc.lower()
    if varUpper.get() == 1:
        z+= abc.upper()
    if varAmbig.get() == 0:
        z+= ambig
    if varSim.get() == 1:
        y=""
        for i in range(len(z)-1):
            if z[i] not in sim:
                y=y+z[i]
        z=y
    #Error Handling (1)
    if varSym.get()==0 and varNum.get()==0 and varLower.get()==0 and varUpper.get()==0 and varAmbig.get()== 1:
        #e.insert(0, "ERROR")
        z="ERROR"
    for x in range(int(lenOptions.get())):
        t = t + random.choice(z)
    e.delete(0, END)
    e.insert(0, t)

##Remember Password
##remPass = Label(root,text="Remember your password:").grid(row=1,column=0,sticky=W,pady=5)
##remPassText = Label(root,text=f"{remPassT}").grid(row=1,column=1,sticky=W,pady=5)

#Password Length
passLen = Label(root,text="Password Length:").grid(row=2,column=0,sticky=W)
lenOptions = StringVar(root)
lenOptions.set("16") # default value
passLenMenu = OptionMenu(root, lenOptions, "8", "12", "16","24","32","40","64","80","96","128","256")
passLenMenu.grid(row=2,column=1,sticky=W)

#Include Symbols
includeSym = Label(root,text="Include Symbols:").grid(row=3,column=0,sticky=W)
varSym = IntVar()
Checkbutton(root, text="( e.g. @#$% )", variable=varSym).grid(row=3,column=1,sticky=W)

#Include Numbers
includeNum = Label(root,text="Include Numbers:").grid(row=4,column=0,sticky=W)
varNum = IntVar()
Checkbutton(root, text="( e.g. 123456 )", variable=varNum).grid(row=4,column=1,sticky=W)

#Include Lowercase Characters
includeLower = Label(root,text="Include Lowercase Characters:").grid(row=5,column=0,sticky=W)
varLower = IntVar()
Checkbutton(root, text="( e.g. abcdefgh )", variable=varLower).grid(row=5,column=1,sticky=W)

#Include Uppercase Characters
includeUpper = Label(root,text="Include Uppercase Characters:").grid(row=6,column=0,sticky=W)
varUpper = IntVar()
Checkbutton(root, text="( e.g. ABCDEFGH )", variable=varUpper).grid(row=6,column=1,sticky=W)

#Exclude Similar Characters
excludeSim = Label(root,text="Exclude Similar Characters:").grid(row=7,column=0,sticky=W)
varSim = IntVar()
Checkbutton(root, text="( e.g. i, l, 1, L, o, 0, O )", variable=varSim).grid(row=7,column=1,sticky=W)

#Exclude Ambiguous Characters
excludeAmbig = Label(root,text="Exclude Ambiguous Characters:").grid(row=8,column=0,sticky=W)
varAmbig = IntVar()
Checkbutton(root, text="""( { } [ ] ( ) / \ ' " ` ~ , ; : . < > )""", variable=varAmbig).grid(row=8,column=1,sticky=W)

#Generate Button
genButton = Button(root,text="Generate Password",command=genPass).grid(row=9,columnspan=2,pady=10)

root.mainloop()
