import json 


def ler_json() -> dict:

    """This function takes a file json type 
    and transforms and return it into a dictionary. 
    """

    try:
        data = None
        with open('/home/kurt/GitHub/geobit_test/data.json') as json_file:   
            data = json.load(json_file)
        
        return data
    
    except:
        return print(
            "There was a problem executing the'ler_son' function from the leitura file")
    

