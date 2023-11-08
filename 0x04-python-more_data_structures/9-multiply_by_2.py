#!/user/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    keys = list(new_dict.keys())
    for key in keys:
        new_dict[key] *= 2
    return (new_dict)
