idade = int(input("digite sua idade: "))

if (idade>=18):
    print("voce eh maior de idade")

else:
    print("voce eh menor de idade")

#imprime na ordem crescente

num1 = int(input("insira um numero: "))
num2 = int(input("insira um numero: "))

if (num1<num2):
    print(num1)
    print(num2)

else:
    print(num2)
    print(num1)

#imprime aprovado/reprovado com base nas notas

nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))
nota3 = float(input("insira a terceira nota: "))

media = (nota1+nota2+nota3)/3

if (media>5.0):
    print("media eh: %.1f - aprovado"% media)

else:
    print("media eh: %.1f - reprovado"% media)
