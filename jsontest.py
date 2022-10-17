import json
  
# Opening JSON file
f = open('settings.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list

# print(data['settings']['ocak1'][0]["volttage"])
# print(data['settings']['ocak2'][0]["volttage"])
for member in data['settings']:
    print(member)
# Closing file
f.close()