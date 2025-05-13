#usar e importar bibliotecas(modulos) do python
import math #importa uma funçao
print(math.sqrt(16))

#importa uma funçao especifica
from math import sqrt
print(sqrt(25))

#as: renomeia um modulo
import random as r
print(r.randint(1, 10))


#importanto um modulo proprio de moduloProprio/meu_modulo.py
import semana2.dia1.meu_modulo as meu_modulo
meu_modulo.saudacao('yago')

import semana2.dia1.meu_modulo as meu_modulo
meu_modulo.idadeMinima()