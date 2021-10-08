from copy import deepcopy
from typing import List

import datetime, time, datetime

def add_imcs(data: List[dict]) -> List[dict]:
    try:
        data = deepcopy(data)
        
        for pessoa in data:

            weight = pessoa['peso']
            height = pessoa['altura']

            height_in_meters = height/ 100
            imc = weight / (height_in_meters**2)

            if  imc < 17:
                pessoa['imc'] = 'Muito abaixo do peso'
            elif imc <= 18.4:
                pessoa['imc'] = 'Abaixo do Peso'
            elif imc <= 29.9:
                pessoa['imc'] = 'Peso normal'
            elif imc <= 34.9:
                pessoa['imc'] = 'Acima do peso'
            else:
                pessoa['imc'] = 'Obesidade'

        return data

    except:
        return print("There was a problem executing the 'add_imcs' function from the adicoes file")


def add_nome_completo(data: List[dict]) -> List[dict]:
    try:
        data = deepcopy(data)

        for pessoa in data:

            pessoa['nome_completo'] = pessoa['nome']+ " " + pessoa['sobrenome'] 

            del pessoa['nome'], pessoa['sobrenome']

        return data
    except:
        return print("There was a problem executing the 'add_nome'_completo function from the adicoes file.  ")




def add_idade(data: List[dict]) -> List[dict]:
    try:
        data = deepcopy(data)

        for pessoa in data:

            birth_str = pessoa['nascimento']
            seconds_in_year =31536000
            now_timestamp = time.time()

            birth_timestamp = datetime.datetime.timestamp(
                datetime.datetime.strptime(birth_str,"%d/%m/%Y")
            )
            age = (now_timestamp - birth_timestamp)/ seconds_in_year

            pessoa['idade'] = int(age)

        return data
    except:
        return print("There was a problem executing the 'add_idade' function from the adicoes file.  ")


