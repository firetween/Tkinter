from tkinter import*
from module1 import *

aken=Tk()
aken.title('Квадратные уравнения')
aken.geometry('600x200')

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

ent1.bind('<Return>',text_to_lbl(ent1,lbl))

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
