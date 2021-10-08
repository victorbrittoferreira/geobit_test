from copy import deepcopy
from typing import List

import time

def atualiza_nascimento_timestamp_para_date_string(data: List[dict]) -> List[dict]:
    """
    This function takes a object dict type, unpacks it, 
    transforms the nasicmento attribute, which is in type timestamp,
    and transforms it into a calendar date each person listed "
    """
    
    try:
        data = deepcopy(data)

        for pessoa in data:

            birth_timestamp = pessoa['nascimento']
            birth_converted = time.strftime('%d/%m/%Y', (time.localtime  (birth_timestamp)))

            pessoa['nascimento'] = birth_converted

        return data
    except:
        return print("There was a problem executing the 'atualiza_nascimento_timestamp_para_date_string' function from the atualizacoes file.  ")


def atualiza_altura_centimetro_para_metro(data: List[dict]) -> List[dict]:
    """
    This function receives a object dict type, unzips it, processes the height,
     which is in centimeters and transforms it into meters, for each person listed "
    """
    try:
        data = deepcopy(data)

        for pessoa in data:

            meter_in_centimetres = 100

            altura_converted = pessoa['altura'] / meter_in_centimetres

            pessoa['altura'] = altura_converted

        return data
    except:
        return print("There was a problem executing the 'atualiza_altura_centimetro_para_metro' function from the atualizacoes file.  ")






