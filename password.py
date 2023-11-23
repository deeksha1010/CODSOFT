from tkinter import *
import pyperclip
import random, string
 
root =Tk()
root.geometry("400x400")
 
root.title("Password Generator")
output = StringVar()
 
combination = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]
 
def randompass():
    password = ""
    for y in range(pass_len.get()):
        char_type = random.choice(combination)
        password = password + random.choice(char_type)
     
    output.set(password)
  
def clipboard():
    pyperclip.copy(output.get())

 
title = Label(root, text = 'Password Length', font = 'arial 12 bold').pack(pady=10) 
 
pass_len = IntVar()
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 24, font='arial 16').pack()
 

 
Button(root, command = randompass, text = "Generate Password", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
label = Label(root, text = 'Random Generated Password', font = 'arial 12 bold').pack(pady="30 10")
Entry(root , textvariable = output, width = 24, font='arial 16').pack()
 
Button(root, text = 'Copy to Clipboard', command = clipboard, font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
root.mainloop()  