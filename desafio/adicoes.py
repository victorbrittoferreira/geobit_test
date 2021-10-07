from copy import deepcopy
import datetime, time
from typing import List
from  .leitura import ler_json

data = deepcopy(ler_json())

def add_imcs(data: List[dict]) -> List[dict]:
#def add_imcs():
    """ 
        Muito abaixo do peso:  menor que 17 kg/m²
        Abaixo do Peso: Entre 17 kg/m² e 18.4 kg/m²
        Peso normal: Entre 18.5 kg/m² e 29.9 kg/m²
        Acima do peso: Entre 30 kg/m² e 34.9 kg/m²
        Obesidade: Acime de 35 kg/m² 
    """

    for index, _ in enumerate (data['pessoas']):

        weight = data['pessoas'][index]['peso']
        height = data['pessoas'][index]['altura']
        
        height_in_meters = height/ 100
        imc = weight / (height_in_meters**2)

        if  imc < 17:
            data['pessoas'][index]['imc'] = 'Muito abaixo do peso'
        elif imc <= 18.4:
            data['pessoas'][index]['imc'] = 'Abaixo do Peso'
        elif imc <= 29.9:
            data['pessoas'][index]['imc'] = 'Peso normal'
        elif imc <= 34.9:
            data['pessoas'][index]['imc'] = 'Acima do peso'
        else:
            data['pessoas'][index]['imc'] = 'Obesidade'

    #return {}
    return data

#print(add_imcs(List[dict]))


def add_nome_completo(data: List[dict]) -> List[dict]:
#def add_nome_completo():

    for index, _ in enumerate (data['pessoas']):

        #Create nome_completo atribute
        data['pessoas'][index]['nome_completo'] = data['pessoas'][index]['nome']+ " " + data['pessoas'][index]['sobrenome'] 
        # delete nome and sobrenome atribute
        del data['pessoas'][index]['nome'],data['pessoas'][index]['sobrenome']

    #return {}
    return data


def add_idade(data: List[dict]) -> List[dict]:
#def add_idade():
    
    for index, _ in enumerate (data['pessoas']):

        birth_timestamp = data['pessoas'][index]['nascimento']
        now_timestamp = time.time()
        age_timestamp = now_timestamp - birth_timestamp
        seconds_in_year =31536000
        year = divmod(age_timestamp, seconds_in_year)

        data['pessoas'][index]['idade'] = int(year[0])
        
    return data
    #return {}