#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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
from weapon_type import WeaponType


class Pokemon():
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = Pokemon(id, pokemon_name, weapon_type, health_points,
                   attack_rating, defense_rating)

    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.

    Attributes
    ----------

    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
    """
    
    # Variable global para guardar la lista de los ID, tal y como se nos pide en el enunciado
    __list_ids = []

    #Definimos el constructor
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):

        #Condional para asegurarnos que el id del pokemon es de tipo int
        if isinstance(pokemon_id, int):
            #Con este condicional nos aseguramos que los ID no se repitan
            if pokemon_id not in Pokemon.__list_ids:
                self._pokemon_id = pokemon_id
                Pokemon.__list_ids.append(self._pokemon_id)
        else:
            raise ValueError("La id debe ser un numero entero")
        
        #Condional para comprobar que el nombre es una cadena de texto
        if isinstance(pokemon_name, str):
            self._pokemon_name = pokemon_name
        else:
            raise TypeError("El nombre del pokemon debe ser una cadena de texto")
        
        #Condional para asegurar que los puntos de salud sean correctos
        if isinstance(health_points, int):
            if 1 <= health_points <= 100:
                self._health_points = health_points
            else:
                raise ValueError("La salud debe estar entre 0 y 100")
        else:
            raise TypeError("health_points debe ser de tipo int")
        
        #Condicional para comprobar que los puntos de ataque son de tipo int y estan entre 0 y 10
        if isinstance(attack_rating, int):
            if 1 <= attack_rating <= 10:
                self._attack_rating = attack_rating
            else:
                raise ValueError("Los puntos de ataque deben estar entre 0 y 10")
        else:
            raise TypeError("attack_rating debe ser de tipo int")
        
        #Condicional para verificar que los puntos de defensa son de tipo int y estan entre 0 y 10
        if isinstance(defense_rating, int):
            if 1 <= defense_rating <= 10:
                self._defense_rating = defense_rating
            else:
                raise ValueError("Los puntos de defensa deben estar entre 0 y 10")
        else:
            raise TypeError("defense_rating debe ser de tipo int")

    #Dfinimos el destructor de la clase Pokemon
    def __del__(self):
        Pokemon.__list_ids.remove(self._pokemon_id)

    #Definimos los getters  
    def get_id(self):
        return self._pokemon_id

    def get_pokemon_name(self):
        return self._pokemon_name

    def get_weapon_type(self):
        return self._weapon_type

    def get_health_points(self):
        return self._health_points

    def get_attack_rating(self):
        return self._attack_rating

    def get_defense_rating(self):
        return self._defense_rating


    #Definimos los setters
    def set_pokemon_name(self, pokemon_name_to_be_set):
        if isinstance(pokemon_name_to_be_set, str):
            self._pokemon_name = pokemon_name_to_be_set
        else:
            raise TypeError("El nombre del pokemon debe sr de tipo string")

    def set_weapon_type(self, weapon_type_to_be_set):
        if isinstance(weapon_type_to_be_set, WeaponType):
            self._weapon_type = weapon_type_to_be_set
        else:
            raise TypeError("weapon_type_to_be_set debe ser un Weapon Type")

    def set_attack_rating(self, attack_rating_to_be_set):
        if isinstance(attack_rating_to_be_set, int):
            if 1 <= attack_rating_to_be_set <= 10:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("Los puntos de ataque deben estar entre 0 y 10")

            raise TypeError("attack_rating_to_be_set debe ser de tipo int")

    def set_defense_rating(self, defense_rating_to_be_set):
        if isinstance(defense_rating_to_be_set, int):
            if 1 <= defense_rating_to_be_set <= 10:
                self._defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("Los puntos de defensa deben estar entre 0 y 10")
        else:
            raise TypeError("defense_rating_to_be_set debe ser de tipo int")


def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
