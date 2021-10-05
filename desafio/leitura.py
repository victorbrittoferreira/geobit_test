import json 


def ler_json():
    data = None
    with open('data.json') as json_file:   
        data = json.load(json_file)
  
    return data
