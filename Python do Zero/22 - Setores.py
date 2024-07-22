# 22 - Setores:


# Não importa a quantidade de elementos iguais colocados em um set, ele sempre irá aparecer somente uma vez quando for executado.

utensils = {"Fork", "Spoon", "Knife"}

dishes = {"Bowl", "Plate", "Cup", "Knife"}

#utensils.add("Napkin")  # Adiciona um elemento ao set.
#utensils.remove("Fork")  # Remove um elemento do set.
#utensils.clear()  # Remove todos os elementos do set.
#dishes.update(utensils)  # Adiciona elementos do set anterior ao set atual.

#print(utensils.difference(dishes))  # Lista elementos diferentes entre um set e outro.
print(utensils.intersection(dishes))  # Lista elementos em comum entre um set e outro.

#for x in dishes:
    #print(x)