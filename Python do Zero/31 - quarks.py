# quarks:

# Compacta todos os argumentos em um único dicionário.

def hello(**kwargs):
    # print("hello" + " " + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end=" ")
    for key,value in kwargs,items():
        print(value, end=" ")


hello(first= "Tommy",middle="Cipriani" last= "Vercetti" )

