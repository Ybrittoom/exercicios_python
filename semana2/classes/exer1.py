


class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Ola meu nome é {self.nome} e tenho {self.idade} anos')

    
yago = Pessoa('yago', 16)
yago.apresentar()



class Produto:
    def __init__(self, nome_produto, validade):
        self.nome_produto = nome_produto
        self.validae = validade

    def apresentar(self):
        print(f'o produto adicionado foi {self.nome_produto} e sua validade é {self.validae}! ')

nome_do_produto = input("Adicione um produto: ")
validade_do_produto = input("Adicione a validade do produto: ")

produto = Produto(nome_do_produto, validade_do_produto)
produto.apresentar()


#herança
class Animal:
    def falar(self):
        print("algum som")


class Cachorro(Animal):
    def falar(self):
        print('au au')


