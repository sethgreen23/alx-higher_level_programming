#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    result = 0
    for i in range(list_length):
        try:
            if not (isinstance(my_list_1[i], (int, float)) and
		    isinstance(my_list_2[i], (int, float))):
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result = my_list_1[i] / my_list_2[i]
            res_list.append(result)
        except TypeError as e:
            res_list.append(0)
            print(e)
        except ZeroDivisionError as e:
            res_list.append(0)
            print(e)
        except IndexError:
            res_list.append(0)
            print("out of range")
        finally:
            res_list.append(result)
    return res_list
