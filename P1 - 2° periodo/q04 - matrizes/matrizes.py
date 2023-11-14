# Soma e Produto matrizes
# leitura de duas matrizes quadradas (3 linhas x 3 colunas) de valores reais
M1 = [[0.0] * 3 for _ in range(3)]
M2 = [[0.0] * 3 for _ in range(3)]
matSoma = [[0.0] * 3 for _ in range(3)]
matProduto = [[0.0] * 3 for _ in range(3)]

print("MATRIZ M1")
for i in range(3):
    for j in range(3):
        M1[i][j] = float(input(f"Informe o valor da posição para Linha {i + 1} e Coluna {j + 1}: "))

print("\nMATRIZ M2")
for i in range(3):
    for j in range(3):
        M2[i][j] = float(input(f"Informe o valor da posição para Linha {i + 1} e Coluna {j + 1}: "))

for i in range(3):
    for j in range(3):
        matSoma[i][j] = M1[i][j] + M2[i][j]

for i in range(3):
    for j in range(3):
        for k in range(3):
            matProduto[i][j] += M1[i][k] * M2[k][j]

print("\nSoma das matrizes:")
for i in range(3):
    for j in range(3):
        print(matSoma[i][j], end=" ")
    print()

print("\nProduto das matrizes:")
for i in range(3):
    for j in range(3):
        print(matProduto[i][j], end=" ")
    print()