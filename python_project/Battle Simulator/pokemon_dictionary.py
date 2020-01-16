def pokemon_list():
    import pandas as pd
    import numpy as np
    df_pokemons = pd.read_csv('main_Pokemon.csv')
    print('Which letter starts the name of Pokemon you are looking for?')
    try:
        s_letter = input().capitalize()
        pokelist = df_pokemons[df_pokemons.pokename.str.startswith(s_letter)]["pokename"].unique()
        print(np.array(pokelist))
    except ValueError:
        print('I do not think we have any Pokemon which name start with letter {}.'.format(s_letter))
