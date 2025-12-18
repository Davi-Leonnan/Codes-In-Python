# É de suma importância nomear uma função de acordo com a função a qual executa.

# Exemplo:

def conta_total(conta_01, conta_02):
    return conta_01 + conta_02


resultado = conta_total(5, 5)

print(resultado)

# Exemplo 02:

def saudações(nome):
    return nome  

saldo = "Olá! " + saudações("Felipe")

print(saldo)

# Exemplo 03:

def media_aritmetica(nota_01, nota_02, nota_03, nota_04):
    return (nota_01 + nota_02 + nota_03 + nota_04) / 4

resultado = media_aritmetica(5, 8, 9, 8.5)

print(resultado)


