# Questão1

# for i in range(2,13,2):
#     print(i)

#Questão2

# valor = int(input("Digite um valor"))
# for i in range(valor):
#     print(i+1)

#Questão3
# vInicial = int(input("Digite um valor"))
# vFinal = int(input("Digite um valor"))

# for i in range(vInicial, vFinal+1):
#     print(i)
# print("O programa foi encerrado")

#Questão4

# vInicial = int(input("Digite um valor"))
# vFinal = int(input("Digite um valor"))

# for i in range(vInicial+1, vFinal):
#     print(i)
# print("O programa foi encerrado")


#Questão5

vInicial = int(input("Digite um valor"))
vFinal = int(input("Digite um valor"))
result=0

for i in range(vInicial, vFinal):
    if i > 1:
        primo = True
    for j in range(2, i):
        if i%j == 0:
            primo = False
        if primo:
            print(result)
   

#Questão6
firstValue = int(input("Digite a temperatura inicial em Celsius"))
finalValue = int(input("Digite a temperatura final em Celsius"))
increment = int(input("Digite o incremento"))

for i in range(firstValue, finalValue, increment):
    print(f"{i}°C")

for j in range(firstValue, finalValue, increment):
    fahranheit =j*1.8+32