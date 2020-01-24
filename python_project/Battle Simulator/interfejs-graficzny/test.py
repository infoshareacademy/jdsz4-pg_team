from tkinter import Label
from mechanika import create_pokemon
from tkinter import *
window = Tk()
window.title("Pokemon battle symulator app")
window.geometry('1200x600')

lbl = Label(window, text="Pokemon A name:", font=("Comic Sans", 28))
lbl.grid(column=0, row=0)

txt_name = Entry(window, width=10,font=("Comic Sans", 28))
txt_name.grid(column=1, row=0)

txt_lvl = Entry(window, width=10,font=("Comic Sans", 28))
txt_lvl.grid(column=1, row=1)

lbl_lvl = Label(window, text="Pokemon A level:", font=("Comic Sans", 28))
lbl_lvl.grid(column=0, row=1)


def clicked():
    pname = txt_name.get()
    plvl = txt_lvl.get()
    poke_a = create_pokemon(pname, plvl)
    type_a,  name_a, level_a, speed_a, hp_a, def_a, att_a = poke_a
    if type_a!=0:
        res ="Pokemon name " +name_a+"\nlevel: "+str(level_a)+"\nspeed: "+str(speed_a)+ "\nhp: "+str(hp_a)+"\ndeff: "+ str(def_a) +"\natt: " + str(att_a)
        lbl_pokea = Label(window, text = res, font=("Comic Sans", 24) )
        lbl_pokea.grid(column=0, row=2)
    else:
        res = "Oops! I don't think we got such Pokemon archive."
    lbl_pokea = Label(window, text = res, font=("Comic Sans", 24) )
    lbl_pokea.grid(column=0, row=2)
    # lbl.configure(text= res)
    # lbl_lvl.configure(text= plvl)
    # lbl.configure(text="Button was clicked !!")

createPKbtn = Button(window, text="Create  Pokemon",font=("Comic Sans", 28), command=clicked)
createPKbtn.grid(column=2,row=0)

window.mainloop()