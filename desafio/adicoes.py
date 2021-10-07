from copy import deepcopy
import datetime, time
from typing import List


def add_imcs(data: List[dict]) -> List[dict]:
    data = deepcopy(data)
#def add_imcs():
    """ 
        Muito abaixo do peso:  menor que 17 kg/m²
        Abaixo do Peso: Entre 17 kg/m² e 18.4 kg/m²
        Peso normal: Entre 18.5 kg/m² e 29.9 kg/m²
        Acima do peso: Entre 30 kg/m² e 34.9 kg/m²
        Obesidade: Acime de 35 kg/m² 
    """

    #for index, _ in enumerate (data['pessoas']):
    for pessoa in data:

        #weight = data['pessoas'][index]['peso']
        weight = pessoa['peso']
        #height = data['pessoas'][index]['altura']
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

    #return {}
    return data

#print(add_imcs(List[dict]))


def add_nome_completo(data: List[dict]) -> List[dict]:
    data = deepcopy(data)
#def add_nome_completo():

    #for index, _ in enumerate (data['pessoas']):
    for pessoa in data:

        #Create nome_completo atribute
        pessoa['nome_completo'] = pessoa['nome']+ " " + pessoa['sobrenome'] 
        # delete nome and sobrenome atribute
        del pessoa['nome'],pessoa['sobrenome']

    #return {}
    return data


def add_idade(data: List[dict]) -> List[dict]:
    data = deepcopy(data)
#def add_idade():
    
    for pessoa in data:

        birth_timestamp = pessoa['nascimento']
        now_timestamp = time.time()
        age_timestamp = now_timestamp - birth_timestamp
        seconds_in_year =31536000
        year = divmod(age_timestamp, seconds_in_year)

        pessoa['idade'] = int(year[0])
        
    return data
    #return {}