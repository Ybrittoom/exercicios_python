import semana2.dia1.ParouImpar as parImp

def parImpar():
    numero = parImp.numeroAleatorio()
    if numero % 2 == 0:#verifica se o numero e par 
        print(f'O numero {numero} é par')
    else:
        print(f'O numero {numero} é impar')

parImpar()
