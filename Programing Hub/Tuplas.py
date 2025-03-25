# Tuplas:


# Definição: Lista que armazena inúmeros tipos de valores, sendo que esses valores podem ou não podem ser do mesmo tipo.

# OBS: O primeiro index de uma tupla é "0".

# OBS 02: Os valores de uma tupla são imutáveis, ou seja, não podem ser adicionados e nem removidos.


# Exemplo 1: Exibir um valor em específico de uma tupla.

Tupla01 = (2, 4, 6, 8, 10)

Tupla01[1]

print(Tupla01[1])


# Exemplo 2: Exibir múltiplos valores de uma tupla.

Tupla02 = (8, 16, 24, 32, 40, 48, 56, 64)

Tupla02[1:8]

print(Tupla02[1:7])


# Exemplo 3: Apagar por completo uma tupla.

Tupla03 = ("Peter", "Louis", "Meg", "Chris", "Stewie", "Brian")

del Tupla03


# Exemplo 4:

Tupla04 = ("456", "001", "Triangle", "Circle", "Square")

Tupla04[0]
Tupla04[:4]

print(Tupla04[0])
print(Tupla04[:5])
