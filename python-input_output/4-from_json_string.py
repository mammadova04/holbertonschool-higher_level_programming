#!/usr/bin/python3
"""JSON"""
import json


def from_json_string(my_str):
    """Deserealization"""
    return json.loads(my_str)
