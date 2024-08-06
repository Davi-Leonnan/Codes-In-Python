# Formato de Linguagem:

Number = input("Disk your favorite number: ")

Right_Number = float(Number)  # A função "float" permite que um número não inteiro seja aceito como valor de entrada.

print("The number disked in your small way is: {:.2f} ".format(Right_Number))
print("The number disked in your small way is: {:,} ".format(Right_Number))
print("The number disked in your small way is: {:X} ".format(Right_Number))
print("The number disked in your small way is: {:E} ".format(Right_Number))