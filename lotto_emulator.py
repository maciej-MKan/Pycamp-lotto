"""Skrypt obliczający ile losowych prób trzeba podjąć dla wylosowania 6 użytkownika
Numery podaje użytkownik lub losuje je skrypt"""

import random


class HitCounter:
    """Klasa zliczająca próby wygrane i przegrane w liście
    ['miss', '1-hit', ... ,'6-hit']"""

    def __init__(self) -> None:
        self._counters = [0,0,0,0,0,0,0]
        self.total = 0

    def get_total(self) -> int:
        """zwraca sumę liczników

        Returns:
            int: całkowita ilośc podjętych prób
        """
        for i in self.get_counters():
            self.total += int(i)
        return self.total

    def inc_counter(self, value):
        """zwiększenie liczników wedłóg ilości dopasowaych numerów

        Args:
            value (int in range(0,6)): ilość dopasowanych numerów
        """
        self._counters[value] += 1

    def get_counters(self) -> list:
        """zwraca listę liczników"""
        return self._counters

def get_random_numbers() -> set:
    """wylosowanie 6 różnych liczb z zaktesy 1 - 49
    Funkcja zwraca 6 elementowy set"""

    number_set = set()

    while len(number_set) < 6:
        number_set.add(random.randint(1,49))
    return number_set

def validate_numbers_from_user(user_choice) -> set:
    """sprawdza poprawność dannych podanych przez użytkownika
    6 numerów z zaktesu 1 - 49 lub opcja losuj

    Args:
        user_choice (str): dane podane przez użytkownika

    Returns:
        set: 6 numerów z zakresu 1 - 49 lub opis błędu
    """
    number_set = set()
    err = ''
    err_desc = ''

    if user_choice.lower() == 'losuj':
        number_set = get_random_numbers()
    else:
        try:
            user_choice = user_choice.split(',')
            for enum_user_choice in enumerate(user_choice):
                number_set.add(int(enum_user_choice[1]))
        except TypeError:
            err_desc += "\nPodałeś coś niewłasciwego."
            err = "bad type data"
        except ValueError:
            err_desc += "\nPodałeś coś niewłasciwego."
            err = "bad value data"

        if len(number_set) != 6:
            err_desc += "\nPodałeś niewłaściwą ilość liczb."
            err = "wrong amount"
        else:
            for number in number_set:
                if number not in range(1, 50):
                    err_desc += f"Liczba {number} jest z poza zakresu."
                    err = "not in range"

    if err:
        return {err_desc}
    return number_set



if __name__ == '__main__':
    numbers = set()
    random_numbers = set()
    hit_counter = HitCounter()

    while len(numbers) < 6:
        if numbers:
            print(list(numbers)[0])
        numbers = validate_numbers_from_user(input('''
Podaj 6 różnych liczb z zakresu od 1 do 49. Oddziel je przecinkami
jeśli chcesz wylosowć liczby w systemie Chybił-Trafił wpisz "losuj": \n''')
        )

    print(f"\ntwoje numery to: {numbers} \n")
    print("zaczynamy!")

    while numbers != random_numbers:
        random_numbers = get_random_numbers()
        hit_value = len([i for i in numbers if i in random_numbers])
        hit_counter.inc_counter(hit_value)
        if hit_value > 4:
            print("-", end="", flush=True)

    total = hit_counter.get_total()
    print(f"\npotrzebowałeś {total:,} prób, żeby trafić szustkę")
    print(f"wydałeś na to {total * 3:,} złotych")
    print(f"zajęło ci to {total / 3:,.0f} tygodni")
    print(f"""w międzyczasie trafiłeś:
    {hit_counter.get_counters()[3]:,} trójek
    {hit_counter.get_counters()[4]:,} czwórek
    {hit_counter.get_counters()[5]:,} piątek""")