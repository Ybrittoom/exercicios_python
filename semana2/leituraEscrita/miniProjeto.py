def agendaContato():
    #criando o input
    contato = input('Digite o nome do contato: ')
    numero = input('Digite o numero do contato: ')

    print('Voce deseja acrescentar ou substituir??')
    print('1 - Acrescentar')
    print('2 - substituir')
    respostaUsuario = input('Digite a opcao desejada: ')
    if respostaUsuario == '1':
        with open('agendaContatos.txt', 'a') as agenda:
            agenda.write(f'Contato: {contato}\n')
            agenda.write(f'Numero: {numero}\n')
            agenda.write('-----------------------------------\n')
    else:
        with open('agenda.txt', 'w') as agenda:
            agenda.write(f'Contato: {contato}\n')
            agenda.write(f'Numero: {numero}\n')
            agenda.write('-----------------------------------\n')


    with open('agendaContatos.txt', 'r') as agenda:
        conteudo = agenda.read()
        print(conteudo)


agendaContato()