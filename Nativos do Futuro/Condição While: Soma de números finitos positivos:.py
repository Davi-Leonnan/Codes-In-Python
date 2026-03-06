# Soma de números finitos positivos:

soma = 0
x = 0

while x < 10:
    x +=1
    n = int(input("digite um número: "))

    if n < 0:
        continue
    
    soma += n

print(f"soma = {soma}")

