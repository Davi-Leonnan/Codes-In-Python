# Cenários hipotéticos:


class Animal:

    alive  = True

    def eat(self):
        print("Este animal está comendo")

    def slumber(self):
        print("Este animal está dormindo")

class Rabbit(Animal):

    def run(self):
        print("Este Coelho está correndo")

class Fish(Animal):

    def swim(self):
        print("Este peixe está nadando")

class Hawk(Animal):

    def fly(self):
        print("Este falcão está voando")



rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.slumber()

rabbit.run()
fish.swim()
hawk.fly()