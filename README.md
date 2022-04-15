# Examen_Parcial_Pokemon

[Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Examen_Parcial_Pokemon.git)

*Queda resuelto el examen propuesto la semana pasada, utilizando la programacion orientada a objetos de python. Para la resolucion me he guiado por la solucion colgada en el portal de la asignatura.*

--- 

## Indice
* [main](#1)
* [pokemon](#2)
* [pokemon_air](#3)
* [pokemon_earth](#4)
* [pokemon_electricity](#5)
* [pokemon_water](#6)
* [weapon_type](#7)

---

## main.py<a name="1"></a>
```python3
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
    print("Entrenador 1 elija su primer pokemon")
    temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons("Introduzca el id del pokemon: ", list_pokemons_alive_coach_1)
    print("Entrenador 2 elija su primer pokemon")
    temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons("Introduzca el id del pokemon: ",list_pokemons_alive_coach_2)


    # Main loop.
    while(coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):

        if not temp_pokemon_coach_1.is_alive():
            # Seleccionamos un nuevo pokemon
            print("Entrenador 1 su pokemon: " + str(temp_pokemon_coach_1) + " ha sido debilitado. Por favor elija su nuevo pokemon para combatir")
            list_pokemons_alive_coach_1.remove(temp_pokemon_coach_1)
            temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons("Introduzca el id del pokemon", list_pokemons_alive_coach_1)
        if not temp_pokemon_coach_2.is_alive():
            # Seleccona un nuevo pokemon
            print("Entrenador 2 su pokemon: " + str(temp_pokemon_coach_2) + " ha sido debilitado. Por favor elija su nuevo pokemon para combatir")
            list_pokemons_alive_coach_2.remove(temp_pokemon_coach_2)
            temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons("Introduzca el id del pokemon", list_pokemons_alive_coach_2)

        print("pokemon from Game User 1 attacks.")
        temp_pokemon_coach_1.fight_attack(temp_pokemon_coach_2)
        print("pokemon from Game User 2 attacks.")
        temp_pokemon_coach_2.fight_attack(temp_pokemon_coach_1)


    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")

    print("Game User 1:")
    #Mostramos por pantalla los pokemon no debilitados dl primer usuario
    for temp_pokemon in temp_list_pokemons_from_coach_1:
        print(temp_pokemon)

    print("Game User 2:")
    #Mostramos por pantalla los pokemon no debilitados del segundo usuario
    for temp_pokemon in temp_list_pokemons_from_coach_2:
        print(temp_pokemon)



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
```
---
## pokemon.py<a name="2"></a>
```python3
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

    #Definimos un metodo para saber si el pokemon esta vivo, es decir, si sus puntos de salud son distintos de 0
    def is_alive(self):
        return not bool(self._health_points == 0)

    #Definimos otro metodo, para simular el ataque de los Pokemon
    def fight_attack(self, pokemon_to_attack):
        points_of_damage = self._attack_rating

        print("El Pokemon" + self._pokemon_name +
              " golpea al Pokemon " + pokemon_to_attack.get_pokemon_name() +
              " con " + str(points_of_damage) + " puntos de daño!")

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit

    #Definimos la funcion fight_defense, para simular el daño que recibe el Pokemon, es decir, la defensa
    def fight_defense(self, points_of_damage):
        if not isinstance(points_of_damage, int):
            raise TypeError("points_of_damage debe ser de tipo int")

        print("El Pokemon " + self._pokemon_name +
              " ha recibido un ataque de " +
              str(points_of_damage) + " puntos de daño.")

        if points_of_damage > self._defense_rating:
            self._health_points = (self._health_points -
                                   (points_of_damage - self._defense_rating))
            pokemon_was_hit = True
        else:
            print("No se recibio daño.")
            pokemon_was_hit = False

        # Si un Pokemon qued con salud negativa, le damos el valor 0 para dar a entender que se ha derrotado al Pokemon
        if self._health_points < 1:
            self._health_points = 0

        return pokemon_was_hit

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
```
---
## pokemon_air.py<a name="3"></a>
```python3
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
from pokemon import Pokemon
from weapon_type import WeaponType

import random

class PokemonAir(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = PokemonAir(id, pokemon_name, weapon_type, health_points,
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
      >>> obj_Pokemon = PokemonEarth(1, "Pidgey", WeaponType.PUNCH, 100, 7, 10)
    """
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        #Heredamos del constructor de Pokemon ya que esta clase esta heredada
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)

    def fight_defense(self, points_of_damage):
        if not isinstance(points_of_damage, int):
            raise TypeError("Los puntos de daño deben ser un numero entero")

        print("El pokemon " + self._pokemon_name +
              " ha recibido un ataque de " +
              str(points_of_damage) + " puntos de daño.")

        failure_probability = random.randrange(0, 2)

        #Si la probabilidad de fallar es 0, el pokemon recibe el ataque
        if failure_probability == 0:
            if points_of_damage > self._defense_rating:
                self._health_points = (self._health_points -
                                       (points_of_damage - self._defense_rating))
                pokemon_was_hit = True
            else:
                print("No se ha recibido daño")
                pokemon_was_hit = False
                
        #De otra manera, no se recibe el golpe
        else:
            print("No se ha recibido daño")
            pokemon_was_hit = False

        # Si un Pokemon qued con salud negativa, le damos el valor 0 para dar a entender que se ha derrotado al Pokemon
        if self._health_points < 1:
            self._health_points = 0

        return pokemon_was_hit


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
    pokemon_1 = PokemonAir(1, "Pidgey", WeaponType.HEADBUTT, 100, 8, 7)

    if pokemon_1.get_pokemon_name() == "Pidgey":
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

    if pokemon_1.get_defense_rating() == 7:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonAir(7, "Pidgey", WeaponType.HEADBUTT, 100, 7, 6)

    if str(pokemon_2) == "Pokemon ID 7 with name Pidgey has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonAir(3, "Pidgey", WeaponType.KICK, 97, 8, 7)

    if pokemon_3.is_alive():
        pokemon_was_hit = pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
        else:
            if pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
            
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonAir(4, "Pidgey", WeaponType.ELBOW, 93, 9, 5)

    pokemon_was_hit = pokemon_4.fight_defense(70)

    if pokemon_was_hit:
        if pokemon_4.get_health_points() == 28:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")
    else:
        if pokemon_4.get_health_points() == 93:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonAir(5, "Pidgey", WeaponType.PUNCH, 99, 10, 8)
    pokemon_6 = PokemonAir(6, "Pidgey", WeaponType.PUNCH, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 95:
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
```
---
## pokemon_earth.py<a name="4"></a>
```python3
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
from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonEarth(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = PokemonEarth(id, pokemon_name, weapon_type, health_points,
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
      >>> obj_Pokemon = PokemonEarth(1, "Diglett", WeaponType.PUNCH, 100, 7, 10)
    """


    #Constructor
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        #Importamos el constructor de Pokemon, ya que PokemonEarth esta heredada de Pokemon
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, 10)
        #Nos aseguramos que la defensa este entre 11 y 20, tal y como se especifica en el enunciado
        if isinstance(defense_rating, int):
            if 11 <= defense_rating <= 20:
                self._defense_rating = defense_rating
            else:
                raise ValueError("La defensa debe estar entre 11 y 20")
        else:
            raise TypeError("La defensa debe ser de tipo int")


    #Definimos un setter
    def set_defense_rating(self, defense_rating_to_be_set):
        #Condional para asegurarnos que la defensa esta entre 11 y 20
        if isinstance(defense_rating_to_be_set, int):
            if 11 <= defense_rating_to_be_set <= 20:
                self._defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("La defensa debe estar entre 11 y 20.")
        else:
            raise TypeError("La defensa debe ser de tipo int")



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
    pokemon_1 = PokemonEarth(1, "Diglett", WeaponType.HEADBUTT, 100, 8, 15)

    if pokemon_1.get_pokemon_name() == "Diglett":
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

    if pokemon_1.get_defense_rating() == 15:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonEarth(7, "Diglett", WeaponType.HEADBUTT, 100, 7, 12)

    if str(pokemon_2) == "Pokemon ID 7 with name Diglett has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonEarth(3, "Diglett", WeaponType.KICK, 97, 8, 15)

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
    pokemon_4 = PokemonEarth(4, "Diglett", WeaponType.ELBOW, 93, 9, 11)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 34:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonEarth(5, "Diglett", WeaponType.PUNCH, 99, 10, 20)
    pokemon_6 = PokemonEarth(6, "Diglett", WeaponType.PUNCH, 99, 9, 18)

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
```
---
## pokemon_electricity.py<a name="5"></a>
```python3
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
from pokemon import Pokemon
from weapon_type import WeaponType

import random

class PokemonElectricity(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = PokemonElectricity(id, pokemon_name, weapon_type, health_points,
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
      >>> obj_Pokemon = PokemonEarth(1, "Pikachu", WeaponType.PUNCH, 100, 7, 10)
    """

    #Constructor
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        #Heredamos del constructor de Pokemon ya que esta clase esta heredada
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)

    #Metodo fight attack
    def fight_attack(self, pokemon_to_attack):

        points_of_damage = self._attack_rating

        print("El pokemon " + self._pokemon_name +
              " golpea al pokemon " + pokemon_to_attack.get_pokemon_name() +
              " con " + str(points_of_damage) + " puntos de daño!")

        hit_probability = random.randrange(0, 2)

        #Si hit_probability es 0, se aplica un ataque normal
        if hit_probability == 0:
            points_of_damage = self._attack_rating
        #De otra manera, se aplican las restricciones del enunciado
        else:
            points_of_damage = 2 * self._attack_rating

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit


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
    pokemon_1 = PokemonElectricity(1, "Pikachu", WeaponType.HEADBUTT, 100, 8, 7)

    if pokemon_1.get_pokemon_name() == "Pikachu":
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

    if pokemon_1.get_defense_rating() == 7:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonElectricity(7, "Pikachu", WeaponType.HEADBUTT, 100, 7, 6)

    if str(pokemon_2) == "Pokemon ID 7 with name Pikachu has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonElectricity(3, "Pikachu", WeaponType.KICK, 97, 8, 7)

    if pokemon_3.is_alive():
        pokemon_was_hit = pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
        else:
            if pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonElectricity(4, "Pikachu", WeaponType.ELBOW, 93, 9, 5)

    pokemon_was_hit = pokemon_4.fight_defense(70)

    if pokemon_was_hit:
        if pokemon_4.get_health_points() == 28:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")
    else:
        if pokemon_4.get_health_points() == 93:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonElectricity(5, "Pikachu", WeaponType.PUNCH, 99, 10, 8)
    pokemon_6 = PokemonElectricity(6, "Pikachu", WeaponType.PUNCH, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if (pokemon_6.get_health_points() == 95) or (pokemon_6.get_health_points() == 85):
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
```
---
## pokemon_water.py<a name="6"></a>
```python3
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
from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonWater(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = PokemonWater(id, pokemon_name, weapon_type, health_points,
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
      >>> obj_Pokemon = PokemonWater(1, "Squirtle", WeaponType.PUNCH, 100, 7, 10)
    """

    #Definimos el constructor de los pokemon de tipo agua
    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        #Heredamos el constructor de la clase Pokemon
        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         10, defense_rating)

        #Condional para verificar que el ataque esta entre 11 y 20, tal y como se especifica en el enunciado
        if isinstance(attack_rating, int):
            if 11 <= attack_rating <= 20:
                self._attack_rating = attack_rating
            else:
                raise ValueError("El ataque debe ser entre 11 y 20")
        else:
            raise TypeError("El ataque debe ser un numero entero")
    
    #Establecemos un setter para attack_rating
    def set_attack_rating(self, attack_rating_to_be_set):
        if isinstance(attack_rating_to_be_set, int):
            if 11 <= attack_rating_to_be_set <= 20:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("El ataque debe ser entre 11 y 20")
        else:
            raise TypeError("El ataque debe ser un numero entero")



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
    pokemon_1 = PokemonWater(1, "Squirtle", WeaponType.HEADBUTT, 100, 12, 8)

    if pokemon_1.get_pokemon_name() == "Squirtle":
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

    if pokemon_1.get_attack_rating() == 12:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 8:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonWater(7, "Squirtle", WeaponType.HEADBUTT, 100,15, 7)

    if str(pokemon_2) == "Pokemon ID 7 with name Squirtle has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonWater(3, "Squirtle", WeaponType.KICK, 97, 15, 8)

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
    pokemon_4 = PokemonWater(4, "Squirtle", WeaponType.ELBOW, 93, 11, 9)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 32:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonWater(5, "Squirtle", WeaponType.PUNCH, 99, 20, 10)
    pokemon_6 = PokemonWater(6, "Squirtle", WeaponType.PUNCH, 99, 18, 9)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 88:
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
```
---
## weapon_type.py<a name="7"></a>
```python3
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the Enum WeaponType, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  weapon_type.py
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
from enum import Enum


class WeaponType(Enum):
    """Python class to implement an enumeration for the attribute Weapon Type.

    This Python class implements an enumeration for the attribute Weapon Type.

    Syntax
    ------
      obj = WeaponType.Enum

    Parameters
    ----------

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class WeaponType.

    Attributes
    ----------

    Example
    -------
      >>> from weapon_type import WeaponType
      >>> obj_WeaponType = WeaponType.Boxer
    """
    #Funcion para comprobar que weapon type es uno de los 4 tipos que nos dice el enunciado
    def from_str(str_weapon_type):
      if str_weapon_type == 'punch':
          return WeaponType.PUNCH
      elif str_weapon_type == 'kick':
          return WeaponType.KICK
      elif str_weapon_type == 'elbow':
          return WeaponType.ELBOW
      elif str_weapon_type == 'headbutt':
          return WeaponType.HEADBUTT
      else:
          raise TypeError(str_weapon_type + " no se corresponde con ningun tipp")



def main():
    """Function main of the module.

    The function main of this module is used to test the Class WeaponType.

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
    print("Test Case 1: Check Class WeaponType - Name.")
    print("=================================================================.")

    if isinstance(WeaponType.PUNCH, WeaponType):
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.KICK, WeaponType):
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.ELBOW, WeaponType):
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.HEADBUTT, WeaponType):
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class WeaponType - Value.")
    print("=================================================================.")

    if WeaponType.PUNCH.value == 2:
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.KICK.value == 4:
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.ELBOW.value == 6:
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.HEADBUTT.value == 10:
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
```
