# Para adicionar itens em uma lista, adicionamos o nome da lista, seguido de um ponto, e depois digitando a função "append", seguido do valor entre parenteses.

winners = ["Sarah", "Lucas", "John", "Rebecca"]

winners.append("Chris")

print(winners)


# Caso desseje adionar um valor em uma posição específica da lista, use a função "insert" no lugar de "append", seguido do valor do índice mais o nome do novo valor.

groceries = ["bread", "flour", "eggs", "sugar"]

groceries.insert(1, "butter")

print(groceries)


# Obs: Em ambas as funções, só se pode adicionar um valor por vez.


# Caso queira remover o último elemento da lista, usa-se a função "pop" seguida de parenteses.

menu = ["Burguer", "french fries", "apple pie", "ice cream"]

menu.pop()

print(menu)

# Caso queira remover um valor em específico, adicione o valor do índice dentro dos parenteses da função "pop".

cakes = ["chcolate cake", "starberry cake", "pudim cake", "pineapple cake", "coconut cake"]

cakes.pop(2)

print(cakes)


burguers = ["X-burguer", "chicken burgen", "X-Bacon", "X-salad", "X-steak"]

burguerRemoved = burguers.pop(2)

print("burguer removed: " + burguerRemoved)
print(burguers)
