# Faça um programa que leia quatro matrizes inteiras, 5 × 5 (A, B, C e D), com pelo menos dois subprogramas:
# um que carrega valores em uma matriz, a ser usado para a leitura das quatro matrizes, e um segundo que recebe duas matrizes 5 × 5 e calcula a matriz soma.

# Aplique esse último subprograma para obter A + B, C + D e A + C

# Função para carregar valores em uma matriz
def carregar_matriz():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(5):
            valor = int(input(f"Digite o valor para a posição [{i + 1}][{j + 1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def soma_matrizes(matriz1, matriz2):
    resultado = []
    for i in range(5):
        linha = []
        for j in range(5):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        resultado.append(linha)
    return resultado

# Carregar as matrizes A, B, C e D
print('=-'*10)
print("matriz A")
A = carregar_matriz()

print('=-'*10)
print("\nmatriz B")
B = carregar_matriz()

print('=-'*10)
print("\nmatriz C")
C = carregar_matriz()

print('=-'*10)
print("\nmatriz D")
D = carregar_matriz()

# Calcular e imprimir A + B, C + D e A + C
r_AB = soma_matrizes(A, B)
r_CD = soma_matrizes(C, D)
r_AC = soma_matrizes(A, C)

print("\nresultado A + B")
for linha in r_AB:
    print(linha)

print("\nresultado C + D")
for linha in r_CD:
    print(linha)

print("\nresultado A + C")
for linha in r_AC:
    print(linha)