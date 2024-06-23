from tkinter import *

root=Tk()

root.title("Simple Calculator.")
root.iconbitmap('calculator.ico')

e=Entry(root,width=60,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    pass

def add():
    first_number=e.get()
    global f_num
    global operation
    operation='addition'
    f_num=int(first_number)
    e.delete(0,END)
    pass
def sub():
    first_number=e.get()
    global f_num
    global operation
    operation='subtraction'
    f_num=int(first_number)
    e.delete(0,END)
    pass

def mul():
    first_number=e.get()
    global f_num
    global operation
    operation='multiplication'
    f_num=int(first_number)
    e.delete(0,END)
    pass

def div():
    first_number=e.get()
    global f_num
    global operation
    operation='division'
    f_num=int(first_number)
    e.delete(0,END)
    pass

def clear():
    e.delete(0,END)
    pass
def equal():
    second_number=e.get()
    e.delete(0,END)

    if operation=='addition':
        e.insert(0,f_num+int(second_number))
    if operation=='subtraction':
        e.insert(0,f_num-int(second_number))
    if operation=='multiplication':
        e.insert(0,f_num*int(second_number))
    if operation=='division':
        e.insert(0,f_num/int(second_number))


button_1=Button(root,text="1",padx="40",pady=20,command=lambda:button_click(1))
button_2=Button(root,text="2",padx="40",pady=20,command=lambda:button_click(2))
button_3=Button(root,text="3",padx="40",pady=20,command=lambda:button_click(3))
button_4=Button(root,text="4",padx="40",pady=20,command=lambda:button_click(4))
button_5=Button(root,text="5",padx="40",pady=20,command=lambda:button_click(5))
button_6=Button(root,text="6",padx="40",pady=20,command=lambda:button_click(6))
button_7=Button(root,text="7",padx="40",pady=20,command=lambda:button_click(7))
button_8=Button(root,text="8",padx="40",pady=20,command=lambda:button_click(8))
button_9=Button(root,text="9",padx="40",pady=20,command=lambda:button_click(9))
button_0=Button(root,text="0",padx="40",pady=20,command=lambda:button_click(0))
button_add=Button(root,text="+",padx="40",pady="20",command=add)
button_sub=Button(root,text="-",padx="41",pady="20",command=sub)
button_mul=Button(root,text="x",padx="41",pady="20",command=mul)
button_div=Button(root,text="/",padx="41",pady="20",command=div)
button_equalto=Button(root,text="=",padx="39",pady="20",command=equal)

button_clear=Button(root,text="Clear",padx="30",pady="20",command=clear)

button_9.grid(row=1,column=2)
button_8.grid(row=1,column=1)
button_7.grid(row=1,column=0)

button_6.grid(row=2,column=2)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=0)

button_3.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=0)

button_0.grid(row=4,column=1)
button_clear.grid(row=4,column=0)
button_equalto.grid(row=4,column=2)

button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)


root.mainloop()

button_1