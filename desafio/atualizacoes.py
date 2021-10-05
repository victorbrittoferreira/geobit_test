from copy import deepcopy
from datetime import datetime, date
import time
from typing import List

from leitura import ler_json

import pdb

data = deepcopy(ler_json())

#def atualiza_nascimento_timestamp_para_date_string(data: List[dict]) -> List[dict]:
def atualiza_nascimento_timestamp_para_date_string():
    #data = deepcopy(ler_json())
    #data = deepcopy(data)
   
    for key, _ in enumerate (data['pessoas']):

        birth_timestamp = data['pessoas'][key]['nascimento']
        #birth_converted = time.strftime(' %d/%m/%Y ', (time.localtime (int (birth_timestamp))))
        
        birth_converted = date.fromtimestamp(birth_timestamp)
        #print(type(birth_converted))
        
        data['pessoas'][key]['nascimento'] = birth_converted

    print(type( data['pessoas'][key]['nascimento'])) 
    return data
    #return {}

#print(atualiza_nascimento_timestamp_para_date_string (List[dict]))
print(atualiza_nascimento_timestamp_para_date_string ())

def atualiza_altura_centimetro_para_metro(data: List[dict]) -> List[dict]:
    #data = deepcopy(ler_json())
    #data = deepcopy(data)
    
    for key, _ in enumerate (data['pessoas']):

        meter_in_centimetres = 100

        altura_converted = data['pessoas'][key]['altura'] / meter_in_centimetres
        data['pessoas'][key]['altura'] = altura_converted

    return data
    #return {}


