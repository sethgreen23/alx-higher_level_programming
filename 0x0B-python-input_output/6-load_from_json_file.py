#!/usr/bin/python3
"""Load from json file Module"""


import json


def load_from_json_file(filename):
    """Load from json file"""

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
