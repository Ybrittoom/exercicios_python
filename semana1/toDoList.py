import time

def inicioToDoList():
    print('Bem-Vindo ao ToDoList mais top do mundo!!')
    while True: #loop principal para nao ecerrar o programa enquanto o usuario nao quiser sair
        print('Escolha uma funçao:\n ' 
        '1 - Adicionar Tarefa\n ' 
        '2 - Listar Tarefas\n ' 
        '3 - Remover Tarefa\n ' 
        '4 - Concluir Tarefa\n ' 
        '5 - Sair ')

        try:
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
                print('Saindo do ToDoList. Até a próxima!')
                break #sai do loop principal e encerra o programa
            else:
                print('escolha um funçao valida')
        except ValueError:
            print('Por favor, digite um número para escolher a função.')
        time.sleep(2)

tarefas = []

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
    listarTarefas()
    entrada = input('Digite (nome ou numero) da tarefa que deseja remover: ')

    try:
        indice = int(entrada)
        if 0 <= indice < len(tarefas):
            tarefaRemovida = tarefas.pop(indice)
            print(f'{tarefaRemovida} removida com sucesso!')
            print('Lista de Tarefas: ')
            print(tarefas)
        else:
            print('Tarefa nao encontrada!!')
            removerTarefa()
    except ValueError:
        if entrada in tarefas:
            tarefas.remove(entrada)
            print('Tarefa removida com sucesso!')
            print('Lista de Tarefas: ')
            print(tarefas)
        else:
            print(f'Tarefa com o nome {entrada} nao encontrada')
            removerTarefa()

def concluirTarefa():
    listarTarefas()
    tarefaConcluida = input('Digite a tarefa que deseja concluir: ')
    if tarefaConcluida in tarefas:
        tarefas.remove(tarefaConcluida)
        print('Tarefa concluida com sucesso!')
    else:
        print('Tarefa nao encontrada')

inicioToDoList()
inicioToDoList()