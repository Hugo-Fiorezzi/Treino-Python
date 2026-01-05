def maior (x,y):
    if x < y:
        print ("O maior número é", y)
    elif x == y:
        print ("Ambos tem o mesmo tamanho")
    else:
        print ("O maior número é", x)

num1 = int(input("Digite um número"))
num2 = int(input("Digite outro número"))
maior (num1, num2)