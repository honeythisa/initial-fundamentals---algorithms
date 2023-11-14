###Escreva um sub-algoritmo que imprima todos os divisores de um dado número inteiro fornecido como entrada.
numero = int(input())
def divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i) # adiciona os números divisores na lista
    return divisores
divisores = divisores(numero)
print(f"Divisores de {numero}: {divisores}")