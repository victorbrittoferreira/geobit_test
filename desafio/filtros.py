from copy import deepcopy
from typing import List

from .adicoes import add_imcs, add_idade 
#from .leitura import ler_json
#data = deepcopy(ler_json())


def filtra_maior_de_idade_com_imc_acima_do_peso(data: List[dict]) -> List[dict]:
    data = deepcopy(data)
#def filtra_maior_de_idade_com_imc_acima_do_peso():

    #dataimc = add_imcs()
    #data = dataimc
    
    data_buffer = []

    #for index, _ in enumerate (data['pessoas']):
    # Gatilho de independência.
    if not "imc" in data[0]:
        data = add_imcs(data)

    if not "idade" in data[0]:
        data = add_idade(data)
    
    for pessoa in data:
        
        
        #birth_timestamp = pessoa['nascimento']
        #now_timestamp = time.time()
        #
        #idade = pessoa['idade']
        #imc = pessoa['imc']
        above_normal_weight= ['Acima do peso' , 'Obesidade']
        
        if pessoa['imc'] in above_normal_weight and pessoa['idade'] >= 18:
            data_buffer.append(pessoa)

    #data['pessoas'].clear()
    #for i in data_buffer: 
    #    data['pessoas'].append(i)

    return data_buffer
    #return {}


def filtra_mulheres_de_meeren_braavos(data: List[dict]) -> List[dict]:
    data = deepcopy(data)
#def filtra_mulheres_de_meeren_braavos():

    data_buffer = []
    
    for pessoa in data:
    
        genere = pessoa['sexo'] 
        city = pessoa['endereço']['cidade']
        state = pessoa['endereço']['estado']

        if genere == 'F' and city == 'Meeren' and state == 'Braavos':
            data_buffer.append(pessoa)
        
        

    #data['pessoas'].clear()
    #for i in data_buffer: 
    #    data['pessoas'].append(i)

    return data_buffer
    #return {}
