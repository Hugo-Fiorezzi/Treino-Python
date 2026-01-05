import numpy as np

n = 39

##Utilizando o NumPy sem importar a função específica

raiz = np.sqrt (n)
print (f"A raiz quadrada de {n} é {raiz:.2f}")

##Teste de raiz com expoente sem o NumPy

raiz2 = 25 ** 0.5
print (raiz2)

##Apenas um teste de importação de funções

import math
from math import factorial, sqrt

fat = factorial(int(sqrt(16)))
print (fat)