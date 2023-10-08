# =============================================================================
# Title             PyHacks - Classes  - Javascript Object Notation (JSON)
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================

import json

# Convert JSON to Python

json_obj = '{"name": "Gary", "age": 38, "city": "Nottingham", "country": "England"}'
# Parse to Python
pythjson = json.loads(json_obj)
# The result is a Python Diction
for key, value in pythjson.items():
    print("The dictionary key is: {} and the value is: {}".format(key, value))
# Access single element
print(pythjson["name"])

# Convert Python to JSON
py_dict = {
    "name": "Gary",
    "age": 38,
    "city": "Nottingham"
    }

jsonify = json.dumps(py_dict)
print(jsonify)

# JSON package allows for the conversion of 
# - dict
# - list
# - tuple
# - string
# - int
# - float
# - Boolean (True and False)
# - None

# All types utilised

details = {
    "name": "Gary", 
    "age": 39,
    "married": True,
    "children": ("Charlie", "Benjamin"),
    "money_end_of_month": None,
    "roles": [
        {"role_name": "Senior Data Scientist", "works_weekends": False},
        {"role_name": "Co-chair of NHS R Community", "works_weekends": False}]
    }

print(json.dumps(details))

# To make this easier to read you can use the indents

json.dumps(details, indent=4, separators=(". ", " = "), sort_keys=True)