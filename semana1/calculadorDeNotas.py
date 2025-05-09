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

# verifica a situaçao do aluno(aprovado, recuperaçao ou reprovado)
def verificarSituacaoDoAluno(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'


def calculadorDeNotas():
    nomeDoAluno = input('Qual o nome do aluno? ')

    if nomeDoAluno not in [alunos.lower() for alunos in alunos]:
        print('Aluno nao encontrado(a) na lista')
        return
    
    notas = []
    for i in range(1, 4):# cria uma sequencia que repete 3 vezes
        nota = float(input(f'Digite a nota {i}: '))#float transforma em numero decimal
        notas.append(nota)#adiciona a lista 'nota'

    #calcula a media
    media = sum(notas) / len(notas)
    situacao = verificarSituacaoDoAluno(media)

    print(f'\nAluno: {nomeDoAluno}')
    print(f'Media: {media:.2f}')
    print(f'Situaçao: {situacao}')

calculadorDeNotas()
