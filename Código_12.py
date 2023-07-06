# Condicionais envolvendo Idade:


#age = int(input("Quantos anos você tem?:"))

#if age >= 100:
    #print("Parabéns, ancestral!")
#elif age >= 18:
    #print("Você é um adulto!")
#elif age < 0:
    #print("Você é ainda um feto, mano!")
#else:
    #print("Você é ainda um pirralho!")


Listagem = int(input("Digite a idade do acleta: "))

if Listagem <= 10:
    print("Você faz parte da seleção infantil.")

elif Listagem <= 13:
    print("Você faz parte da seleção infantojuvenil I.")

elif Listagem <= 17:
    print("Você faz parte da seleção Infantojuvenil II.")

elif Listagem <= 40:
    print("Você faz parte da seleção Adulta I.")

elif Listagem <= 60:
    print("Você faz parte da seleção Adulta II.")

elif Listagem >60:
    print("Você faz parte da seleção idosa.")

else:
    print("Candidato não compativel.")

