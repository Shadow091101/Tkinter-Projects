from tkinter import *
import time


#Refer:https://docs.python.org/3/library/time.html 
root=Tk()
root.geometry('500x500')

def clock():
    global hour
    global minute
    global second
    hour=time.strftime('%H')#for 12 hours used %I instead of %H
    minute=time.strftime('%M')
    second=time.strftime('%S')
    # ms=time.strftime('')
    my_label.config(text=hour+":"+minute+":"+second)
    my_label.after(1000,clock)
    
    

# def update():
#     my_label.config(text='How are you')

lap_count=1
def laps():
    
    global lap_count
    my_lap=Label(root,text=f'Lap {lap_count} :'+hour+":"+minute+":"+second)
    my_lap.pack(pady=2)
    lap_count+=1
    


my_label=Label(root,text='',font=("Helvetica",48),fg='green',bg="black")
my_label.pack(pady=20)

my_lap_button=Button(root,text='Lap',command=laps)
my_lap_button.pack(pady=20)






clock()

root.mainloop()