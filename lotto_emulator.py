#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

"""A script that calculates how many random attempts are required to select a 6 user
The numbers are provided by the user or randomly selected by the script"""

import random


class HitCounter:
    """Class that counts attempts won and lost in a list
    ['miss', '1-hit', ... ,'6-hit']"""

    def __init__(self) -> None:
        self._counters = [0,0,0,0,0,0,0]

    def get_total(self) -> int:
        """returns the sum of the counters
        Returns:
            int: total number of attempts made
        """
        return sum(self._counters)

    def inc_counter(self, value):
        """increasing the counters according to the number of matching numbers

        Args:
            value (int in range(0,6)): number of matched numbers
        """
        self._counters[value] += 1

    def get_counters(self) -> list:
        """returns a list of counters"""
        return self._counters

def get_random_numbers() -> set:
    """drawing 6 different numbers from ranges 1 - 49
    The function returns a 6-element set"""

    number_set = set()

    while len(number_set) < 6:
        number_set.add(random.randint(1,49))
    return number_set

def validate_numbers_from_user(user_choice) -> set:
    """validates the data provided by the user
    6 numbers from 1 - 49 or the random option

    Args:
        user_choice (str): data provided by the user

    Returns:
        str: description of errors in user data,
        set: 6 numbers from 1 - 49 or error description
    """
    number_set = set()
    err_desc = ''

    if user_choice.lower() == 'losuj':
        number_set = get_random_numbers()
    else:
        try:
            user_choice = user_choice.split(',')
            for number in user_choice:
                number_set.add(int(number))
        except TypeError:
            err_desc += "\nPodałeś coś niewłasciwego. "
        except ValueError:
            err_desc += "\nPodałeś coś niewłasciwego. "

        if len(number_set) != 6:
            err_desc += "\nPodałeś niewłaściwą ilość liczb. "
        else:
            for number in number_set:
                if number not in range(1, 50):
                    err_desc += f"\nLiczba {number} jest z poza zakresu. "
    if err_desc:
        number_set = set()
    return err_desc, number_set



if __name__ == '__main__':
    numbers = set()
    random_numbers = set()
    hit_counter = HitCounter()

    while len(numbers) < 6:
        err, numbers = validate_numbers_from_user(input('''
Podaj 6 różnych liczb z zakresu od 1 do 49. Oddziel je przecinkami
jeśli chcesz wylosowć liczby w systemie Chybił-Trafił wpisz "losuj": \n''')
        )
        print(err)

    print(f"twoje numery to: {numbers} \n")
    print("zaczynamy!")

    while numbers != random_numbers:
        random_numbers = get_random_numbers()
        hit_value = len(numbers.intersection(random_numbers))
        hit_counter.inc_counter(hit_value)
        if hit_value > 4:
            print("-", end="", flush=True)

    total = hit_counter.get_total()
    hits = hit_counter.get_counters()
    print(f"\npotrzebowałeś {total:,} prób, żeby trafić szustkę")
    print(f"wydałeś na to {total * 3:,} złotych")
    print(f"zajęło ci to {total / 3:,.0f} tygodni")
    print(f"""w międzyczasie trafiłeś:
    {hits[3]:,} trójek
    {hits[4]:,} czwórek
    {hits[5]:,} piątek""")
