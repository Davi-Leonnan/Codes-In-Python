# Dicionários:


# Definição: Estrutura de dados que contem dados na forma de pares de chaves e valores.

# OBS: Items em um dicionaŕios são fechadosn por chaves.

# OBS 02: Ao exibir todos os items de um dicionário, eles não aparecerão em ordem cronológica, visto que o mesmo não é considerado uma estrutura de dados ordenada.


# Exemplo 1: Acessar um item específico er um dicionário.

Dict01 = {
    "Nomes": "Pedro, Tiago, Jacó",
    "Idades": 33|31|26,
    "Profissões": "Engenheiro, Arquiteto, médico"
    }

Dict01["Idades"]

print(Dict01["Idades"])


# Exemplo 2: Atualizando um valor de um dicionário.

Dict02 = {
    "Salgados": "Coxinha, Quibe, Empada",
    "Doces": "Brigadeiro, beijinho, bolinho de chuva"
}

Dict02["Doces"] = "Bolo de macaxeira, Monteiro Lopes"

print(Dict02)


# Exemplo 3: Removendo um valor de um dicionário.

Dict03 = {
    "Nome": "Max Payne",
    "Idade": 33,
    "Profissão": "Detetive policial"
}

del Dict03["Idade"]

print(Dict03)


# Exemplo 4: Removendo todos os itens de um Dicionário.

Dict04 = {
    "Nome": "Mona Sax",
    "Idade": 28,
    "Profissão": "Mercenária"
}

Dict04.clear()

print(Dict04)