import json




# path_to_json = "./users.json"
# with open(path_to_json, "r") as handler:
#     info = json.load(handler)

# users = info["users"]
# passwords = info["passwords"]

# print("User 0 '{}', has password '{}'".format(users[1], passwords[1]))


def Login(path,username,password):

    path_to_json = path
    with open(path_to_json, "r") as handler:
            data = json.load(handler)

    for member in data['members']:
        if member['username'] == username and member['password'] == password:
            return True
        else:
            return False

def saveJson(title,data,path):


    with open(path,'r') as js:
        myData = json.load(js)
        print(type(myData["settings"]))
    myData["settings"][title] = data

    with open(path,'w') as js:
        js.write(json.dumps(myData,indent=4,ensure_ascii=False,encoding='utf-8'))
        


def readJson(path,parameter):
    path_to_json = path
    with open(path_to_json, "r") as handler:
            data = json.load(handler)
    for member in data[parameter]:
        print(member)
    return(data[parameter])

