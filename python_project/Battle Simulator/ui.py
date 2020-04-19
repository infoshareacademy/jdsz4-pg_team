import pandas as pd
global type_a,  name_a, level_a, speed_a, hp_a, def_a, att_a
global type_b,  name_b, level_b, speed_b, hp_b, def_b, att_b
from tkinter import *

#The type effectiveness chart
eff_tab = [ ('Bug', 'Bug', 1), ('Bug', 'Dark', 2), ('Bug', 'Dragon', 1), ('Bug', 'Electric', 1), ('Bug', 'Fairy', 0.5),
           ('Bug', 'Fighting', 0.5), ('Bug', 'Fire', 0.5), ('Bug', 'Flying', 0.5), ('Bug', 'Ghost', 0.5), ('Bug', 'Grass', 2),
           ('Bug', 'Ground', 1), ('Bug', 'Ice', 1), ('Bug', 'Normal', 1), ('Bug', 'Poison', 0.5), ('Bug', 'Psychic', 2),
           ('Bug', 'Rock', 1), ('Bug', 'Steel', 0.5), ('Bug', 'Water', 1), ('Dark', 'Bug', 1), ('Dark', 'Dark', 0.5),
           ('Dark', 'Dragon', 1), ('Dark', 'Electric', 1), ('Dark', 'Fairy', 0.5), ('Dark', 'Fighting', 0.5), ('Dark', 'Fire', 1),
           ('Dark', 'Flying', 1), ('Dark', 'Ghost', 2), ('Dark', 'Grass', 1), ('Dark', 'Ground', 1), ('Dark', 'Ice', 1),
           ('Dark', 'Normal', 1), ('Dark', 'Poison', 1), ('Dark', 'Psychic', 2), ('Dark', 'Rock', 1), ('Dark', 'Steel', 1),
           ('Dark', 'Water', 1), ('Dragon', 'Bug', 1), ('Dragon', 'Dark', 1), ('Dragon', 'Dragon', 2), ('Dragon', 'Electric', 1),
           ('Dragon', 'Fairy', 0), ('Dragon', 'Fighting', 1), ('Dragon', 'Fire', 1), ('Dragon', 'Flying', 1), ('Dragon', 'Ghost', 1),
           ('Dragon', 'Grass', 1), ('Dragon', 'Ground', 1), ('Dragon', 'Ice', 1), ('Dragon', 'Normal', 1), ('Dragon', 'Poison', 1),
           ('Dragon', 'Psychic', 1), ('Dragon', 'Rock', 1), ('Dragon', 'Steel', 0.5), ('Dragon', 'Water', 1), ('Electric', 'Bug', 1),
           ('Electric', 'Dark', 1), ('Electric', 'Dragon', 0.5), ('Electric', 'Electric', 0.5), ('Electric', 'Fairy', 1),
           ('Electric', 'Fighting', 1), ('Electric', 'Fire', 1), ('Electric', 'Flying', 2), ('Electric', 'Ghost', 1),
           ('Electric', 'Grass', 0.5), ('Electric', 'Ground', 0), ('Electric', 'Ice', 1), ('Electric', 'Normal', 1),
           ('Electric', 'Poison', 1), ('Electric', 'Psychic', 1), ('Electric', 'Rock', 1), ('Electric', 'Steel', 1),
           ('Electric', 'Water', 2), ('Fairy', 'Bug', 1), ('Fairy', 'Dark', 2), ('Fairy', 'Dragon', 2), ('Fairy', 'Electric', 1),
           ('Fairy', 'Fairy', 1), ('Fairy', 'Fighting', 2), ('Fairy', 'Fire', 0.5), ('Fairy', 'Flying', 1), ('Fairy', 'Ghost', 1),
           ('Fairy', 'Grass', 1), ('Fairy', 'Ground', 1), ('Fairy', 'Ice', 1), ('Fairy', 'Normal', 1), ('Fairy', 'Poison', 0.5),
           ('Fairy', 'Psychic', 1), ('Fairy', 'Rock', 1), ('Fairy', 'Steel', 0.5), ('Fairy', 'Water', 1), ('Fighting', 'Bug', 0.5),
           ('Fighting', 'Dark', 2), ('Fighting', 'Dragon', 1), ('Fighting', 'Electric', 1), ('Fighting', 'Fairy', 0.5),
           ('Fighting', 'Fighting', 1), ('Fighting', 'Fire', 1), ('Fighting', 'Flying', 0.5), ('Fighting', 'Ghost', 0),
           ('Fighting', 'Grass', 1), ('Fighting', 'Ground', 1), ('Fighting', 'Ice', 2), ('Fighting', 'Normal', 2), ('Fighting', 'Poison', 0.5),
           ('Fighting', 'Psychic', 0.5), ('Fighting', 'Rock', 2), ('Fighting', 'Steel', 2), ('Fighting', 'Water', 1), ('Fire', 'Bug', 2),
           ('Fire', 'Dark', 1), ('Fire', 'Dragon', 0.5), ('Fire', 'Electric', 1), ('Fire', 'Fairy', 1), ('Fire', 'Fighting', 1),
           ('Fire', 'Fire', 0.5), ('Fire', 'Flying', 1), ('Fire', 'Ghost', 1), ('Fire', 'Grass', 2), ('Fire', 'Ground', 1), ('Fire', 'Ice', 2),
           ('Fire', 'Normal', 1), ('Fire', 'Poison', 1), ('Fire', 'Psychic', 1), ('Fire', 'Rock', 0.5), ('Fire', 'Steel', 2), ('Fire', 'Water', 0.5),
           ('Flying', 'Bug', 2), ('Flying', 'Dark', 1), ('Flying', 'Dragon', 1), ('Flying', 'Electric', 0.5), ('Flying', 'Fairy', 1), ('Flying', 'Fighting', 2),
           ('Flying', 'Fire', 1), ('Flying', 'Flying', 1), ('Flying', 'Ghost', 1), ('Flying', 'Grass', 2), ('Flying', 'Ground', 1), ('Flying', 'Ice', 1),
           ('Flying', 'Normal', 1), ('Flying', 'Poison', 1), ('Flying', 'Psychic', 1), ('Flying', 'Rock', 0.5), ('Flying', 'Steel', 0.5), ('Flying', 'Water', 1),
           ('Ghost', 'Bug', 1), ('Ghost', 'Dark', 0.5), ('Ghost', 'Dragon', 1), ('Ghost', 'Electric', 1), ('Ghost', 'Fairy', 1), ('Ghost', 'Fighting', 1),
           ('Ghost', 'Fire', 1), ('Ghost', 'Flying', 1), ('Ghost', 'Ghost', 2), ('Ghost', 'Grass', 1), ('Ghost', 'Ground', 1), ('Ghost', 'Ice', 1),
           ('Ghost', 'Normal', 0), ('Ghost', 'Poison', 1), ('Ghost', 'Psychic', 2), ('Ghost', 'Rock', 1), ('Ghost', 'Steel', 1), ('Ghost', 'Water', 1),
           ('Grass', 'Bug', 0.5), ('Grass', 'Dark', 1), ('Grass', 'Dragon', 0.5), ('Grass', 'Electric', 1), ('Grass', 'Fairy', 1), ('Grass', 'Fighting', 1),
           ('Grass', 'Fire', 0.5), ('Grass', 'Flying', 0.5), ('Grass', 'Ghost', 1), ('Grass', 'Grass', 0.5), ('Grass', 'Ground', 2), ('Grass', 'Ice', 1),
           ('Grass', 'Normal', 1), ('Grass', 'Poison', 0.5), ('Grass', 'Psychic', 1), ('Grass', 'Rock', 2), ('Grass', 'Steel', 0.5), ('Grass', 'Water', 2),
           ('Ground', 'Bug', 0.5), ('Ground', 'Dark', 1), ('Ground', 'Dragon', 1), ('Ground', 'Electric', 2), ('Ground', 'Fairy', 1), ('Ground', 'Fighting', 1),
           ('Ground', 'Fire', 2), ('Ground', 'Flying', 0), ('Ground', 'Ghost', 1), ('Ground', 'Grass', 0.5), ('Ground', 'Ground', 1), ('Ground', 'Ice', 1),
           ('Ground', 'Normal', 1), ('Ground', 'Poison', 2), ('Ground', 'Psychic', 1), ('Ground', 'Rock', 2), ('Ground', 'Steel', 2), ('Ground', 'Water', 1),
           ('Ice', 'Bug', 1), ('Ice', 'Dark', 1), ('Ice', 'Dragon', 2), ('Ice', 'Electric', 1), ('Ice', 'Fairy', 1), ('Ice', 'Fighting', 1), ('Ice', 'Fire', 0.5),
           ('Ice', 'Flying', 2), ('Ice', 'Ghost', 1), ('Ice', 'Grass', 2), ('Ice', 'Ground', 2), ('Ice', 'Ice', 0.5), ('Ice', 'Normal', 1), ('Ice', 'Poison', 1),
           ('Ice', 'Psychic', 1), ('Ice', 'Rock', 1), ('Ice', 'Steel', 0.5), ('Ice', 'Water', 0.5), ('Normal', 'Bug', 1), ('Normal', 'Dark', 1), ('Normal', 'Dragon', 1),
           ('Normal', 'Electric', 1), ('Normal', 'Fairy', 1), ('Normal', 'Fighting', 1), ('Normal', 'Fire', 1), ('Normal', 'Flying', 1), ('Normal', 'Ghost', 0),
           ('Normal', 'Grass', 1), ('Normal', 'Ground', 1), ('Normal', 'Ice', 1), ('Normal', 'Normal', 1), ('Normal', 'Poison', 1), ('Normal', 'Psychic', 1),
           ('Normal', 'Rock', 0.5), ('Normal', 'Steel', 0.5), ('Normal', 'Water', 1), ('Poison', 'Bug', 1), ('Poison', 'Dark', 1), ('Poison', 'Dragon', 1),
           ('Poison', 'Electric', 1), ('Poison', 'Fairy', 2), ('Poison', 'Fighting', 1), ('Poison', 'Fire', 1), ('Poison', 'Flying', 1), ('Poison', 'Ghost', 0.5),
           ('Poison', 'Grass', 2), ('Poison', 'Ground', 0.5), ('Poison', 'Ice', 1), ('Poison', 'Normal', 1), ('Poison', 'Poison', 0.5), ('Poison', 'Psychic', 1),
           ('Poison', 'Rock', 0.5), ('Poison', 'Steel', 0), ('Poison', 'Water', 1), ('Psychic', 'Bug', 1), ('Psychic', 'Dark', 0), ('Psychic', 'Dragon', 1),
           ('Psychic', 'Electric', 1), ('Psychic', 'Fairy', 1), ('Psychic', 'Fighting', 2), ('Psychic', 'Fire', 1), ('Psychic', 'Flying', 1), ('Psychic', 'Ghost', 1),
           ('Psychic', 'Grass', 1), ('Psychic', 'Ground', 1), ('Psychic', 'Ice', 1), ('Psychic', 'Normal', 1), ('Psychic', 'Poison', 2), ('Psychic', 'Psychic', 0.5),
           ('Psychic', 'Rock', 1), ('Psychic', 'Steel', 0.5), ('Psychic', 'Water', 1), ('Rock', 'Bug', 2), ('Rock', 'Dark', 1), ('Rock', 'Dragon', 1), ('Rock', 'Electric', 1),
           ('Rock', 'Fairy', 1), ('Rock', 'Fighting', 0.5), ('Rock', 'Fire', 2), ('Rock', 'Flying', 2), ('Rock', 'Ghost', 1), ('Rock', 'Grass', 1), ('Rock', 'Ground', 0.5),
           ('Rock', 'Ice', 2), ('Rock', 'Normal', 1), ('Rock', 'Poison', 1), ('Rock', 'Psychic', 1), ('Rock', 'Rock', 1), ('Rock', 'Steel', 0.5), ('Rock', 'Water', 1),
           ('Steel', 'Bug', 1), ('Steel', 'Dark', 1), ('Steel', 'Dragon', 1), ('Steel', 'Electric', 0.5), ('Steel', 'Fairy', 2), ('Steel', 'Fighting', 1), ('Steel', 'Fire', 0.5),
           ('Steel', 'Flying', 1), ('Steel', 'Ghost', 1), ('Steel', 'Grass', 1), ('Steel', 'Ground', 1), ('Steel', 'Ice', 2), ('Steel', 'Normal', 1), ('Steel', 'Poison', 1),
           ('Steel', 'Psychic', 1), ('Steel', 'Rock', 2), ('Steel', 'Steel', 0.5), ('Steel', 'Water', 0.5), ('Water', 'Bug', 1), ('Water', 'Dark', 1), ('Water', 'Dragon', 0.5),
           ('Water', 'Electric', 1), ('Water', 'Fairy', 1), ('Water', 'Fighting', 1), ('Water', 'Fire', 2), ('Water', 'Flying', 1), ('Water', 'Ghost', 1), ('Water', 'Grass', 0.5),
           ('Water', 'Ground', 2), ('Water', 'Ice', 1), ('Water', 'Normal', 1), ('Water', 'Poison', 1), ('Water', 'Psychic', 1), ('Water', 'Rock', 2), ('Water', 'Steel', 1),
           ('Water', 'Water', 0.5)]

def get_eff(type_a, type_b):
    for i in range(len(eff_tab)):
        if (eff_tab[i][0] == type_a) and (eff_tab[i][1] == type_b):
            return eff_tab[i][2]

def get_random():
    from numpy.random import random
    return 2*random()-1

def punch(type_fast, hp_fast, def_fast, att_fast, type_slow, hp_slow, def_slow, att_slow):
    eff_fast = get_eff(type_fast, type_slow)
    eff_slow = get_eff(type_slow, type_fast)
    punch_fast = (att_fast - def_slow)*eff_fast
    if punch_fast > 0:
        if punch_fast <= hp_slow:
            hp_slow = hp_slow - punch_fast
        else:
            hp_slow = 0
    else:
        punch_fast = 0
    punch_slow = (att_slow - def_fast)*eff_slow
    if punch_slow > 0:
        if punch_slow <= hp_fast:
            hp_fast = hp_fast-punch_slow
        else:
            hp_fast = 0
    else:
        punch_slow = 0
    return hp_fast, hp_slow, punch_fast, punch_slow

def fight():
    global type_a, name_a, level_a, speed_a, hp_a, def_a, att_a
    global type_b, name_b, level_b, speed_b, hp_b, def_b, att_b
    runda = 0
    res = ""
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
        res=res+"\nRound " + str(runda) + "\n" + name_a + " (lv. "+ str(level_a)+")"+' attacks with strength: ' + str(punch_a) +". " + name_b + " (lv. " + str(level_b)+")" + ' attacks with strength: '+ str(punch_b)
        res = res +'\n '+ name_a+ " (lv. "+ str(level_a)+ ")" +' HP: '+ str(hp_a)+ ". " + name_b+ " (lv. "+ str(level_b)+ ")" + ' HP: '+ str(hp_b)
        rundy.configure(text=res)
        if punch_a == 0 and punch_b == 0:
            break
    if hp_a > hp_b:
        res1 = "\t"+ name_a +" on level "+ str(level_a)+ " won!"
        results.configure(text=res1)
    elif hp_b > hp_a:
        res1 = "\t"+name_b + " on level " + str(level_b) +" won!"
        results.configure(text=res1)
    else:
        results.configure(text="\t Tie!")

def create_pokemon_b():
    global type_a, name_a, level_a, speed_a, hp_a, def_a, att_a
    global type_b, name_b, level_b, speed_b, hp_b, def_b, att_b
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
                                      name, level, type1, hp, defense, speed, att), font=("Comic Sans", 15),background="azure")
                type_b = type1
                name_b = name
                level_b = level
                speed_b = speed
                hp_b = hp
                def_b = defense
                att_b = att
                if att_a != 0 and att_b != 0:
                    button_fight = Button(root, text='FIGHT!', font=("Comic Sans", 10), command=fight)
                    button_fight.grid(row=6, column=1)
            except ValueError:
                stats_b.configure(text="Oops! I don't think we got such Pokemon archive.",
                                  font=("Comic Sans", 15),background="azure")
    else:

        stats_b.configure(text="Oops! I don't think we got such Pokemon archive.", font=("Comic Sans", 15),background="azure")

def create_pokemon_a():
    global type_a, name_a, level_a, speed_a, hp_a, def_a, att_a
    global type_b, name_b, level_b, speed_b, hp_b, def_b, att_b
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
                type_a = type1
                name_a = name
                level_a = level
                speed_a = speed
                hp_a = hp
                def_a = defense
                att_a = att
                if att_a != 0 and attack_b != 0:
                    button_fight = Button(root, text='FIGHT!', font=("Comic Sans", 10),command=fight)
                    button_fight.grid(row=6, column=1)
            except ValueError:
                stats.configure(text="Oops! I don't think we got such Pokemon archive.",
                                  font=("Comic Sans", 15),background="azure")
    else:
       stats.configure(text="Oops! I don't think we got such Pokemon archive.", font=("Comic Sans", 15),background="azure")


root = Tk()
root.configure(background='azure')
root.geometry('1200x1200')

img = PhotoImage(file="pokemon-logo2.png")
canvas = Canvas(root,width = 500, height = 200,background='azure')
canvas.grid(row=0, column=1,columnspan=8)
canvas.create_image(0,0, anchor=NW, image=img)

frame1=Frame(root, width=500, height=550, background="azure")
frame1.grid(row=1, column=7, rowspan=12)

frame2=Frame(root, width=300, height=250, background="azure")
frame2.grid(row=1, column=2, rowspan=5)

frame3=Frame(root, width=300, height=250, background="azure")
frame3.grid(row=6, column=2, rowspan=5)

my_label = Label(root, background="azure")
my_label.grid(row=2, column=1)
#entry fields where name and level of pokemon B are entered

label_pokename = Label(root, text='Enter name of Pokemon A',font=("Comic Sans", 15),background="azure")
label_pokelevel = Label(root, text='What is it\'s level?',font=("Comic Sans", 15),background="azure")

entry_pokename = Entry(root, width=20, font=("Comic Sans", 15))
entry_pokelevel = Entry(root, width=20, font=("Comic Sans", 15))

label_pokename.grid(row=1)
entry_pokename.grid(row=2)
label_pokelevel.grid(row=3)
entry_pokelevel.grid(row=4)

#statistics field

stats = Label(frame2,font=("Comic Sans", 15),background="azure")
stats.grid(row=0, column=0, columnspan=6, rowspan=6, )

#button starting function used to pull pokemon data from the csv

# button_a = Button(root, text='Search',font=("Comic Sans", 15),command= (lambda: attack=create_pokemon_a() ))
button_a = Button(root, text='Search',font=("Comic Sans", 15),command=create_pokemon_a)

button_a.grid(row=5)

#entry fields where name and level of pokemon B are entered

label_pokename_b = Label(root, text='Enter name of Pokemon B',font=("Comic Sans", 15),background="azure")
label_pokelevel_b = Label(root, text='What is it\'s level?',font=("Comic Sans", 15),background="azure")

entry_pokename_b = Entry(root, width=20, font=("Comic Sans", 15))
entry_pokelevel_b = Entry(root, width=20, font=("Comic Sans", 15))

label_pokename_b.grid(row=7)
entry_pokename_b.grid(row=8)
label_pokelevel_b.grid(row=9)
entry_pokelevel_b.grid(row=10)

#statistics field

stats_b = Label(frame3,font=("Comic Sans", 15),background="azure")
stats_b.grid(row=7,column=1, columnspan=6, rowspan=6)

#button starting function used to pull pokemon data from the csv

button_b = Button(root, text='Search',font=("Comic Sans", 15),command=create_pokemon_b)
button_b.grid(row=11)

rundy = Label(frame1, font=("Comic Sans", 12),background="azure")
rundy.grid(row=0)

results = Label(frame1, font=("Comic Sans", 20, ), fg='red', background="azure")
results.grid(column=1,row=0)

root.mainloop()