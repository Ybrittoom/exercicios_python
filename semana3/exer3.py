class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)


alunos = []
alunos.append(Aluno("Ygor"))
alunos.append(Aluno("Rayssa"))

alunos[0].adicionar_nota(10)
print(alunos[0].nome, alunos[0].notas)