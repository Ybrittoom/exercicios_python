try:
    numero = int(input("Digite um Numero: "))
    print(10 / numero)
except ValueError:
    print('Voce digitou algo que nao é numero!')
except ZeroDivisionError:
    print('Nao é possivel dividir com zero 0!')
finally:
    print('fim do programa')