from copy import deepcopy

from leitura import ler_json
import datetime, time

import pdb

#data = deepcopy(ler_json())


def filtra_maior_de_idade_com_imc_acima_do_peso():

    #data = deepcopy(data)
    data = deepcopy(ler_json())
    data_buffer = []

    for index, _ in enumerate (data['pessoas']):

        ## PS: Não sei o quão autônomo vocês gostariam que fosse a função, 
        # sendo assim. eu a considerei de forma absoluta, isto é, chamar outra função de outro aquivo.
        

        birth_timestamp = data['pessoas'][index]['nascimento']
        now_timestamp = time.time()
        age_timestamp = now_timestamp - birth_timestamp
        seconds_in_year =31536000
        year = divmod(age_timestamp, seconds_in_year)
        data['pessoas'][index]['idade'] = int(year[0])

        #________________________

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

        #__________________________________
    
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

    #return data
    return {}

print(filtra_maior_de_idade_com_imc_acima_do_peso())


def filtra_mulheres_de_meeren_braavos():

    data = deepcopy(ler_json())
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

    #return data
    return {}
