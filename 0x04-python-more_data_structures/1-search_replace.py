#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_check = list(map(lambda check: replace if check == search else check, my_list))
    return (list_check)

