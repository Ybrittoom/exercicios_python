class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar(self):
        print(f"{self.nome} R$ {self.preco:.2f}")


class Estoque:
    def __init__(self):
        self.produtos = []

    def add(self, produto):
        self.produtos.append(produto)

    def listar(self):
        for produto in self.produtos:
            Produto.mostrar(produto)


#usando
estoque = Estoque()
estoque.add(Produto("Teclado", 100)) #adiciona um produto usando o a funçao add()
estoque.add(Produto('Mouse', 50))
estoque.listar()