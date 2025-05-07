#float refere-se a um tipo de dado que representa números de ponto flutuante, ou seja, números com casas decimais
num = float(input("Digite um Numero:"))
#pode se usar em projetos onde precisam de calculo decimal

if num > 0:
    print("Numero positivo", num)
elif num < 0:
    print("Numero negativo", num)
else:
    print("Zero")

#verificador de maior idade
idade = int(input("Digite a sua idade: "))

if idade < 18:
    print('Voce e menor de idade: ', idade)
else:
    print('Voce e maior de idade: ', idade)