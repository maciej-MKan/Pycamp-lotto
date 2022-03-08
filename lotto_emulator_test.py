"""Test module for lotto_emulator"""

import lotto_emulator

def test_len_random_generate():
    """sprawdzenie poprawnej ilości losowanych numerów"""
    assert len(lotto_emulator.get_random_numbers()) == 6

def test_random_generate():
    """sprawdzenie losowości numerów"""
    for _ in range(10):
        numbers1 = lotto_emulator.get_random_numbers()
        assert numbers1 != lotto_emulator.get_random_numbers()

def test_len_generate_numbers():
    """sprawdzenie funkcji losuj"""
    assert len(lotto_emulator.validate_numbers_from_user('losuj')) == 6

def test_validate_user_data():
    """sprawdzenie walidacji danych użytkownika"""
    input_data = ['1', '1,2,3,4,5', '1,dwa,3,4,5,6', '1,2,3,4,5,50', '0,1,2,3,4,5']
    for data in input_data:
        assert len(lotto_emulator.validate_numbers_from_user(str(data))) != 6

def test_convert_user_data():
    """sprawdzenie poprawności konwersji danych użytkownia"""
    assert isinstance(lotto_emulator.validate_numbers_from_user('1,2,3,4,5,6'), set)

def test_range():
    """sprawdzenie zakresu przyjmowanych danych"""
    assert lotto_emulator.validate_numbers_from_user('1,2,3,4,5,49') == {1,2,3,4,5,49}

def test_counters_class():
    """sprawdzenie poprawności działania liczników"""
    test_counters = lotto_emulator.HitCounter()
    for i in range(7): #7 because 0 is miss
        test_counters.inc_counter(i)
    for i in test_counters.get_counters():
        if i != 1:
            assert False
    if test_counters.get_total() != 7:
        assert False
    assert True
