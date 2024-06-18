#compara variaveis

num1 = int(input("insira um numero: "))
num2 = int(input("insira um numero: "))
num3 = int(input("insira um numero: "))

print("numero 1 é maior que o numero dois,", num1>num2)
print("numero 2 é maior que o numero 1 e 2", num2>num1 and num2>num3)
print("numero 3 e maior ou igual ao numero 1", num3>=num1)
print("numero 3 é maior que o numero 1 ou 2", num3>num1 or num3>num2)