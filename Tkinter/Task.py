from tkinter import*
from tkinter import ttk

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

def uus_aken(ind:int):
    uusAken=Toplevel()
    tabs=ttk.Notebook(uusAken)
    texts=['1.png','2.png','3.png','4.png','5.png']
    tab=[]
    for i in range(len(texts)):
        tab[i]=Frame(tabs)
        tabs.add(tab[i], text=texts[i])
        #i+=1 здесь это нахрен не упало, потому что инкреминент i идет уже по ходу пробегания по списку



    #tab1=Frame(tabs)
    #img1=PhotoImage(file=texts[0]).subsample(7)
    #tabs.add(tab1,text=texts[0])
    #can1=Canvas(tab1,width=600,height=300,bg='red')
    #can1.create_image(0,0,image=img1,anchor=NW)
    #can1.pack()
    #tab2=Frame(tabs)
    #tab3=Frame(tabs)
    #tab4=Frame(tabs)
    #tab5=Frame(tabs)
    #tabs.add(tab1,text=texts[0])
    #tabs.add(tab2,text=texts[1])
    #tabs.add(tab3,text=texts[2])
    #tabs.add(tab4,text=texts[3])
    #tabs.add(tab5,text=texts[4])
    #tabs.grid(row=0,column=0)
    tabs.select(ind)
    uusAken.mainloop()

#def ava_pilt(ind:int):
#    global tabs
#    tabs.select(ind)

aken=Tk()
aken.title('Window name')
aken.geometry('600x400')
menu=Menu(aken)
aken.config(menu=menu)
m1=Menu(menu)
menu.add_cascade(label='Tabs',menu=m1)
m1.add_command(label='Tab1',accelerator='Command+A',command=lambda:uus_aken(0))
m1.add_command(label='Tab2',command=lambda:uus_aken(1))
m1.add_command(label='Tab3',command=lambda:uus_aken(2))
m1.add_separator()

btn=Button(aken,text='Press it!',font='Arial 14',fg='green',bg='lightblue',width=20,height=3)
btn2=Button(aken,text=' Double window ',font='Arial 12',fg='green',bg='lightblue', command=lambda:uus_aken(0))
lbl=Label(aken,text='ˇ~ˇ')
ent=Entry(aken,fg='blue',width=20,font='Arial 14')
var=IntVar() #or StringVar()
var.set(3) #делает функцию активной, выбирает третью кнопку(?)

r1=Radiobutton(aken,text='First',variable=var,value=1,font='Arial 14',fg='gray',bg='darkgray',command=valik)
r2=Radiobutton(aken,text='Second',variable=var,value=2,font='Arial 14',fg='gray',bg='darkgray',command=valik)
r3=Radiobutton(aken,text='Third',variable=var,value=3,font='Arial 14',fg='gray',bg='darkgray',command=valik)


btn.bind('<Button-1>',klicker)
btn.bind('<Button-3>',klicker2)
ent.bind('<Return>',text_to_lbl)#Enter

lbl.pack()
btn.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
btn2.pack(side=RIGHT)
aken.mainloop()
#ent=Entry(aken,fg='blue',width=20,font='Arial 14')
