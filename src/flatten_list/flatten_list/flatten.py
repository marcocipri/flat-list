''' checks if the element is a list '''
def check_iterator(element):
    return isinstance(element, (list,))

''' concatenate the flat list in the main list ''' 
def concat_flat_list(element_list, main_list):
    for _element in element_list:
        main_list.append(_element)
    return main_list

''' conatenate simple element in main list '''
def concat_element(element, main_list):
    main_list.append(element)
    return main_list


def atom_flat(the_list):
    _has_to_reiterate = False
    _main_list=[]
    for _element in the_list:
        if check_iterator(_element):
            _has_to_reiterate = True
            _main_list = concat_flat_list(_element,_main_list)
        else:
            if not isinstance(_element, (int)):
                raise Exception(' only int type allowed ')
            _main_list=concat_element(_element,_main_list)
    return _has_to_reiterate, _main_list    

'''my solution, pretty fast!'''
def deep_flat(main_list):
    _has_to_reiterate = True
    while _has_to_reiterate:
        _the_list = main_list
        main_list = []
        _has_to_reiterate, main_list =  atom_flat(_the_list)
    return main_list



