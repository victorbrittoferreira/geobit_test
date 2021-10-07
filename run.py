from desafio import adicoes, atualizacoes, filtros, leitura

if __name__ == '__main__':
    # leitura
    data = leitura.ler_json()
    pessoas = data["pessoas"]

    # atualizacoes
    pessoas = atualizacoes.atualiza_altura_centimetro_para_metro(pessoas)
    pessoas = atualizacoes.atualiza_nascimento_timestamp_para_date_string(pessoas)

    # Adições
    pessoas = adicoes.add_idade(pessoas)
    pessoas = adicoes.add_imcs(pessoas)
    pessoas = adicoes.add_nome_completo(pessoas)

    # filtros
    filtro_1 = filtros.filtra_maior_de_idade_com_imc_acima_do_peso(pessoas)
    filtro_2 = filtros.filtra_mulheres_de_meeren_braavos(pessoas)

    #escrita
    # a função data_to_json vem aqui

    funcao_data_json = escrita.data_to_json(pessoas)

    print(pessoas)