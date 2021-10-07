from copy import deepcopy
from datetime import datetime, date
import time
from typing import List

def atualiza_nascimento_timestamp_para_date_string(data: List[dict]) -> List[dict]:
#def atualiza_nascimento_timestamp_para_date_string():
    data = deepcopy(data)
    #for index, _ in enumerate (data['pessoas']):
    for pessoa in data:

        birth_timestamp = pessoa['nascimento']

        #birth_converted = time.strftime(' %d/%m/%Y ', (time.localtime (int (birth_timestamp))))
        birth_converted = time.strftime(' %d%m%Y ', (time.localtime  (birth_timestamp)))
        #birth_converted = date.fromtimestamp(birth_timestamp)
        
        pessoa['nascimento'] = (int(birth_converted))
        #print(type(pessoa['nascimento']))

    return data
    #return {}



def atualiza_altura_centimetro_para_metro(data: List[dict]) -> List[dict]:
#def atualiza_altura_centimetro_para_metro():
    data = deepcopy(data)
    
    for pessoa in data:

        meter_in_centimetres = 100

        altura_converted = pessoa['altura'] / meter_in_centimetres
        pessoa['altura'] = altura_converted

    return data
    #return {}





