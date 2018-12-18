'''
FlattenList: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2018, Marco Cipri
Licensed under MIT
'''

from flatten_list import deep_flat
import pytest


def test_example():
    main_list = [[1,2, [3]], 4]
    assert deep_flat(main_list) == [1, 2, 3,4]

def test_complex():
    main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4]]
    assert deep_flat(main_list) == [1,2,21,22,31,32,334,335,3351,3352,3353,336,3361,3362,3363,4]

def test_long():
    main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4,list(range(1000000))]]
    assert deep_flat(main_list) == [1,2,21,22,31,32,334,335,3351,3352,3353,336,3361,3362,3363,4,list(range(1000000))]

def test_passes():
    with pytest.raises(Exception) as e_info:
        main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4, "33",list(range(1000000))]]
        deep_flat(main_list) 