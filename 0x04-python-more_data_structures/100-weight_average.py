#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    sum_product = sum(map(lambda x: x[0] * x[1], my_list))
    sum_second = sum(map(lambda x: x[1], my_list))
    return (sum_product/sum_second)
