linhas = 3
colunas = 4
m = [[0 for i in range(colunas)] for i in range(linhas)]

somaTotal = 0
contadorElementos = 0
contadorPar = 0
somaImpar = 0

for i in range(linhas):
    for e in range(colunas):
        m[i][e] = int(input(f'Informe o valor da seguinte posição: Linha: {i + 1} | Coluna: {e + 1}  '))

for i in range(linhas):
    for e in range(colunas):
        somaTotal = somaTotal + m[i][e]
        contadorElementos += 1

# a quantidade de elementos pares da matriz
        if m[i][e] % 2 == 0:
            contadorPar += 1
# a soma dos elementos ímpares contidos na matriz
        else:
            somaImpar = somaImpar + m[i][e]

mediaElementos = somaTotal / contadorElementos

# mostrar no console
print("")
print(f'A matriz informada contem {contadorPar} elementos pares.')
print("")
print(f'A soma dos elementos ímpares informados na matriz é de: {somaImpar}')
print("")
print(f'A média de todos os elementos da matriz é de: {mediaElementos}')
print("")