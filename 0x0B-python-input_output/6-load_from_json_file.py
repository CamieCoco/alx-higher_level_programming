#!/usr/bin/python3
"""
 function that creates an Object from JSON :
"""
import json


def load_from_json_file(filename):
    """
    You must use the with statement
    ou t need to manage exceptions if the JSON string t
    represent an object.
    """
    with open(filename, mode="r") as myFile:
        return(json.load(myFile)) 
