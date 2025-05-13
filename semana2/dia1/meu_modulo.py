import time


def saudacao(nome):
    print(f'Ola {nome}!')



def idadeMinima():

    idade = int(input("Digite a sua idade: "))
    idadeMinima = 18

    while idade <= idadeMinima or idade > idadeMinima:
        if idade <= idadeMinima:
            print(f'Voce tem {idade} anos, nao podera dirigir')
        else:
            print(f'Voce tem {idade} anos, podera dirigir')
        idade += 1
        time.sleep(0.1)