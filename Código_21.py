# Múltiplos Cenários hipotéticos:


class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("Este animal está comendo")

class Dog(Animal):

    def bark(self):
        print("Este cachorro está latindo")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()