#!/usr/bin/python3
"""Add item Python"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


list_json = []
if len(sys.argv) > 1:
    arguments = sys.argv[1:]
    list_json = load_from_json_file("add_item.json")
    for element in arguments:
        list_json.append(element)
    save_to_json_file(list_json, "add_item_json")
else:
    save_to_json_file(list_json, "add_item.json")
