#!/usr/bin/python3
"""Add item Python"""


import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


list_json = []
arguments = sys.argv[1:]
if os.path.isfile("add_item.json"):
    list_json = load_from_json_file("add_item.json")
for element in arguments:
    list_json.append(element)
save_to_json_file(list_json, "add_item.json")
