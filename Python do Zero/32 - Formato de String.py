# Formato de Linguagem:

# A função "Format" permite que, ao mudar o valor de uma variável que irá ser exibida, a exibição também irá mudar junto.

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)

#print("The {} jumped over the {}".format(animal, item))
#print("The {1} jumped over the {0}".format(animal, item))  # Argumento Posicional
#print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # Argumento com Palavra Chave.

text = "The {} jumped over the {}"
print(text.format(animal, item))