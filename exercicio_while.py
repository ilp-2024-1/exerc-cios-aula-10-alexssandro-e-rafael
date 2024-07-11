#exercicio_2
# Escreva um programa que solicita ao usuário valores numéricos e realiza a soma
# desses valores. Quando o usuário digitar o valor 0 o programa deverá exibir o valor do
# somatório e encerrar o programa com uma mensagem de término do programa. O
# usuário deverá ser informado no início do programa o que o programa faz e qual a
# condição para encerramento do programa.

print("esse programa soma dois numeros inteiros")
V_numerico1 = int(input("insira um valor numerico:"))

V_numerico2 = int(input("insira um valor numerico:"))

resultado = V_numerico1 + V_numerico2


while resultado:
    print(resultado)
    V_numerico1 = int(input("insira um valor numerico:"))

    V_numerico2 = int(input("insira um valor numerico:"))

    resultado = V_numerico1 + V_numerico2

    
    print (resultado)
    print("fim do programa")

    break

#exercicio_4
# Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário
# para adivinhar qual é o número. O programa deve continuar pedindo palpites até que
# o usuário acerte o número. Ao final, o programa deve informar quantos palpites foram
# necessários e informar que o programa encerrou.



# from random import randint
# import random

# continuar= int(input("digite um numero aleatorio"))
# while continuar:
   
#   r = random.randint(1,100)
# print(r)
# continuar=int(input(""))


