def pokemonA():
    import pandas as pd
    df_pokemons = pd.read_csv('main_Pokemon.csv')
    global name_a, level_a, speed_a
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
                    print('Speed of {} on level {} is equal to: {}.'.format(name_a, level_a, speed_a))
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
                    print('Speed of {} on level {} is equal to: {}.'.format(name_b, level_b, speed_b))
                    break
                except ValueError:
                    print("Oops! I don't think we got {} on level {} is in the archive.".format(name_b,level_b))
            break
        else: 
            print("Oops! I don't think we got such Pokemon archive.")
