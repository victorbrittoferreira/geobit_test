from desafio import adicoes, atualizacoes, filtros, leitura, escrita

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
    filter_1 = filtros.filtra_maior_de_idade_com_imc_acima_do_peso(pessoas)
    filter_2 = filtros.filtra_mulheres_de_meeren_braavos(pessoas)

    #escrita
    escrita = escrita.data_dict_to_json_file(pessoas , filter_1, filter_2)
