class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print('O animal faz barulho')

class Cachorro(Animal):
    def falar(self):
        print(f'O {self.nome} faz au au!')


animal = Animal("Bicho")
cachorro = Cachorro("pitBull")

animal.falar()
cachorro.falar()