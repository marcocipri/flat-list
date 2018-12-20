'''
FlattenList: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2018, Marco Cipri
Licensed under MIT

unit test devoted for private module's functions 
'''

from flatten_list.flatten import atom_flat
from flatten_list.flatten import check_iterator
from flatten_list.flatten import concat_element
from flatten_list.flatten import concat_flat_list


import pytest


def test_check_iterator_true():
        _element = [[1,2, [3]], 4]
        assert check_iterator(_element) == True

def test_check_iterator_int():
        _element = 1
        assert check_iterator(_element) == False

def test_check_iterator_string():
    with pytest.raises(Exception) as e_info:
        _element = '1'
        check_iterator(_element)

def test_check_iterator_list():
        _element = [['1','2', ['3']], '4']
        assert check_iterator(_element) == True

def test_concat_flat_complex_list():
        _element_list = [[1,2, [3]], 4]
        _main_list = [-1,0]
        assert concat_flat_list(_element_list, _main_list) == [-1, 0, [1, 2, [3]], 4]

def test_concat_flat_simple_list():
        _element_list = [2]
        _main_list = [-1,0]
        assert concat_flat_list(_element_list, _main_list) == [-1, 0, 2]

def test_concat_simple_int():
        _element_list = 2
        _main_list = [-1,0]
        assert concat_element(_element_list,_main_list) == [-1, 0, 2]

def test_concat_atom_00():
        _main_list = [1]
        assert atom_flat(_main_list) == (False, [1])

def test_concat_atom_01():
        _main_list = [1,0]
        assert atom_flat(_main_list) == (False, [1, 0])

def test_concat_atom_02():
        _main_list = [1,[2,3]]
        assert atom_flat(_main_list) == (True, [1, 2,3])

def test_concat_atom_03():
        _main_list = [1,[2,3,[4,5]]]
        assert atom_flat(_main_list) == (True, [1,2,3,[4,5]])

def test_concat_atom_04():
    with pytest.raises(Exception) as e_info:
        _main_list = ['d',[2,3,['c',5]]]
        atom_flat(_main_list)

def test_concat_atom_05():
        _main_list = [1,['a','b',[4,5]]]
        assert atom_flat(_main_list) == (True, [1,'a','b',[4,5]])