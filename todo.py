from tkinter import *
from tkinter import messagebox


# new task
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


#delete task
def deleteTask():
    lb.delete(ANCHOR)

#window     
win = Tk()
win.geometry('500x450+500+200')
win.title('ToDo List')
win.config(bg='#FFFFFF')
win.resizable(width=False, height=False)

#frame
frame = Frame(win)
frame.pack(pady=10)

#list
lb = Listbox(
    frame,
    width=27,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#e6cccc',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",   
)
lb.pack(side=LEFT, fill=BOTH)

task_list = []
for item in task_list:
    lb.insert(END, item)

#scrollbar
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    win,
    font=('times', 24)
    )
my_entry.pack(pady=20)

#buttons adding
button_frame = Frame(win)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=25,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


#buttons deleting
delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

win.mainloop()