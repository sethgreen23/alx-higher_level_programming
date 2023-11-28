#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, "counter", 0)
    return "BestSchool, " * (magic_string.n - 1) + "BestSchool"
