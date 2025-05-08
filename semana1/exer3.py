#exercicios de loop e laços
# n = int(input("Digite um numero: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i }")#f-string, um jeito mais facil de escrever variaveis em strings

import time

idade = int(input("Digite a sua idade: "))
idadeMinima = 18

while idade <= idadeMinima or idade > idadeMinima:
    if idade <= idadeMinima:
        print(f'Voce tem {idade} anos, nao podera dirigir')
    else:
        print(f'Voce tem {idade} anos, podera dirigir')
    idade += 1
    time.sleep(0.1)
    