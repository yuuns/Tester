from encodings import utf_8
import json

ocak4 = {
            "voltage": [1,1,1,1,1,1,1,0,0,1,1],
                "current": [1,1,1,0,0,1,1,1,1,1,1],
                "voltageDescription": ["1","2","3","4","5","6","7","8","9","10","11"],
                "temp": [1,1,1,1,1,1,1,1,1,1,1],
                "tempDescription": ["1","2","3","4","5","6","7","8","9","10","11"],
                "time": 100
        }

with open('json_data.json','r') as js:
    myData = json.load(js)
print(type(myData["settings"]))

yeniOcakAdi = "ocak6"
myData["settings"][yeniOcakAdi] = ocak4

with open('json_data.json','w') as js:
    js.write(json.dumps(myData,indent=4))
