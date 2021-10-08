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

        for pessoa in pessoas:
            json_data['pessoas'].append(pessoa)

        for pessoa in filter_1:
            json_data['filtros']['maiores_de_idade_com_imc_acima_peso'].append(pessoa)

        for pessoa in filter_2:
            json_data['filtros']['mulheres_meeren_braavos'].append(pessoa)


        with open('/home/kurt/GitHub/geobit_test/output.json', 'w') as fp:
            json.dump(json_data, fp, ensure_ascii= False, indent= 4)

    except:
        return print("There was a problem executing the 'data_to_json' function from the escrita file.")

    