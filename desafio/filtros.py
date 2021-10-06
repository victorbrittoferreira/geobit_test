from copy import deepcopy

from typing import List
from .leitura import ler_json

#from adicoes import add_imcs

import datetime, time

import pdb

data = deepcopy(ler_json())


#def filtra_maior_de_idade_com_imc_acima_do_peso(data: List[dict]) -> List[dict]:
def filtra_maior_de_idade_com_imc_acima_do_peso():
    """
        Não sei o quão autônomo você gostaria que fosse a função, pois eu a considerei de forma absoluta,
    isto é, não chamar outra função de outro aquivo para realizar a função IMC.
    Se for considerar autonomia relativa, ou interdependente, favor descomentar abaixo 

    dataimc e data
    """
    #dataimc = add_imcs()
    #data = dataimc
    
    data_buffer = []

    for index, _ in enumerate (data['pessoas']):
        
        birth_timestamp = data['pessoas'][index]['nascimento']
        now_timestamp = time.time()
        age_timestamp = now_timestamp - birth_timestamp
        seconds_in_year =31536000
        year = divmod(age_timestamp, seconds_in_year)
        #print(int(year[0]))
        data['pessoas'][index]['idade'] = int(year[0])

        ##########################

        ## Descomite pra ser absolutamente independente da função add_imc e, por seguinte, a comente

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

        ############################
        #print(data['pessoas'][index]['imc'])

        idade = data['pessoas'][index]['idade']
        imc = data['pessoas'][index]['imc']
        above_normal_weight= ['Acima do peso' , 'Obesidade']
        
        if imc in above_normal_weight and idade >= 18:
            data_buffer.append(data['pessoas'][index])
        else:
            pass

    data['pessoas'].clear()
    for i in data_buffer: 
        data['pessoas'].append(i)

    return data
    #return {}


#def filtra_mulheres_de_meeren_braavos(data: List[dict]) -> List[dict]:
def filtra_mulheres_de_meeren_braavos():

    data_buffer = []
    
    for index, _ in enumerate (data['pessoas']):
    
        genere = data['pessoas'][index]['sexo'] 
        city = data['pessoas'][index]['endereço']['cidade']
        state = data['pessoas'][index]['endereço']['estado']

        if genere == 'F' and city == 'Meeren' and state == 'Braavos':
            data_buffer.append(data['pessoas'][index])
        else:
            pass

    data['pessoas'].clear()
    for i in data_buffer: 
        data['pessoas'].append(i)

    return data
    #return {}
