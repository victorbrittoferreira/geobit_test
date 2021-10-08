import json 


def ler_json():
    try:
        data = None
        with open('/home/kurt/GitHub/geobit_test/data.json') as json_file:   
            data = json.load(json_file)
        
        return data
    
    except:
        return print("There was a problem executing the 'ler_son' function from the leitura file.  ")
    

