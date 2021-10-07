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

    ##

    with open('/home/kurt/GitHub/geobit_test/output.json', 'w') as fp:
        output = json.dump(json_data, fp)
    #return output