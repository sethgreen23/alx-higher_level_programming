#!/user/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary.keys())
    for key in keys:
        a_dictionary[key] *= 2
    return (a_dictionary)
