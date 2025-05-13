
array = ['cavalo', 'boi', 'gato']

def removerArray():
    print(array)
    entrada = input('Digite o item que deseja remover: ')
    try:
        indice = int(entrada)
        if 0 <= indice < len(array):
            item_removido = array.pop(indice)
            print(f'"{item_removido}" removido com sucesso!')
            print(array)
        else:
            print('numero nao encontrado')

    except ValueError:
        if entrada in array:
            array.remove(entrada)
            print(f'{entrada} removido com sucesso')
            print(array)
        else:
            print('Tarefa nao encontrada')
    
removerArray()