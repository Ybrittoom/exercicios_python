def inicioToDoList():
    print('Bem-Vindo ao ToDoList mais top do mundo!!')
    print('Escolha uma funçao:\n ' 
    '1 - Adicionar Tarefa\n ' 
    '2 - Listar Tarefas\n ' 
    '3 - Remover Tarefa\n ' 
    '4 - Concluir Tarefa\n ' 
    '5 - Sair ')

    funcaoDaLista = int(input('Escolha uma funçao(numero): '))

    if (funcaoDaLista == 1):
        adicionarTarefa()
    elif (funcaoDaLista == 2):
        listarTarefas()
    elif (funcaoDaLista == 3):
        removerTarefa()
    elif (funcaoDaLista == 4):
        concluirTarefa()
    elif (funcaoDaLista == 5):
        sair()
    else:
        print('escolha um funçao valida')

tarefas = ['cavalo', 'boi']

def adicionarTarefa():
    novaTarefa = input('Digite a nova tarefa: ')
    tarefas.append(novaTarefa)
    print('Tarefa adicionada com sucesso!')

def listarTarefas():
    if not tarefas:
        print('Nenhuma tarefa encontrada')
    else:
        print('Lista de tarefas: ')
        for tarefa in tarefas:
            print ('-', tarefa)


def removerTarefa():
    tarefaRemover = input('Digite a tarefa que deseja remover: ')
    if tarefaRemover in tarefas:
        tarefas.remove(tarefaRemover)
        print('Tarefa removida com sucesso!')
    else:
        print('Tarefa nao encontrada')

inicioToDoList()
print(tarefas[1])
print(tarefas)