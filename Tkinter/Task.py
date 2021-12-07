from tkinter import*
from module1 import *
from math import*

aken=Tk()
aken.title('Квадратные уравнения')
aken.geometry('600x200')
global a
a=0
b=0
c=0

answer=[]

def lahenda():    
    if (a.get()!=""and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
        else:
            t="Корней нет"
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        elif b.get()=="":
            b.configure(bg="red")
        elif c.get()=="":
            c.configure(bg="red")

def text_to_lbl(event):#ent_number
    text=ent1.get()
    a=text
    print(a)
    lbl5.configure(text=text)
    
    #ent1.delete(0,END)

def text_to_lbl2(event):#ent_number
    text=ent2.get()
    b=text
    lbl5.configure(text=text)
    
    #ent1.delete(0,END)

def text_to_lbl3(event):#ent_number
    text=ent3.get()
    c=text
    lbl5.configure(text=text)
    
    resolve1()
    print(a)
    #ent1.delete(0,END)

def resolve1():
    
    D=b*2-4*a*c    
    lbl5.configure(text=D)
    
    #print(b)
    #print(c)
    #print(D)
    pass

lbl=Label(aken,text='Решение квадратного уравнения',font='Arial 20',bg='lightblue',fg='green')
ent1=Entry(aken,fg='green',width=5,font='Arial 14')
lbl2=Label(aken,text=' x**2+ ',font='Arial 20',fg='green')
ent2=Entry(aken,fg='green',width=5,font='Arial 14')
lbl3=Label(aken,text=' x+ ',font='Arial 20',fg='green')
ent3=Entry(aken,fg='green',width=5,font='Arial 14')
lbl4=Label(aken,text='=0',font='Arial 20',fg='green')
ent3=Entry(aken,fg='green',width=5,font='Arial 14')
btn=Button(aken,text='Решить',font='Arial 14',bg='darkgreen',width=10,height=3)
lbl5=Label(aken,text='Решение',width=50,font='Arial 20',bg='yellow')



ent1.bind('<Return>',text_to_lbl)
ent2.bind('<Return>',text_to_lbl2)
ent3.bind('<Return>',text_to_lbl3)

lbl.pack()
ent1.pack(side=LEFT)
lbl2.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl3.pack(side=LEFT)
ent3.pack(side=LEFT)
lbl4.pack(side=LEFT)
btn.pack(side=LEFT)
lbl5.pack(side=BOTTOM)

aken.mainloop()
