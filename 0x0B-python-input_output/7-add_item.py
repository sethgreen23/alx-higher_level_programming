#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
from os.path import isfile

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
list_json = []

# can use try except FileNotFoundError list_json = []
if isfile(filename):
    list_json = load_from_json_file(filename)

for arg in argv[1:]:
    list_json.append(arg)

save_to_json_file(list_json, filename)
