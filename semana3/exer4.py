#salvando dados em json
import json

dados = {"nome": "Ygor", "notas": 9}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)