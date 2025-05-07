#este e um exemplo que variavel e uma pequena calculadora no terminal

#criando uma variavel(valorUm e valorDois)
valorUm = int(input("Digite o primeiro valor:"))#input exibe a mensagem 
valorDois = int(input("Digite o segundo valor:"))#int converte o valor digitado em numero

operacao = input("Escolha a operaçao desejada:")#exibe uma mensagem

if operacao == "soma"or operacao == "SOMA":
    print(valorUm + valorDois)
elif operacao == "subtraçao" or operacao == "SUBTRAÇAO":
    print(valorUm - valorDois)
elif operacao == "multiplicaçao" or operacao == "MULTIPLICAÇAO":
    print(valorUm * valorDois)
elif operacao == "divisao" or operacao == "DIVISAO":
    print(valorUm / valorDois)
else:
    print("Sem resultado")