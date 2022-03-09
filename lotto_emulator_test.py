#!/usr/bin/env pytest

"""Test module for lotto_emulator"""

import lotto_emulator

def test_len_random_generate():
    """checking the correct number of drawn numbers"""
    assert len(lotto_emulator.get_random_numbers()) == 6

def test_random_generate():
    """checking the randomness of numbers"""
    for _ in range(10):
        numbers1 = lotto_emulator.get_random_numbers()
        assert numbers1 != lotto_emulator.get_random_numbers()

def test_len_generate_numbers():
    """checking the random function"""
    _, numbers = lotto_emulator.validate_numbers_from_user('losuj')
    assert len(numbers) == 6

def test_validate_user_data():
    """checking the validation of user data"""
    input_data = ['1', '1,2,3,4,5', '1,dwa,3,4,5,6', '1,2,3,4,5,50', '0,1,2,3,4,5']
    for data in input_data:
        assert len(lotto_emulator.validate_numbers_from_user(str(data))) != 6

def test_convert_user_data():
    """checking the correctness of user data conversion"""
    _, numbers = lotto_emulator.validate_numbers_from_user('1,2,3,4,5,6')
    assert isinstance(numbers, set)

def test_range():
    """checking the scope of received data"""
    _, numbers = lotto_emulator.validate_numbers_from_user('1,2,3,4,5,49')
    assert  numbers == {1,2,3,4,5,49}

def test_counters_class():
    """checking the correct operation of the counters"""
    test_counters = lotto_emulator.HitCounter()
    for i in range(7): #7 because 0 is miss
        test_counters.inc_counter(i)
    for i in test_counters.get_counters():
        if i != 1:
            assert False
    if test_counters.get_total() != 7:
        assert False
    assert True
