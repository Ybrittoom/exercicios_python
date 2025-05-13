# open('arquivo.txt', 'w'): abre para escrever (sobrescreve)
# open('arquivo.txt', 'a'): abre para acrescentar
# open('arquivo.txt', 'r'): abre para ler

#escrevendo 
with open("agenda1.txt", "w") as arquivo:
    arquivo.write('Yago - 99999-1234\n')


with open("agenda1.txt", "r") as arquivo:
    print(arquivo.read())