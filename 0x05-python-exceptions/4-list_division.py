#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    list_num = []
    for initial in range(0, list_length):
        try:
            divide_num = my_list_1[initial] / my_list_2[initial]
        except TypeError:
            print("wrong type")
            divide_num = 0
        except ZeroDivisionError:
            print("division by 0")
            divide_num = 0
        except IndexError:
            print("out of range")
            divide_num = 0
        finally:
            list_num.append(divide_num)
    return (list_num)

