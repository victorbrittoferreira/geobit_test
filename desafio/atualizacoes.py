from copy import deepcopy
from datetime import datetime, date
import time
from typing import List

from .leitura import ler_json

import pdb 


data = deepcopy(ler_json())

def atualiza_nascimento_timestamp_para_date_string(data: List[dict]) -> List[dict]:
#def atualiza_nascimento_timestamp_para_date_string():
   
    for index, _ in enumerate (data['pessoas']):

        birth_timestamp = data['pessoas'][index]['nascimento']

        #birth_converted = time.strftime(' %d/%m/%Y ', (time.localtime (int (birth_timestamp))))
        birth_converted = time.strftime(' %d%m%Y ', (time.localtime  (birth_timestamp)))
        #birth_converted = date.fromtimestamp(birth_timestamp)
        
        data['pessoas'][index]['nascimento'] = (int(birth_converted))
        #print(type(data['pessoas'][index]['nascimento']))

    return data
    #return {}

#print(atualiza_nascimento_timestamp_para_date_string (List[dict]))
#print(atualiza_nascimento_timestamp_para_date_string ())

def atualiza_altura_centimetro_para_metro(data: List[dict]) -> List[dict]:
#def atualiza_altura_centimetro_para_metro():
    
    for index, _ in enumerate (data['pessoas']):

        meter_in_centimetres = 100

        altura_converted = data['pessoas'][index]['altura'] / meter_in_centimetres
        data['pessoas'][index]['altura'] = altura_converted

    return data
    #return {}

#print(atualiza_altura_centimetro_para_metro())




