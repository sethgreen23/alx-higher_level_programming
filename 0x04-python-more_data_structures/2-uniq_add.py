#!/usr/bin/python3
def uniq_add(my_list=[]):
    dic = dict()
    for x in my_list:
        dic[x] = dic.get(x, 1)
    summation = 0
    for x in list(dic.keys()):
        summation += x
    return (summation)
