#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.
import csv
import copy

from weapon_type import WeaponType
from pokemon import Pokemon


def get_data_from_user(name_file):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      Null .

    Example
    -------
      >>> get_data_from_user("file.csv")
    """
    set_of_pokemons = []

    #Nos aseguramos que name_file sea de tipo string
    if not isinstance(name_file, str):
        raise TypeError("name_file no es una cadena de texto")

    name_file_s = name_file

    try:
        with open(name_file_s, newline='') as csv_file:
            reader = csv.reader(csv_file)
            data_from_file = list(reader)

        for temp_pokemon_csv in data_from_file:
            coach_pokemon = Pokemon(int(temp_pokemon_csv[0]),
                                    temp_pokemon_csv[1],
                                    WeaponType.from_str(temp_pokemon_csv[2]),
                                    int(temp_pokemon_csv[3]),
                                    int(temp_pokemon_csv[4]),
                                    int(temp_pokemon_csv[5]))

            set_of_pokemons.append(coach_pokemon)

    #Excepcion por si nos equivocamos al introducir los pokemons
    except SyntaxError:
        print("Oops! Los pokemon fueron introducimos incorrectamente, intentelo de nuevo...")

    return set_of_pokemons



def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Null .

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """
    #Nos aseguramos que la lista de los pokemon sea una lista
    if isinstance(list_of_pokemons,list):

        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("Todos los Pokemon deber ser de un tipo")
        print("Por favor entrenador " + str(coach_to_ask) + " introduce la ID del Pokemon: " + "\n")

        while True:
            print("Lista de Pokemons: " + "\n")
            
            for i in list_of_pokemons:
                print(i)
            
            string_introduced = input(":~>")
            try:
                int_introduced= int(string_introduced)
            except ValueError:
                print("Por favor, introduce un ID presente en la lista:")
            for temp_pokemon in list_of_pokemons:
                if int_introduced == temp_pokemon.get_id():
                    return temp_pokemon
            print("Por favor introduza un numero presente en la lista")
    #Salta la excepcion ya que no list_pokemons no es una lista
    else:
        raise TypeError("list_pokemons deberia ser una lista")



def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Null .

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """

    #Nos aseguramos que la lista de pokemons es una lista
    if isinstance(list_of_pokemons, list):
        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("Todos los pokemon deben ser de un tipo")

    defeated = True

    for temp_pokemon in list_of_pokemons:
        if temp_pokemon.is_alive():
            defeated = False

    return not defeated


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")


    # Get configuration for Game User 1.
    print ("Configuracion del jugador 1: \n")
    game_user_1 = get_data_from_user("coach_1_pokemons.csv")

    # Get configuration for Game User 2.
    print ("Configuracion del jugador 2: \n")
    game_user_2 = get_data_from_user("coach_2_pokemons.csv")


    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    temp_list_pokemons_from_coach_1 = game_user_1
    list_pokemons_alive_coach_1 = copy.copy(temp_list_pokemons_from_coach_1)

    temp_list_pokemons_from_coach_2 = game_user_2
    list_pokemons_alive_coach_2 = copy.copy(temp_list_pokemons_from_coach_2)

    # Choose first pokemons
 

    # Main loop.



    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
