from tkinter import *
import time
root=Tk()
root.title("Calculator")
root.geometry("400x800+20+20")
root.config(bg="powder blue")
def result(x):
    if x== '=':
        try:
            s1.set(eval(s1.get()))
        except Exception as e:
            s1.set(e)
    elif x=='C':
        s1.set('')
    elif x=="CE":
        s1.set(s1.get()[:-1])
    elif x=="1/x":
        a="1/"
        s1.set(eval(a+s1.get()))
    elif x=="x^2":
        a="**2"
        s1.set(eval(s1.get()+a))
    elif x=="sqrtx":
        a="**(1/2)"
        s1.set(eval(s1.get()+a))
    else:
        s1.set(s1.get()+x)
   
f1=Frame(root)
f1.pack(padx=10,pady=10,fill="both",expand="yes")
s1=StringVar()
e1=Entry(f1,font="arial  20 bold",bg="yellow",justify="right",relief="raised",bd=5,textvariable=s1)
e1.pack(fill="both",expand="yes",padx=5,pady=5)
for data in ["789/" ,"456*","123+",".0=-",["1/x","x^2","sqrtx","%"],['C','CE']]:
    f2=Frame(root,bg="powder blue")
    for t in data:
        b=Button(f2,text=t,font="arial  20 bold",bg="orange",relief="raised",bd=5,command=lambda x=t:result(x))
        b.pack(side=LEFT,fill="both",expand="yes",padx=10,pady=10)
    f2.pack(padx=5,pady=5,fill="both",expand="yes")
def showtime():
    l1['text']=time.ctime()
    l1.after(1000,showtime)
f1=Frame(root)
f1.pack(padx=5,pady=5,fill="both",expand="yes")
l1=Label(f1,font="arial  20 bold",bg="blue",relief="raised",bd=5)
l1.pack(fill="both",expand="yes",padx=5,pady=5)
showtime()
f1=Frame(root)
f1.pack(padx=5,pady=5,fill="both",expand="yes")
b=Button(f1,text="close",font="arial  20 bold",bg="red",relief="raised",bd=5,command=lambda:root.destroy())
b.pack(side=LEFT,fill="both",expand="yes",padx=10,pady=10)

root.mainloop()
