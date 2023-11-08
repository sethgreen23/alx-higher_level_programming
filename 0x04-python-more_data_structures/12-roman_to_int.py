#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    rom_dict = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
    result = 0
    for index, value in enumerate(roman_string):
        if (value == 'V') and (roman_string[index - 1] == 'I'):
            result += rom_dict['V'] - (2 * rom_dict['I'])
        elif (value == 'X') and (roman_string[index - 1] == 'I'):
            result += rom_dict['X'] - (2 * rom_dict['I'])
        elif (value == 'L') and (roman_string[index - 1] == 'X'):
            result += rom_dict['L'] - (2 * rom_dict['X'])
        elif (value == 'C') and (roman_string[index - 1] == 'X'):
            result += rom_dict['C'] - (2 * rom_dict['X'])
        elif (value == 'D') and (roman_string[index - 1] == 'C'):
            result += rom_dict['D'] - (2 * rom_dict['C'])
        elif (value == 'M') and (roman_string[index - 1] == 'C'):
            result += rom_dict['M'] - (2 * rom_dict['C'])
        else:
            result += rom_dict[value]
    return (result)
