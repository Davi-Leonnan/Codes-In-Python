# Quando desejamos saber quantas vezes um mesmo elemento aparece em uma lista, utilizamos a função "count()", em seguida, escrevemos o elemento dentro dos parenteses.

# Exemplo 01:

Orders = ["pizza", "hamburguer", "pizza", "pasta", "french fires", "pizza", "lasagna"]

print(Orders.count("pizza"))

# Exemplo 02:

Results = [True, False, True, True, False, True, False, True, True, False]

True_Results = Results.count(True)

print((True_Results))

# Quando queremos saber se um certo elemento está presente na lista, podemos utilizar a palavra-chave "in".

# Exemplo 03:

Groceries = ["sugar", "rice", "beans", "oil", "butter", "cokkies", "oranges", "coffee"]

print("rice" in Groceries)
print("milk" in Groceries)
