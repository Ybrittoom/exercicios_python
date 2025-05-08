import time

print('OLA, BEM-VINDO AO ALISTAMENTO DO EXERCITO BRASILEIRO')
time.sleep(3)
print('Vou passar as fichas com os dado que deve ser preenchidos')
time.sleep(3)
input('Antes de começar Você já tem alguma informação sobre o processo de alistamento ou é a sua primeira vez aqui?')

nome = input("Qual o seu nome?: ")
dataDeNascimento = (input('Qual a sua data de nascimento(dd/mm/aaaa)?: '))
nomeDoPai = input('Qual o nome do seu Pai?: ')
nomeDaMae = input('Qual o nome da sua Mae?: ')
endereco = input('Endereço Completo (Rua, Número, Bairro, Cidade, Estado, CEP)?: ').split(',')
nivelEscolaridade = input('Qual o seu nivel de escolaridade?: ')
profissao = input('Qual a sua profissao?(opcional): ')
deficiencia = input('Possui alguma deficiencia? (Sim/Não) ')
saude = input('Possui algum problema de saude? (sim/nao) ')

#armazena a data de nascimento aqui, separada por '/'
dataNascimento = dataDeNascimento.split('/')
#armaxena o endereço aqui, separado por ','
enderecoDaPessoa = endereco

if deficiencia.lower() == 'sim':
    deficiencia = input('Qual(s) a sua deficiencia?: ')

if saude.lower() == 'sim':
    saude = input('Qual o seu problema de saude?: ')


listaDePessoas = []
pessoa = {
    "nome": nome,
    "data_de_nascimento": dataDeNascimento,
    "nome_do_pai": nomeDoPai,
    "nome_da_mae": nomeDaMae,
    "endereco": endereco,
    "nivel_de_escolaridade": nivelEscolaridade,
    "profissao": profissao,
    "deficiencia": deficiencia,
    "saude": saude
}

listaDePessoas.append(pessoa)

print(listaDePessoas)
