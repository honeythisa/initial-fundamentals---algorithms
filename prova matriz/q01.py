#
print('A matriz informada devera ser uma matriz quadrada')
d = int(input('Informe a dimensão da matriz: '))
m = [[0 for i in range(d)] for j in range(d)]

for linha in range(d):
    for coluna in range(d):
        entrada = float(input(f'Informe o número da seguinte posição: Coluna {coluna + 1}, Linha {linha + 1} : '))
        m[linha][coluna] = entrada

print('Acima Diagonal Principal: ')
for linha in range(d):
    for coluna in range(linha + 1, d):
            print(f'{m[linha][coluna]} - Posição: Linha: {linha} | Coluna: {coluna}')

diagonal_sec = []
print('Abaixo Diagonal Secundaria: ')
for linha in range(d):
    for coluna in range(d):
        if (linha + coluna) > d - 1:
            diagonal_sec.append(m[linha][coluna])
            print(f'{m[linha][coluna]} - Posição: Linha: {linha} | Coluna: {coluna}')

print('\nMatriz informada: \n')
for i in range(d):
    print(m[i])