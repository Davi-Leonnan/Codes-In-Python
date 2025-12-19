# Dentro das funções, é possivel armazenar um valor que pode ser usado dentro do escopo da função.

# Exemplo 01:

def bonificaçao(salario):

    bonus = 200

    print(salario + bonus)

bonificaçao(2000)

# Podemos também adicionar a variável fora da função e usa-la no escopo. (Variável global)

# Exemplo 02:

afirmaçao = "Aprovado"
negaçao = "Reprovado"

def teste_de_qualidade(produto_01, produto_02, produto_03):

    if produto_01 == afirmaçao and produto_02 == afirmaçao and produto_03 == afirmaçao:
        print("Pronto para a entrega")

    else:
        print("Revisão necessária.")

teste_de_qualidade("aprovado", "aprovado", "aprovado")


# Exemplo 03:

salario = 2000

def despesas(conta_de_luz, conta_de_agua, conta_de_internet, mercado):
    print(salario - conta_de_luz - conta_de_agua - conta_de_internet - mercado)

despesas_totais = despesas(200, 100, 50, 550)

print(despesas_totais)

