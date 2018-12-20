
def check_iterator(element):

    """checks if the element is a list 
    Args:
        element : 

    Returns:
        bool: True if element is a loist, False otherwise.

    Examples:
        see unit test (basic_test.py)
    """
    checks = {"<class 'int'>":False,"<class 'list'>":True}
    return checks[str(type(element))]

def concat_flat_list(element_list, main_list):

    """ concatenate the elements the flat list in the main list 
    Args:
        element_list : list which contains 
        main_list : list to be enrich

    Returns:
        list : the main_list enriched 

    Examples:
        see unit test (basic_test.py)
    """

    for _element in element_list:
        main_list.append(_element)
    return main_list

def concat_element(element, main_list):
    """ conatenate simple element in main list
    Args:
        element : element to be appended to the main_list
        main_list : list to be enrich

    Returns:
        list : enriched list.

    Examples:
        see unit test (basic_test.py)
    """
    main_list.append(element)
    return main_list


def atom_flat(the_list):
    """ scans the list and ironing , foreach simple elemnt, checks if is an admitted type (int) 
    Args:
        element_list : 
        main_list :

    Returns:
        bool: True if element is a loist, False otherwise.
 
    Examples:
        see unit test (basic_test.py)
    """
    _has_to_reiterate = False
    _main_list=[]
    for _element in the_list:
        if check_iterator(_element):
            _has_to_reiterate = True
            _main_list = concat_flat_list(_element,_main_list)
        else:
            _main_list=concat_element(_element,_main_list)
    return _has_to_reiterate, _main_list    

def deep_flat(main_list):
    """ concatenate simple element in main list
        solving this problem I've began with a tail recursive approach but, at least for Python,
        I switched to this 'no recursive' solution because poor performance
    Args:
        element_list : 
        main_list :

    Returns:
        bool: True if element is a loist, False otherwise.

 
    Examples:
        see unit test (module_test.py)
    """
    _has_to_reiterate = True
    _flatten_list = main_list
    while _has_to_reiterate:
        _the_list = _flatten_list
        _flatten_list = []
        _has_to_reiterate, _flatten_list =  atom_flat(_the_list)
    return _flatten_list



print(atom_flat([1,2,3]))