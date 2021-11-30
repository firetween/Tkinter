from tkinter import*

klik=0
def klicker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)

def klicker2(event):
    global klik
    if klik>0:
        klik-=1
    else:
        klik=0
    lbl.configure(text=klik)

def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)

def valik():
    #val=var.get()#здесь считывается 1,2 или 3
    #ent.insert(END,str(val)+', ')
    #или
    val=str(var.get())+', '#здесь считывается 1,2 или 3
    ent.insert(END,val)

aken=Tk()
aken.title('Window name')
aken.geometry('600x400')

btn=Button(aken,text='Press it!',font='Arial 14',fg='green',bg='lightblue',width=20,height=3)
lbl=Label(aken,text='ˇ~ˇ')
ent=Entry(aken,fg='blue',width=20,font='Arial 14')
var=IntVar() #or StringVar()
var.set(3) #делает функцию активной, выбирает третью кнопку(?)
r1=Radiobutton(aken,text='First',variable=var,value=1,font='Arial 14',fg='gray',bg='darkgray',width=20,height=3,command=valik)
r2=Radiobutton(aken,text='Second',variable=var,value=2,font='Arial 14',fg='gray',bg='darkgray',width=20,height=3,command=valik)
r3=Radiobutton(aken,text='Third',variable=var,value=3,font='Arial 14',fg='gray',bg='darkgray',width=20,height=3,command=valik)


btn.bind('<Button-1>',klicker)
btn.bind('<Button-3>',klicker2)
ent.bind('<Return>',text_to_lbl)#Enter

lbl.pack()
btn.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
aken.mainloop()
ent=Entry(aken,fg='blue',width=20,font='Arial 14')
