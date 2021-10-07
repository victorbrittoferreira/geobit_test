from copy import deepcopy
from typing import List

import time

def atualiza_nascimento_timestamp_para_date_string(data: List[dict]) -> List[dict]:
    data = deepcopy(data)

    for pessoa in data:

        birth_timestamp = pessoa['nascimento']
        birth_converted = time.strftime('%d/%m/%Y', (time.localtime  (birth_timestamp)))
        
        pessoa['nascimento'] = birth_converted

    return data


def atualiza_altura_centimetro_para_metro(data: List[dict]) -> List[dict]:
    data = deepcopy(data)
    
    for pessoa in data:

        meter_in_centimetres = 100

        altura_converted = pessoa['altura'] / meter_in_centimetres

        pessoa['altura'] = altura_converted

    return data






