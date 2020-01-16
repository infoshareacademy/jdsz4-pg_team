def pokemonA():
    import pandas as pd
    df_pokemons = pd.read_csv('main_Pokemon.csv')
    global name_a, level_a, speed_a, hp_a, def_a, type_a
    while True:
        print('Enter name of pokemon A.')
        name_a = str(input()).capitalize()
        if name_a in list(df_pokemons['pokename']):
            while True:
                print('What is it\'s level?')
                level_a = input()
                try:
                    level_a = int(level_a) 
                    speed_a = int(df_pokemons[(df_pokemons['pokename'] == name_a) & (df_pokemons['pokelevel'] == level_a)]['speed'].mean())
                    hp_a = int(df_pokemons[(df_pokemons['pokename'] == name_a) & (df_pokemons['pokelevel'] == level_a)]['hp'].mean())
                    attack_a = int(df_pokemons[(df_pokemons['pokename'] == name_a) & (df_pokemons['pokelevel'] == level_a)]['attack'].mean())
                    def_a = int(df_pokemons[(df_pokemons['pokename'] == name_a) & (df_pokemons['pokelevel'] == level_a)]['defense'].mean())
                    type_a = str(df_pokemons[(df_pokemons['pokename'] == name_a) & (df_pokemons['pokelevel'] == level_a)]['type1'].unique())
                    print('{} on level {}: \nType = {} \nHP = {} \nDefense = {} \nSpeed = {}'.format(name_a, level_a, type_a, hp_a, def_a, speed_a))
                    break
                except ValueError:
                    print("Oops! I don't think we got {} on level {} is in the archive.".format(name_a,level_a))
            break
        else: 
            print("Oops! I don't think we got such Pokemon archive.")

def pokemonB():
    import pandas as pd
    df_pokemons = pd.read_csv('main_Pokemon.csv')
    global name_b,level_b,speed_b
    while True:
        print('Enter name of pokemon B.')
        name_b = str(input()).capitalize()
        if name_b in list(df_pokemons['pokename']):
            while True:
                print('What is it\'s level?')
                level_b = input()
                try:
                    level_b = int(level_b) 
                    speed_b = int(df_pokemons[(df_pokemons['pokename'] == name_b) & (df_pokemons['pokelevel'] == level_b)]['speed'].mean())
                    hp_b = int(df_pokemons[(df_pokemons['pokename'] == name_b) & (df_pokemons['pokelevel'] == level_b)]['hp'].mean())
                    attack_b = int(df_pokemons[(df_pokemons['pokename'] == name_b) & (df_pokemons['pokelevel'] == level_b)]['attack'].mean())
                    def_b = int(df_pokemons[(df_pokemons['pokename'] == name_b) & (df_pokemons['pokelevel'] == level_b)]['defense'].mean())
                    type_b = str(df_pokemons[(df_pokemons['pokename'] == name_b) & (df_pokemons['pokelevel'] == level_b)]['type1'].unique())
                    print('{} on level {}: \nType = {} \nHP = {} \nDefense = {} \nSpeed = {}'.format(name_b, level_b, type_b, hp_b, def_b, speed_b))
                    break
                except ValueError:
                    print("Oops! I don't think we got {} on level {} is in the archive.".format(name_b,level_b))
            break
        else: 
            print("Oops! I don't think we got such Pokemon archive.")
