def create_pokemon():
    import pandas as pd
    df_pokemons = pd.read_csv('main_Pokemon.csv')
    while True:
        print('\nEnter name of Pokemon.')
        name = str(input()).capitalize()
        if name in list(df_pokemons['pokename']):
            while True:
                print("Enter this {}'s level.".format(name))
                level = input()
                try:
                    level = int(level)
                    speed = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)]['speed'].mean())
                    hp = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)]['hp'].mean())
                    att = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)]['attack'].mean())
                    defense = int(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)]['defense'].mean())
                    type1 = str(df_pokemons[(df_pokemons['pokename'] == name) & (df_pokemons['pokelevel'] == level)]['type1'].unique()[0])
                    print('{} on level {}: \nType = {} \nHP = {} \nDefense = {} \nSpeed = {}\nAttack = {}\n'.format(name, level, type1, hp, defense, speed,att))
                    return type1, name, level, speed, hp, defense, att
                except ValueError:
                    print("Oops! I don't think we got {} on level {} is in the archive.\nWould you like to choose other Pokemon?".format(name, level))
                    answer = input().capitalize()
                    if answer == 'Yes':
                        break
        else:
            print("Oops! I don't think we got such Pokemon archive.")

