from tkinter import *


def create_pokemon_b():
    import pandas as pd
    df_pokemons = pd.read_csv('/home/js/PycharmProjects/untitled/main_Pokemon.csv')
    while True:
        name = str(entry_pokename_b.get()).capitalize()
        if name in list(df_pokemons['pokename']):
            while True:
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
                    stats = Label(root,
                                  text='{} on level {}: \nType = {} \nHP = {} \nDefense = {} \nSpeed = {}\nAttack = {}\n'.format(
                                      name, level, type1, hp, defense, speed, att), font=("Comic Sans", 15),background="azure")
                    stats.grid(row=8, column=1, columnspan=6, rowspan=6)
                    global poke_b
                    poke_b = tuple(type1, name, level, speed, hp, defense, att)

                except ValueError:
                    error = Label(root, text="Oops! I don't think we got such Pokemon archive.",
                                  font=("Comic Sans", 20),background="azure")
                    error.grid(row=8, column=1)
        else:
            my_label = Label(root, text="Oops! I don't think we got such Pokemon archive.", font=("Comic Sans", 20),background="azure")
            my_label.grid(row=2, column=1)


def create_pokemon_a():
    import pandas as pd
    df_pokemons = pd.read_csv('/home/js/PycharmProjects/untitled/main_Pokemon.csv')
    while True:
        name = str(entry_pokename.get()).capitalize()
        if name in list(df_pokemons['pokename']):
            while True:
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
                    stats = Label(root,
                                  text='{} on level {}: \nType = {} \nHP = {} \nDefense = {} \nSpeed = {}\nAttack = {}\n'.format(
                                      name, level, type1, hp, defense, speed, att), font=("Comic Sans", 15),background="azure")
                    stats.grid(row=1, column=1, columnspan=6, rowspan=6)
                    global poke_a
                    poke_a = tuple(type1, name, level, speed, hp, defense, att)
                except ValueError:
                    error = Label(root, text="Oops! I don't think we got such Pokemon archive.",
                                  font=("Comic Sans", 20),background="azure")
                    error.grid(row=1, column=1)
        else:
            my_label = Label(root, text="Oops! I don't think we got such Pokemon archive.", font=("Comic Sans", 20),background="azure")
            my_label.grid(row=2, column=1)




root = Tk()
root.configure(background='azure')

img = PhotoImage(file="/home/js/PycharmProjects/untitled/pokemon-logo.png")
canvas = Canvas(root,width = 1200, height = 400,background='azure')
canvas.grid(row=0,columnspan=8)
canvas.create_image(0,0, anchor=NW, image=img)

frame1=Frame(root, width=300, height=550, background="azure")
frame1.grid(row=2, column=8, rowspan=12)

frame2=Frame(root, width=300, height=250, background="azure")
frame2.grid(row=2, column=3, rowspan=5)

frame3=Frame(root, width=300, height=250, background="azure")
frame3.grid(row=7, column=3, rowspan=6)

my_label = Label(root, background="azure")
my_label.grid(row=2, column=1)
#entry fields where name and level of pokemon B are entered

label_pokename = Label(root, text='Enter name of Pokemon A.',font=("Comic Sans", 15),background="azure")
label_pokelevel = Label(root, text='What is it\'s level?',font=("Comic Sans", 15),background="azure")

entry_pokename = Entry(root, width=40, font=("Comic Sans", 15))
entry_pokelevel = Entry(root, width=40, font=("Comic Sans", 15))

label_pokename.grid(row=1)
entry_pokename.grid(row=2)
label_pokelevel.grid(row=3)
entry_pokelevel.grid(row=4)

#statistics field

stats = Label(root,background="azure")
stats.grid(row=2,column=1, columnspan=6, rowspan=6)

#button starting function used to pull pokemon data from the csv

button_a = Button(root, text='Search',font=("Comic Sans", 15),command=create_pokemon_a)
button_a.grid(row=5)

#entry fields where name and level of pokemon B are entered

label_pokename_b = Label(root, text='Enter name of Pokemon B.',font=("Comic Sans", 15),background="azure")
label_pokelevel_b = Label(root, text='What is it\'s level?',font=("Comic Sans", 15),background="azure")

entry_pokename_b = Entry(root, width=40, font=("Comic Sans", 15))
entry_pokelevel_b = Entry(root, width=40, font=("Comic Sans", 15))

label_pokename_b.grid(row=7)
entry_pokename_b.grid(row=8)
label_pokelevel_b.grid(row=9)
entry_pokelevel_b.grid(row=10)

#statistics field

stats_b = Label(root)
stats_b.grid(row=7,column=1, columnspan=6, rowspan=6)

#button starting function used to pull pokemon data from the csv

button_b = Button(root, text='Search',font=("Comic Sans", 15),command=create_pokemon_b)
button_b.grid(row=11)


root.mainloop()