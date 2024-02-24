def my_list_fn():
    my_list = (1, 2, 3)
    my_new_list = list(my_list)
    my_new_list.append(4)
    my_list = tuple(my_new_list)
    print(my_list is my_new_list)
    return my_list


def my_tuple_fn():
    my_tuple = (1, 2, 3)
    new_element = 4
    newer_element = 5
    my_tuple += (new_element, newer_element)
    my_new_tuple = my_tuple
    print(my_tuple is my_new_tuple)
    return my_new_tuple


print(my_tuple_fn(), my_list_fn())
