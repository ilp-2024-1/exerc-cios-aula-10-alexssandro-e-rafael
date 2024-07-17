# # Execício 1: Escreva um programa que exiba os valores dos números de 1 até 100. Ao término o
# # programa deverá exibir uma mensagem de encerramento informando que o programa
# # terminou.

from random import randint

print('Esse programa exibe os valores de 1 até 100')
n = 1
while ( n <= 100):
    print(n)
    n = n + 1
print('Fim do programa')


# #exercicio_2
# # Escreva um programa que solicita ao usuário valores numéricos e realiza a soma
# # desses valores. Quando o usuário digitar o valor 0 o programa deverá exibir o valor do
# # somatório e encerrar o programa com uma mensagem de término do programa. O
# # usuário deverá ser informado no início do programa o que o programa faz e qual a
# # condição para encerramento do programa.

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


# Exercício 3: Crie um programa que solicita ao usuário uma senha e em seguida compare esse valor
# com uma senha armazenada em uma variável. Enquanto o usuário não acertar o valor
# da senha o programa deverá solicitar a senha ao usuário. Quando o usuário acerta a
# senha, o programa deverá encerrar exibindo uma mensagem encerramento e informar
# que o usuário acertou a senha.

senha = str(input('Digite uma senha:'))
while  senha != 'Rafael':
    print('Senha incorreta!')
    senha = str(input('Digite uma nova senha:'))

print("Senha correta.")

senha = str(input('Digite uma senha:'))
if senha == 'Rafael':
    print('Senha correta!!')
elif senha != 'Rafael':
    print('Senha incorreta!')


#exercicio_4
# Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário
# para adivinhar qual é o número. O programa deve continuar pedindo palpites até que
# o usuário acerte o número. Ao final, o programa deve informar quantos palpites foram
# necessários e informar que o programa encerrou.

from random import randint, randrange
import random

r = random.randint(1,100)
print(r)
palpite = int(input("digite um numero aleatorio: "))
conta_palpite=1
while palpite != r:
    palpite = int(input("digite um numero aleatorio: "))
    conta_palpite += 1

print(f"quantidade de palpites: {conta_palpite}")
print ("fim do programa")



# # Exercício 5: Escreva um programa que solicita ao usuário um valor numérico inteiro positivo e, em
# # seguida, calcule o fatorial desse número usando um loop do tipo while. Ao final o
# # programa deverá exibir o valor do fatorial do número informado pelo usuário e término
# # do programa.

num = int(input('Digite um valor inteiro e positivo:'))
resultado = 1
count = 1

while count <= num :
    resultado *= count
    count += 1

print(resultado)

#Exercicio 6 Escreva um programa que peça ao usuário para digitar um número “n” inteiro positivo
# e, em seguida, imprima os “n” primeiros termos da sequência de Fibonacci. A
# sequência de Fibonacci é dada pela somatório de dois números que resulta no seu
# sucessor. Ex: 0, 1, 1, 2, 3, 5, 8... Esses são os 7 primeiros números da sequência.
# Exiba os números na tela e informa o término do programa ao final.
#exercicio 6. Escreva um programa que peça ao usuário para digitar um número “n” inteiro positivo
#e, em seguida, imprima os “n” primeiros termos da sequência de Fibonacci. A
#sequência de Fibonacci é dada pela somatório de dois números que resulta no seu
#sucessor. Ex: 0, 1, 1, 2, 3, 5, 8... Esses são os 7 primeiros números da sequência.
#Exiba os números na tela e informa o término do programa ao final.

def fibonacci(n, inicio):
    fib_sequen = [inicio-1, inicio]  # Inicializa a sequência com o primeiro número inserido duas vezes

    while len(fib_sequen) < n:
        fib_sequen.append(fib_sequen[-1] + fib_sequen[-2])

    return fib_sequen

# Solicita ao usuário o primeiro número da sequência
inicio = int(input("Digite o primeiro número da sequência de Fibonacci: "))

# Definir que queremos sempre 7 termos
n_termos = 7

sequence = fibonacci(n_termos, inicio)
print(f"Sequência de Fibonacci com {n_termos} termos a partir de {inicio}:")
print(sequence)


# # Exercício 7: escreva um algoritmo que solicite ao usuário um número entre 1 e 10.000 e
# # depois informe ao usuário se o número digitado é primo ou não. Um número é
# # dito ser primo quando ele é divisível apenas por 1 e ele mesmo. Ao término,
# # informe que o programa foi encerrado.

p = ('É primo')
n_p = ('Não é primo')
n1 = int(input('Digite um número entre 1 e 10.000:'))
if n1 == 3 or n1 == 2:
    print(n1,p)
elif n1 < 2:
    print(n1,n_p)
elif n1 % 2 == 0 or n1 % 3 == 0:
    print(n1,n_p)
else:
    print('Primo')
print('Fim do programa!')

# Exercicio 8 Escreva um programa que peça ao usuário para digitar um número inteiro e,
# em seguida, calcule a soma dos dígitos desse número usando um loop while.
# Ao término, informe que o programa foi encerrado.
# Ex: entrada: 19.623 à saída: 21; entrada: 456 à saída: 15;


def soma_digitos(numero):
    numero_str = str(numero)  # Converte o número para string
    soma = 0
    indice = 0
    
    while indice < len(numero_str):
        digito = int(numero_str[indice])  # Converte o caractere para inteiro
        soma += digito
        indice += 1
    
    return soma

# Exemplo de uso
numero = int(input("Digite um número: "))
resultado = soma_digitos(numero)
print(f"A soma dos dígitos do número {numero} é: {resultado}")


# # Exercício 9: escreva um programa que peça ao usuário para digitar um número n e, em
# # seguida, calcule a soma da série harmônica até o enésimo termo: H(n) = 1 +
# # 1/2 + 1/3 + ... + 1/n. Ao término, informe que o programa foi encerrado.

def calcular_serie_harmonica(n):
    soma = 0.0
    i = 1
    while i <= n:
        soma += 1 / i
        i += 1
    return soma

def main():
    while True:
        try:
            n = int(input("Digite um número inteiro positivo (ou zero para sair): "))
            if n < 0:
                print("Número inválido. Digite um número inteiro positivo (ou zero para sair).")
                continue
            elif n == 0:
                print("Encerrando o programa...")
                break
            else:
                resultado = calcular_serie_harmonica(n)
                print(f"A soma da série harmônica até o {n}-ésimo termo é: {resultado:.4f}")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo (ou zero para sair).")

    print("O programa foi encerrado.")

if __name__ == "__main__":
    main()



