from typing import List
import json


def data_to_json(pessoas: List[dict], filter_1: List[dict], filter_2: List[dict]) -> dict: 

    json_data = {
            "pessoas": [],
            "filtros": {
                "menores_de_idade_com_imc_acima_peso": [],
                "mulheres_meeren_braavos": []
            }
        }
    
    for pessoa in pessoas:
        json_data['pessoas'].append(pessoa)

    for pessoa in filter_1:
        json_data['filtros']['menores_de_idade_com_imc_acima_peso'].append(pessoa)

    for pessoa in filter_2:
        json_data['filtros']['mulheres_meeren_braavos'].append(pessoa)


    with open('/home/kurt/GitHub/geobit_test/output.json', 'w') as fp:
        output = json.dump(json_data, fp ,ensure_ascii=False, indent=4)

    