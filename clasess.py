class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass

class Predator(Animal):
    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} eats {food.name}')
            self.fed = True
        else:
            print(f'{self.name} does not eat {food.name}')
            self.alive = False




dog = Predator('Mors')
krapiva = Plant('Krapiva')
krapiva.edible = True
print(dog.name)
print(dog.alive)
print(dog.fed)
dog.eat(krapiva)
print(dog.alive)
print(dog.fed)