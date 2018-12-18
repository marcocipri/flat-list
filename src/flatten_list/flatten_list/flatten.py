from iteration_utilities import deepflatten


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


def req_flat(lst):
	return sum( ([x] if not isinstance(x, list) else req_flat(x)
		     for x in lst), [] )

'''tail recursive by lambda... too slow'''
flatten=lambda l: sum(map(flatten,l),[]) if isinstance(l,list) else [l]


main_list = [1,2,[21,22],[31,32,[334,335, [3351,3352,3353],336,[3361,3362,3363]],4, 33,list(range(1000000))]]
#main_list = [[1,2, [3]], 4]
print('flatted ' + str(deep_flat(main_list)))

print('flatted req ' + str(list(deepflatten(main_list))))

print('flatted lambda ' + str(list(flatten(main_list))))
