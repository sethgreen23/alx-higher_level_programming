def isuppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
