from copy import deepcopy
from datetime import datetime
import time

from .leitura import ler_json

#data = deepcopy(ler_json())

def atualiza_nascimento_timestamp_para_date_string():
    #data = deepcopy(ler_json())
    data = deepcopy(data)
   
    for key, _ in enumerate (data['pessoas']):

        birth_timestamp = data['pessoas'][key]['nascimento']
        birth_converted = time.strftime(
            ' %d/%m/%Y ', 
            time.localtime(birth_timestamp)
            )
        data['pessoas'][key]['nascimento'] = birth_converted
        
    #return data
    return {}


def atualiza_altura_centimetro_para_metro():
    #data = deepcopy(ler_json())
    data = deepcopy(data)
    
    for key, _ in enumerate (data['pessoas']):

        meter_in_centimetres = 100

        altura_converted = data['pessoas'][key]['altura'] / meter_in_centimetres
        data['pessoas'][key]['altura'] = altura_converted

    #return data
    return {}


