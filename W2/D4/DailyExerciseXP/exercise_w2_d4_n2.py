import json

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

print(data["company"]["employee"]["payable"]["salary"])

data["company"]["employee"]["birth_date"] = "YYYY-MM-DD"
data["company"]["employee"]["birth_date"] = "1990-05-15"

with open(f'{dir_path}/sampleJson.json', 'w') as json_file:
    json.dump(data, json_file, indent=2, sort_keys= True)

