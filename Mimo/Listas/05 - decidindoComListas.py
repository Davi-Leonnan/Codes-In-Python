# Para saber o número de elementos em uma lista, utilizamos a função "len():

# Exemplo 01:

SH2_Characters = ["James", "Mary", "Maria", "Angela", "Eddie", "Laura"]

print(len(SH2_Characters))

# Exemplo 02:

SH1_Characters = ["Harry", "Cheryl", "Cybil", "Lisa", "Kauffman", "Dalia"]

Main_Characters = len(SH1_Characters)

print(Main_Characters)


# Podemos usar a função "len()" em condicionais, tais como:

# Exemplo 01:

Meals = ["Fried chicken", "Beef", "Lasagna", "Fried fish"]

Lunch_Meals = len(Meals)

if Lunch_Meals >= 2:
    print("Serve the lunch now!")
