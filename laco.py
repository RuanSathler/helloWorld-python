#imprimir os numeros de 0 a 10

for num in range(10):
    print(num)

#imprime os numeros de 10 a 15

for num in range(10, 16):
    print(num)

#imprime os numeros em ordem decrecenste

for num in range(15, 0, -1):
    print(num)

#enguanto um numero negativo n entrar, somar os numeros e dar a sua média

qunt = 0
soma = 0
media = 0
num = float(input("insira um numero: "))

while (num>0.0):
    qunt = qunt+1
    soma = soma+num

    num = float(input("insira um numero: "))

media = soma / qunt

print("/n total da soma: ", soma)
print("/n quantidade de numeros lidos: ", qunt)
print("/n media dos valores: ", media)