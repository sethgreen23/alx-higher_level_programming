#!/usr/bin/python3
"""save to json file Module"""


import json


def save_to_json_file(my_obj, filename):
    """Save to json file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
