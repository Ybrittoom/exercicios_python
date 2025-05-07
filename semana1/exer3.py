#exercicios de loop e laços
n = int(input("Digite um numero: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i }")#f-string, um jeito mais facil de escrever variaveis em strings

import time

idade = int(input("Digite a sua idade: "))
idadeMinima = 18

while idade <= idadeMinima:
    print(f"Voce tem {idade} anos. Nao poderar dirigir")
    idade += 1