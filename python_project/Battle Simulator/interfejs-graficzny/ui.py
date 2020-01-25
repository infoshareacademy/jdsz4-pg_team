from tkinter import *
import pandas as pd


global poke_a, poke_b

def create_pokemon_b():
    global poke_b, poke_a
    df_pokemons = pd.read_csv('main_Pokemon.csv')
    name = str(entry_pokename_b.get()).capitalize()
    if name in list(df_pokemons['pokename']):
            level = entry_pokelevel_b.get()
            try:
                level = int(level)
                speed = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                    'speed'].mean())
                hp = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                 'hp'].mean())
                att = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                  'attack'].mean())
                defense = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                      'defense'].mean())
                type1 = str(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                    'type1'].unique()[0])
                stats_b.configure(text='{} on level {}: \nType = {} \nHP = {} \nDefense = {} \nSpeed = {}\nAttack = {}\n'.format(
                                      name, level, type1, hp, defense, speed, att), font=("Comic Sans", 10),background="azure")
                poke_b = tuple(type1, name, level, speed, hp, defense, att)
                if len(poke_a) != 0 and len(poke_a) != 0:
                    button_fight = Button(root, text='FIGHT!', font=("Comic Sans", 10))
                    button_fight.grid(row=6, column=1, command=fight(poke_a,poke_b))
            except ValueError:
                stats_b.configure(text="Oops! I don't think we got such Pokemon archive.",
                                  font=("Comic Sans", 10),background="azure")
    else:

        stats_b.configure(text="Oops! I don't think we got such Pokemon archive.", font=("Comic Sans", 10),background="azure")


def create_pokemon_a():
    global poke_a, poke_b
    df_pokemons = pd.read_csv('main_Pokemon.csv')
    name = str(entry_pokename.get()).capitalize()
    if name in list(df_pokemons['pokename']):
            level = entry_pokelevel.get()
            try:
                level = int(level)
                speed = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                    'speed'].mean())
                hp = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                 'hp'].mean())
                att = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                  'attack'].mean())
                defense = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                      'defense'].mean())
                type1 = str(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)][
                                    'type1'].unique()[0])
                stats.configure(text='{} on level {}: \nType = {} \nHP = {} \nDefense = {} \nSpeed = {}\nAttack = {}\n'.format(
                                      name, level, type1, hp, defense, speed, att))
                poke_a = (type1, name, level, speed, hp, defense, att)
                if len(poke_a) != 0 and len(poke_a) != 0:
                    button_fight = Button(root, text='FIGHT!', font=("Comic Sans", 10))
                    button_fight.grid(row=6, column=1)
            except ValueError:
                stats.configure(text="Oops! I don't think we got such Pokemon archive.",
                                  font=("Comic Sans", 10),background="azure")
    else:
       stats.configure(text="Oops! I don't think we got such Pokemon archive.", font=("Comic Sans", 10),background="azure")



root = Tk()

poke_a = ()
poke_b = ()

root.configure(background='azure')
root.geometry('1200x1200')

img = PhotoImage(file="pokemon-logo.png")
canvas = Canvas(root,width = 1200, height = 400,background='azure')
canvas.grid(row=0,columnspan=8)
canvas.create_image(0,0, anchor=NW, image=img)

frame1=Frame(root, width=300, height=550, background="azure")
frame1.grid(row=1, column=8, rowspan=12)

frame2=Frame(root, width=300, height=250, background="azure")
frame2.grid(row=1, column=2, rowspan=5)

frame3=Frame(root, width=300, height=250, background="azure")
frame3.grid(row=6, column=2, rowspan=6)

my_label = Label(root, background="azure")
my_label.grid(row=2, column=1)
#entry fields where name and level of pokemon B are entered

label_pokename = Label(root, text='Enter name of Pokemon A.',font=("Comic Sans", 10),background="azure")
label_pokelevel = Label(root, text='What is it\'s level?',font=("Comic Sans", 10),background="azure")

entry_pokename = Entry(root, width=40, font=("Comic Sans", 10))
entry_pokelevel = Entry(root, width=40, font=("Comic Sans", 10))

label_pokename.grid(row=1)
entry_pokename.grid(row=2)
label_pokelevel.grid(row=3)
entry_pokelevel.grid(row=4)

#statistics field

stats = Label(frame2,font=("Comic Sans", 10),background="azure")
stats.grid(row=0, column=0, columnspan=6, rowspan=6, )

#button starting function used to pull pokemon data from the csv

button_a = Button(root, text='Search',font=("Comic Sans", 10),command=create_pokemon_a)
button_a.grid(row=5)

#entry fields where name and level of pokemon B are entered

label_pokename_b = Label(root, text='Enter name of Pokemon B.',font=("Comic Sans", 10),background="azure")
label_pokelevel_b = Label(root, text='What is it\'s level?',font=("Comic Sans", 10),background="azure")

entry_pokename_b = Entry(root, width=40, font=("Comic Sans", 10))
entry_pokelevel_b = Entry(root, width=40, font=("Comic Sans", 10))

label_pokename_b.grid(row=7)
entry_pokename_b.grid(row=8)
label_pokelevel_b.grid(row=9)
entry_pokelevel_b.grid(row=10)

#statistics field

stats_b = Label(frame3,font=("Comic Sans", 10),background="azure")
stats_b.grid(row=7,column=1, columnspan=6, rowspan=6)

#button starting function used to pull pokemon data from the csv

button_b = Button(root, text='Search',font=("Comic Sans", 10),command=create_pokemon_b)
button_b.grid(row=11)

##########################################################################################



results = Label(frame1, font=("Comic Sans", 10),background="grey")
results.grid(row=0)

def fight(poke_a, poke_b):
    type_a, name_a, level_a, speed_a, hp_a, def_a, att_a = poke_a
    type_b, name_b, level_b, speed_b, hp_b, def_b, att_b = poke_b
    runda = 0
    while True:
        if hp_a == 0 or hp_b == 0:
            break
        else:
            if speed_a > speed_b:
                (hp_a, hp_b, punch_a, punch_b) = punch(type_a, hp_a, def_a, att_a, type_b, hp_b, def_b, att_b)
            elif speed_a < speed_b:
                (hp_b, hp_a, punch_b, punch_a) = punch(type_b, hp_b, def_b, att_b, type_a, hp_a, def_a, att_a)
            else:
                x = get_random()
                if x > 0:
                    (hp_a, hp_b, punch_a, punch_b) = punch(type_a, hp_a, def_a, att_a, type_b, hp_b, def_b, att_b)
                elif x == 0:
                    x = get_random()
                else:
                    (hp_b, hp_a, punch_b, punch_a) = punch(type_b, hp_b, def_b, att_b, type_a, hp_a, def_a, att_a)
        runda = runda + 1
        results.configure(text=f'Round: {runda} \n \t {name_a} attacks with strength: {punch_a}, '
                               f'{name_b} attacks with strength: {punch_b}')
        results.configure(text=f'\t {name_a} HP: {hp_a}, {name_b}, HP {hp_b}')
        if punch_a == 0 and punch_b == 0:
            break
    if hp_a > hp_b:
        results.configure(text=f'{name_a} won!')
    elif hp_b > hp_a:
        results.configure(text=f'{name_b} won!')
    else:
        results.configure(text='Tie!')


##########################################################################################


root.mainloop()
