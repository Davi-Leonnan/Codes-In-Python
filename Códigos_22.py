# Métodos lógicos:

class Car:

    def turn_on(self):
        print("Você liga o motor")
        return self

    def drive(self):
        print("Você dirige o carro")
        return self

    def brake(self):
        print("Você pisa nos freios")
        return self

    def turn_off(self):
        print("Você desliga o motor")
        return self

car = Car()



car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
