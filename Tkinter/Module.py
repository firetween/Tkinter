def colorise(field1,field2,field3):
    field1.configure(bg='lightblue')
    field2.configure(bg='lightblue')
    field3.configure(bg='lightblue')


def solution(var1, var2, var3, field1, field2, field3):
    if (var1.get()!='' and var2.get()!='' and var3.get()!=''): 
        a=int(var1.get())
        b=int(var2.get())
        c=int(var3.get())
        D=b**2-4*a*c
        if D>0:
            x1=round((-1*b+sqrt(D))/(2*a),2)
            x2=round((-1*b-sqrt(D))/(2*a),2)
            text=f'X1={x1}, \nX2={x2}'
        elif D==0:
            x1=round((-1*b)/(2*a),2)
            t=f'X1={x1}'
        else:
            t='Корней нет'
        lbl5.configure(text=f'D={D}\n{t}')
        colorise(field1, field2, field3)

    else:
        if a_Field.get()=='':
            a_Field.configure(bg='red')
        elif b_Field.get()=='':
            b_Field.configure(bg='red')
        elif c_Field.get()=='':
            c_Field.configure(bg='red')
