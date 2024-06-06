#!/usr/bin/python3
"""JSON"""
import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.isfile(filename):
    list_of_args = load_from_json_file(filename)
else:
    list_of_args = []

list_of_args.extend(sys.argv[1:])
save_to_json_file(list_of_args, filename)
