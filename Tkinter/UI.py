from tkinter import *
from tkinter import ttk

def colorise(field):
    field.configure(bg='lightblue')


def solution():
    if (a_Field.get()!='' and b_Field.get()!='' and c_Field.get()!=''): 
        a=int(a_Field.get())
        b=int(b_Field.get())
        c=int(c_Field.get())
        D=b**2-4*a*c
        if D>0:
            x1=round((-1*b+sqrt(D))/(2*a),2)
            x2=round((-1*b-sqrt(D))/(2*a),2)
            text=f'X1={x1}, \nX2={x2}'
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f'X1={x1}'
        else:
            t='Корней нет'
        lbl5.configure(text=f'D={D}\n{t}')
        colorise(a_Field)
        colorise(b_Field)
        colorise(c_Field)
    else:
        if a_Field.get()=='':
            a_Field.configure(bg='red')
        elif b_Field.get()=='':
            b_Field.configure(bg='red')
        elif c_Field.get()=='':
            c_Field.configure(bg='red')

aken=Tk() #Создание окна
aken.title('Quadratic equation') #Заголовок окна
aken.geometry('600x165') #Размер окна

lbl=Label(aken,text='Решение квадратного уравнения',font="Arial 20",fg="green",bg="lightblue") 
btn=Button(aken,text="Решить",font="Arial 20",bg="green",command=solution)
a_Field=Entry(aken,width=5,font="Arial 20",fg="green",bg="lightblue")
lbl2=Label(aken,text=" x**2+ ",width=4,font="Arial 20",fg="green") 
b_Field=Entry(aken,width=4,font="Arial 20",fg="green",bg="lightblue")
lbl3=Label(aken,text="x+",width=3,font="Arial 20",fg="green")
c_Field=Entry(aken,width=4,font="Arial 20",fg="green",bg="lightblue")
lbl4=Label(aken,text="=",width=3,font="Arial 20",fg="green")
lbl5=Label(aken,text="Решение",height=2,width=30,font="Arial 10",bg="yellow")

lbl.pack()
a_Field.pack(side=LEFT)
lbl2.pack(side=LEFT)
b_Field.pack(side=LEFT)
lbl3.pack(side=LEFT)
c_Field.pack(side=LEFT)
lbl4.pack(side=LEFT)
btn.pack(side=LEFT)
lbl5.pack()
lbl5.place(x=180,y=130)

aken.mainloop()

