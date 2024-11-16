from tkinter import *
import pyttsx3
  
root=Tk()
root.geometry('500x500')

engine=pyttsx3.init()

def speak():

    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0,END)
    
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',0.5)        # setting up volume level  between 0 and 1

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate




my_entry=Entry(root,font=("Helvetica",28))
my_entry.pack(pady=20)

my_button=Button(root,text="Speak",command=speak)
my_button.pack(pady=20)


root.mainloop()

