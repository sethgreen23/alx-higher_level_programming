#!/usr/bin/python3
"""Add item Python"""


from sys import argv
from os.path import isfile
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
list_json = []
arguments = argv[1:]
if isfile(filename):
    list_json = load_from_json_file(filename)
for element in arguments:
    list_json.append(element)
save_to_json_file(list_json, filename)
