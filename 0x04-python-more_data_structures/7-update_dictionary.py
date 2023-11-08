#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not type(key) == 'str':
        key = str(key)
    if not key in a_dictionary:
        a_dictionary.update({key : value})
    else:
        a_dictionary[key] = value
    return (a_dictionary)
