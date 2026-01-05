for n in range (0,5):
    print (n)

##Números pares e sua soma

somap = 0 
contp = 0
somai = 0
conti = 0

for c in range (1,6):
    num = int(input(f"Digite o {c} valor"))
    if num % 2 == 0:
        somap += num
        contp += 1
    else:
        somai += num
        conti += 1
print (f"Você digitou {contp} números pares, {conti} números ímpares e a soma de pares é {somap}, já a soma de ímpares é {somai}.")

#Uso simples do While

c = 1
while c <= 10:
    s = c + 10
    print(s)
    c += 1
print("Acabou")