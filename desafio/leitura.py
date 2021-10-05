import json 


def ler_json():
    data = None
    with open('/home/kurt/GitHub/geobit_test/data.json') as json_file:   
        data = json.load(json_file)
  
    return data
