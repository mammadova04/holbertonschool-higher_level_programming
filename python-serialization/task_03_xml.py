#!/usr/bin/env python3

"""
The ''3. Serializing and Deserializing with XML'' module
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize_to_xml - function to take a
    Python dictionary and a filename as parameters.
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    deserialize_from_xml - function to take a filename
    as its parameter, read the XML data from that file,
    """
    data = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        data[child.tag] = child.text
    return data
