import numpy as np
from random import randint

nota = randint (1,10)

if nota >= 6:
    print (f"Sua nota foi {nota}, você foi aprovado!")
elif nota >= 5 and nota <6:
    print (f"Sua nota foi {nota}, você está de recuperação!")
else:
    print (f"Sua nota foi {nota}, você foi reprovado!")