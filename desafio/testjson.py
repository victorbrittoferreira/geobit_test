import json

people_string = '''
{
    "pessoas": [
        {
            "id": 26,
            "nome": "Ricardo",
            "sobrenome": "Anne",
            "sexo": "M",
            "altura": 148,
            "peso": 72.6,
            "nascimento": 4762800.0,
            "endereço": {
                "bairro": "Rua 1",
                "cidade": "Wakanda",
                "estado": "Myr",
                "numero": 3
            }
        },
        {
            "id": 24,
            "nome": "Sousa",
            "sobrenome": "Arruda",
            "sexo": "M",
            "altura": 179,
            "peso": 73.8,
            "nascimento": 334292400.0,
            "endereço": {
                "bairro": "Rua 1",
                "cidade": "Hebrew",
                "estado": "Braavos",
                "numero": 2
            }
        }
    ]
}
'''

data = json.loads(people_string)

print(data)