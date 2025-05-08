alunos = [
        "Angelo",
        "Agatha",
        "Emily",
        "Eduardo",
        "Matheus",
        "Pedro",
        "Rayssa",
        "Rayanne",
        "Sara",
        "Ygor"
    ]


def verificarSituacaoDoAluno(media):
        if media >= 7:
            print('Aprovado')
        elif media >= 5:
            print('Recuperação')
        else:
            print('Reprovado')


def calculadorDeNotas():
    nomeDoAluno = input('Qual o nome do aluno? ')

    if nomeDoAluno not in alunos:
        print('Aluno nao encontrado(a) na lista')
        return
    
    notas = []
    for i in range(1, 4):
        nota = float(input(f'Digite a nota {i}: '))
        notas.append(nota)

    media = sum(notas) / len(notas)
    situacao = verificarSituacaoDoAluno(media)

    print(f'\nAluno: {nomeDoAluno}')
    print(f'Media: {media:.2f}')
    print(f'Situaçao: {situacao}')

calculadorDeNotas()
