from copy import deepcopy
from typing import List

import datetime, time, datetime

def add_imcs(data: List[dict]) -> List[dict]:
    """
    This function takes a object dict type, 
    unzips it and adds the BMI(imc) attributes to each person listed

    Very underweight (Muito abaixo do peso): less than 17 kg/m²
    Underweight (Abaixo do Peso): Between 17 kg/m² and 18.4 kg/m²
    Normal weight (Peso normal): Between 18.5 kg/m² and 29.9 kg/m²
    Overweight (Acima do peso): Between 30 kg/m² and 34.9 kg/m²
    Obesity (Obesidade): Above 35 kg/m²
    """

    data = deepcopy(data)
        
    try:
        for pessoa in data:
        
            weight = pessoa['peso']
            height = pessoa['altura']
            
            height_in_meters = height/ 100
            imc = weight / (height_in_meters**2)
            
            if  imc < 17:
                pessoa['imc'] = 'Muito abaixo do peso'
            elif imc <= 18.4:
                pessoa['imc'] = 'Abaixo do Peso'
            elif imc <= 29.9:
                pessoa['imc'] = 'Peso normal'
            elif imc <= 34.9:
                pessoa['imc'] = 'Acima do peso'
            else:
                pessoa['imc'] = 'Obesidade'
            
        return data
        
    except:
        return print("There was a problem executing the 'add_imcs' function from the adicoes file")


def add_nome_completo(data: List[dict]) -> List[dict]:
    """
    This function takes a object dict type, unzips it, 
    strips off the first and last name attributes and 
    adds the full name to each person listed " 
    """

    try:
        data = deepcopy(data)

        for pessoa in data:

            pessoa['nome_completo'] = pessoa['nome']+ " " + pessoa['sobrenome'] 

            del pessoa['nome'], pessoa['sobrenome']

        return data
    except:
        return print("There was a problem executing the 'add_nome'completo function from the adicoes file.")



def add_idade(data: List[dict]) -> List[dict]:
    """
    This function takes a object dict type, unpacks it, 
    transforms the nasicmento attribute, which is in type timestamp,
    and transforms it into a calendar date each person listed "
    """
    
    try:
        data = deepcopy(data)

        for pessoa in data:

            birth_str = pessoa['nascimento']
            seconds_in_year =31536000
            now_timestamp = time.time()

            birth_timestamp = datetime.datetime.timestamp(
                datetime.datetime.strptime(birth_str,"%d/%m/%Y")
            )
            age = (now_timestamp - birth_timestamp)/ seconds_in_year

            pessoa['idade'] = int(age)

        return data
    except:
        return print("There was a problem executing the 'add_idade'function from the adicoes file.")


