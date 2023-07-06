# Operadores Lógicos:

temp = int(input("Digite a temperatura ambiente: "))

if temp >= 0 and temp <= 30:
    print("a temperatura está boa!")
    print("Você pode ir lá pra fora")
elif temp < 0 or temp > 30:
    print("a temperatura não está adequada no momento!")
    print("Permaneça abrigado!")