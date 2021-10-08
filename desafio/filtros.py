from copy import deepcopy
from typing import List

from .adicoes import add_imcs, add_idade 

def filtra_maior_de_idade_com_imc_acima_do_peso(data: List[dict]) -> List[dict]:
    try:
        data = deepcopy(data)
        data_temp = []
    
        # Independence switch
        if not "imc" in data[0]:
            data = add_imcs(data)

        if not "idade" in data[0]:
            data = add_idade(data)

        for pessoa in data:

            above_normal_weight= ['Acima do peso' , 'Obesidade']

            if pessoa['imc'] in above_normal_weight and pessoa['idade'] >= 18:
                data_temp.append(pessoa)

        return data_temp
    except:
        return print("There was a problem executing the 'filtra_maior_de_idade_com_imc_acima_do_peso' function from the filtros file.  ")    

def filtra_mulheres_de_meeren_braavos(data: List[dict]) -> List[dict]:
    try:
        data = deepcopy(data)
        data_temp = []

        for pessoa in data:
        
            genere = pessoa['sexo'] 
            city = pessoa['endereço']['cidade']
            state = pessoa['endereço']['estado']

            if genere == 'F' and city == 'Meeren' and state == 'Braavos':
                data_temp.append(pessoa)

        return data_temp
    except:
        return print("There was a problem executing the 'filtra_mulheres_de_meeren_braavos' function from the filtros file.  ")    

