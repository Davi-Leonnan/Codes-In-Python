# Condição while: Soma finita de um número

soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 13:
        break
    soma += n

print(f"soma = {soma}")


frase = "o rato roeu a roupa do rei de roma"
palavra = ""
palavras = []
i = 0
while i < len(frase):
    if frase[i] == " ":
        palavras.append(palavra)
        palavra = ""
    else:
        palavra += frase[i]
    i += 1
palavras.append(palavra)

i = 0
while i < len(palavras):
    if len(palavras[i]) > 3:
        print(palavras[i])
    i += 14
    
