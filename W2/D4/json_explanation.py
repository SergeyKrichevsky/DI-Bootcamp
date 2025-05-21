import json

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Converting a dict to json

my_family = {
    'parants':['Bath', 'Jerry'],
    'children':['Summer', 'Morty']
}

# with open(f"{dir_path}/family.json", "w") as f:
#     json.dump(my_family, f)

json_my_family = json.dumps(my_family)
print(json_my_family)
print(type(json_my_family))

# CONVERT A JSON INTO DICTIONARY

with open(f"{dir_path}/family.json", "r") as f:
    my_family_2 = json.load(f)
    print(my_family_2)
    print(type(my_family_2))


parse_family = json.loads(json_my_family)
# print('parsed from JSON string to ': parse_family)#......\
print('=' * 50)
print(json_my_family)
print(type(json_my_family))
print(parse_family)
print(type(parse_family))

