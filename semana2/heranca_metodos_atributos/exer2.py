class Produto:
    def __init__(self, nome):
        self.nome_produto = nome
        print(f'Produto {self.nome_produto} adicionado com sucesso!!')

    def preco(self):
        print(f'{self.nome_produto} ele tem um preço!!')
        
class Arroz(Produto):
    def preco(self):
        print(f'O preco do {self.nome_produto} e R$10,00')

class Feijao(Produto):
    def preco(self):
        print(f'O preco do {self.nome_produto} e R$15,00')



produto = input('Digite o nome do produto: ')

if produto == 'arroz':
    arroz = Arroz(produto)
    arroz.preco()
elif produto == 'feijao':
    feijao = Feijao(produto)
    feijao.preco()
else:
    print('Produto nao encontrado')