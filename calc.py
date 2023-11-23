from tkinter import *  
from tkinter import messagebox 
from functools import partial

root=Tk()
root.title("Calc")
root.geometry("220x260")

txtBox=StringVar()
evalBox=StringVar()
txtBox.set("")  
evalBox.set("")  
def set_text(ch):
    txt=txtBox.get()  
    txtBox.set("{}{}".format(txt,ch))
    
def operator(opr):
    evl=evalBox.get()
    txt=txtBox.get()     
    if txt=="":
        return
    evalBox.set("{}{}{}".format(evl,txt,opr))
    txtBox.set("")  
    
def calculate():
    evl=evalBox.get()  
    txt=txtBox.get() 
    evalBox.set("{}{}".format(evl,txt))
    txtBox.set("")
    evl=evalBox.get() 
    oprs=['+','-','*','/']
    c=evl[-1:]
    if c in oprs:
       evl=evl[:-1]
    txtBox.set(str(eval(evl)))
    
def clr_text():
    txtBox.set("") 
    evalBox.set("") 
    
Entry(root,textvariable = evalBox,font = ('Arial',8,'normal'),width=30,justify='right',state='readonly').place(x=10,y=1)
Entry(root,textvariable = txtBox,font = ('Arial',18,'normal'),width=14,justify='right',state='readonly').place(x=10,y=20)

Button(root,text=" 7 ",font=('Arial', 13),command=partial(set_text,"7"),padx=5,pady=5).place(x=10,y=60)
Button(root,text=" 8 ",font=('Arial', 13),command=partial(set_text,"8"),padx=5,pady=5).place(x=60,y=60)
Button(root,text=" 9 ",font=('Arial', 13),command=partial(set_text,"9"),padx=5,pady=5).place(x=110,y=60)
Button(root,text=" / ",font=('Arial', 13),command=partial(operator,"/"),padx=5,pady=5).place(x=160,y=60)

Button(root,text=" 4 ",font=('Arial', 13),command=partial(set_text,"4"),padx=5,pady=5).place(x=10,y=110)
Button(root,text=" 5 ",font=('Arial', 13),command=partial(set_text,"5"),padx=5,pady=5).place(x=60,y=110)
Button(root,text=" 6 ",font=('Arial', 13),command=partial(set_text,"6"),padx=5,pady=5).place(x=110,y=110)
Button(root,text=" * ",font=('Arial', 13),command=partial(operator,"*"),padx=5,pady=5).place(x=160,y=110)

Button(root,text=" 1 ",font=('Arial', 13),command=partial(set_text,"1"),padx=5,pady=5).place(x=10,y=160)
Button(root,text=" 2 ",font=('Arial', 13),command=partial(set_text,"2"),padx=5,pady=5).place(x=60,y=160)
Button(root,text=" 3 ",font=('Arial', 13),command=partial(set_text,"3"),padx=5,pady=5).place(x=110,y=160)
Button(root,text=" - ",font=('Arial', 13),command=partial(operator,"-"),padx=5,pady=5).place(x=160,y=160)

Button(root,text=" C ",font=('Arial', 12),command=clr_text,padx=5,pady=5).place(x=10,y=210)
Button(root,text=" 0 ",font=('Arial', 13),command=partial(set_text,"0"),padx=5,pady=5).place(x=60,y=210)
Button(root,text=" = ",font=('Arial', 13),command=calculate,padx=5,pady=5).place(x=110,y=210)
Button(root,text=" + ",font=('Arial', 12),command=partial(operator,"+"),padx=5,pady=5).place(x=160,y=210)

root.mainloop()