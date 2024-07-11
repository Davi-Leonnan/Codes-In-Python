# Operadores Lógicos:

# Ao adicionar "not" nas condicionais mais parentesens nas condições, a mesma irá atutar de forma reversa.
# Exemplo: if not(temp >= 0 and temp <= 30):

temp = int(input("What is the temperature (C°) outside?"))

if temp >= 0 and temp <= 30:
    print("The temperature is good today! ")
    print("Go outside!")

elif temp < 0 or temp >30:
    print("The temperature it's bad today!")
    print("Stay outside!")

