'''
FlattenList: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2018, Marco Cipri
Licensed under MIT
'''

from iteration_utilities import deepflatten
from flatten_list import deep_flat
import pytest


def test_example():
    main_list = [[1,2, [3]], 4]
    assert deep_flat(main_list) == [1, 2, 3,4]

def test_complex():
    main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4]]
    assert deep_flat(main_list) == [1,2,21,22,31,32,334,335,3351,3352,3353,336,3361,3362,3363,4]
    
def test_string():
    with pytest.raises(Exception) as e_info:
        main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4, "33",list(range(100))]]
        deep_flat(main_list) 

def test_char():
    with pytest.raises(Exception) as e_info:
        main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4, s ,list(range(100))]]
        deep_flat(main_list) 


def test_dict():
    with pytest.raises(Exception) as e_info:
        main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4, {6,7} ,list(range(100))]]
        deep_flat(main_list) 

def test_float():
    with pytest.raises(Exception) as e_info:
        main_list = [1,2,[21,22],[31,3.2,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4 ,list(range(100))]]
        deep_flat(main_list) 

def test_long_list():
    main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4,list(range(100))]]
    assert deep_flat(main_list) == list(deepflatten(main_list))


def test_more_long_string():
    main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4,list(range(100))]]
    assert deep_flat(main_list) == list(deepflatten(main_list))

def test_extremely_long_string():
    main_list = [1,2,[21,22],[31,32,[334,list(range(20000,30000)), [3351,3352,3353],list(range(10000,20000)),[3361,list(range(220000,230000)),3363]],4,list(range(40000,60000))]]
    assert deep_flat(main_list) == list(deepflatten(main_list))