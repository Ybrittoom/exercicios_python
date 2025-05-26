#listas e dicionarios

alunos = {
    "nome": "Ygor",
    "notas": [7, 8, 9, 5]
}

media = sum(alunos["notas"]) / len(alunos["notas"])
print(f'a media do aluno {alunos["nome"]} é {media:.2f}')

