# Condição While: Cálculo da média de duas notas

leituras = 1 
while leituras < 6:
    nota_01 = float(input("Digite a nota 01 do aluno {}: ".format(leituras)))
    nota_02 = float(input("Digite a nota 02 do aluno {}: ".format(leituras)))
    
    media = (nota_01 + nota_02)/2
    print("A media do aluno {} é igual a {:.2f}".format(leituras, media))
    print(("-") * 100)

    leituras = leituras + 1


