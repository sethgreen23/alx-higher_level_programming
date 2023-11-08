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
    for idx, value in enumerate(roman_string):
        idx_valid = (idx - 1 > 0 or idx == 1)
        if (value == 'V') and (roman_string[idx - 1] == 'I') and idx_valid:
            result += rom_dict['V'] - (2 * rom_dict['I'])
        elif (value == 'X') and (roman_string[idx - 1] == 'I') and idx_valid:
            result += rom_dict['X'] - (2 * rom_dict['I'])
        elif (value == 'L') and (roman_string[idx - 1] == 'X') and idx_valid:
            result += rom_dict['L'] - (2 * rom_dict['X'])
        elif (value == 'C') and (roman_string[idx - 1] == 'X') and idx_valid:
            result += rom_dict['C'] - (2 * rom_dict['X'])
        elif (value == 'D') and (roman_string[idx - 1] == 'C') and idx_valid:
            result += rom_dict['D'] - (2 * rom_dict['C'])
        elif (value == 'M') and (roman_string[idx - 1] == 'C') and idx_valid:
            result += rom_dict['M'] - (2 * rom_dict['C'])
        else:
            result += rom_dict[value]
    return (result)
