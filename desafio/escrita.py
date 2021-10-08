from typing import List
import json


def data_to_json(pessoas: List[dict], filter_1: List[dict], filter_2: List[dict]) -> dict: 
    try:

        json_data = {
                "pessoas": [],
                "filtros": {
                    "maiores_de_idade_com_imc_acima_peso": [],
                    "mulheres_meeren_braavos": []
                }
            }
        #def __init__(self, data):
        #    self.id = id
        #    self.sexo = sexo
        #    self.altura = altura
        #    self.peso = peso
        #    self.nascimento = nascimento
        #    self.endereço = endereço
        #    self.idade = idade
        #    self.imc = imc
        #    self.nome_completo = nome_completo

        def execute_adicoes_e_atualizacoes():
            try:
                for pessoa in pessoas:
                    json_data['pessoas'].append(pessoa)
                return pessoas

            except:
                return print("There was a problem executing the 'execute_adicoes_e_atualizacoes' function from the escrita file.  ")    
        
        def execute_filtros():
            try:
                for pessoa in filter_2:
                    json_data['filtros']['mulheres_meeren_braavos'].append(pessoa)

                for pessoa in filter_1:
                    json_data['filtros']['maiores_de_idade_com_imc_acima_peso'].append(pessoa)
                return pessoas

            except:
                return print("There was a problem executing the 'execute_filtros' function from the escrita file.  ")    

        def dict_to_json():
            try:
            #execute_adicoes_e_atualizacoes()
            #execute_filtros()

                with open('/home/kurt/GitHub/geobit_test/output.json', 'w') as fp:
                    json.dump(json_data, fp, ensure_ascii= False, indent= 4)
            except:
                return print("There was a problem executing the 'execute_filtros' function from the escrita file.  ")  



        return execute_adicoes_e_atualizacoes(), execute_filtros(),  dict_to_json()

    except:
        return print("There was a problem executing the 'data_to_json' function from the escrita file.")

    