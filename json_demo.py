# JavaScript Object Notation 

import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", ""],
            "has_license": true
        },
        {
            "name": "",
            "phone": "",
            "emails": [uyy],
            "has_license": null
        }
    ]
}
'''
print(type(people_string))
# json.loads() is  responsible for converting a JSON-formatted string
# into a Pyhton data structure, allowing you to work with the JSON data using native Python type 
#   a  dictionary
data = json.loads(people_string)
print(data)
print(type(data['people']))
print(type(data))



