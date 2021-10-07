import json

from leitura import ler_json
from adicoes import add_imcs, add_idade, add_nome_completo
from atualizacoes import (
    atualiza_altura_centimetro_para_metro, 
    atualiza_nascimento_timestamp_para_date_string
)
from filtros import (
    filtra_maior_de_idade_com_imc_acima_do_peso,
    filtra_mulheres_de_meeren_braavos
)

print('1')

class Run(object):
    json_data = {
        "pessoas": [],
        "filtros": {
            "menores_de_idade_com_imc_acima_peso": [],
            "mulheres_meeren_braavos": []
        }
    }

    print('2')

    def __init__(self, data):
        ...
    print('3')
    def execute_adicoes_e_atualizacoes(self):
        """
            Leia o arquivo json usando a função ler_json e acima do
            retorno aplique todas as adições e atualizações. Por fim,
            adicione todas as pessoas já formatadas ao 
            self.json_data['pessoas']
        """
        print('x')
        ler_json()

        add_imcs()
        add_idade()
        add_nome_completo()

        atualiza_altura_centimetro_para_metro()
        atualiza_nascimento_timestamp_para_date_string()

        return json_data

        ...
    print('4')
    def execute_filtros(self):
        """
            Aplique cada filtro usando como data a variável 
            self.json_data['pessoas'] e adicione o resultado em 
            self.json_data['filtros'] na chave respectiva ao filtro.
        """
        filtra_maior_de_idade_com_imc_acima_do_peso
        filtra_mulheres_de_meeren_braavos
        
        return json_data
        ...
    print('5')
    def dict_to_json():
        """
            Transforme o dicionário self.json_data 
            em um arquivo chamado output.json
        """
        json_data = data
        #with open('/home/kurt/GitHub/geobit_test/output.json', 'w') as fp:
        #    output.json = json.dump(json_data, fp)

        print(output.json)
        #return output.json
        
        #output.json =json.dumps(data)

    print('6')
    print(dict_to_json())