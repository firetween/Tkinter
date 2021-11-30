def klicker(event):
    #global klik
    #klik+=1
    #lbl.configure(text=klik)
    pass

def text_to_lbl(ent_number,lbl_number):
    text_field=ent_number.get()
    lbl_number.configure(text=text_field)
    ent_number.delete(0,END)
    #text=ent.get()
    #lbl.configure(text=text)
    #ent.delete(0,END)
