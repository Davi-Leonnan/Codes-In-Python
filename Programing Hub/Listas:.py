# Listas:

# Exemplo 1:

List01 = [0, 1, 2, 3, 4, 5, 6]

# Acessar um determinado valor em uma lista (O primeiro index é "0")

a = List01[1]
print(a)

# Acessar um determinado conjunto de valores em uma lista (O segundo parâmetro irá ser o valor de
# parada, ao invés do último valor a ser exibido)

b = List01[1:5]
print(b)

# Acessar todos os valores da lista:

c = List01[:]

# ou:

d = List01[0:7]

print(c)
print(d)


# Exemplo 2:

List02 = [25, 50, 75, 100, 125, 150, 175, 200]

# Mudando o valor de uma lista:

List02[1] = 70

print(List02)

# Adicionando um valor em uma lista:

List02.append(225)

print(List02)


# Exemplo 3:

List03 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]

# Deletando valores em uma lista:

del List03[4]

print(List03)

# ou:

List03.remove(9)  # Neste caso, é necessário especificar o valor em específico para remove-lo.

print(List03)


# Exemplo 4:

List04 = ["Mõnica", "Cebolinha", "Cascão", "Magali", "Franjinha", "Xaveco"]

e = List04[2]

print(e)

f = List04[0:4]

print(f)

List04.append("Denise")

print(List04)

del List04[5]

print(List04)
