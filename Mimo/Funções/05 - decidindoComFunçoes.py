# Podemos criar condicionais dentro de funções, e adicionar um parâmetro para torna-las mais flexiveis.

# Exemplo 01:

def tempo_de_corrida (tempo):

    if tempo < 3.00:
        print("Parabéns! Você bateu o seu recorde!")
    
    elif tempo >= 3.00 and tempo <= 5.00:
        print("Você atingiu o seu tempo médio de corrida")

    else:
        print("Você foi além do seu tempo médio de corrida, continue praticando")

resultado = tempo_de_corrida(2.50)

print(resultado)


# Exemplo 02:

def preço_do_açai(preço_da_lata):

    if preço_da_lata <= 50:
        print("Preço do açaí: R$18,00")

    elif preço_da_lata > 50 and preço_da_lata <= 100:
        print("Preço do açaí: R$20,00")

    elif preço_da_lata > 100 and preço_da_lata <= 150:
        print("Preço do açaí: R$22,00")

    else:
        print("Preço do açaí: R$25,00")

resultado = preço_do_açai(100)

print(resultado)

