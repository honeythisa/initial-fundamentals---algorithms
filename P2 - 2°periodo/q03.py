# Escreva um programa, em python, que atenda às seguintes funcionalidades:
# leia valores reais e armazene-os em uma matriz 6×6.
# calcule a média dos elementos da área assinalada em cinza (ver figura abaixo)
# determinar o maior elemento contido na matriz;
# verificar se um determinado valor (passado como parâmetro) está contido na matriz. Esse valor deve ser informado pelo usuário, via leitura;
# fazer a varredura da matriz e devolução dos elementos contidos em sua diagonal principal, copiados para um vetor.

def ler_matriz():
    matriz = []
    for i in range(6):
        linha = []
        for j in range(6):
            valor = float(input(f"Informe o valor para a posição ({i + 1},{j + 1}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def media_cinza(matriz):
    soma = 0
    count = 0
    for i in range(1, 5):
        for j in range(1, 5):
            soma += matriz[i][j]
            count += 1
    return soma / count

def maior_elem(matriz):
    maior = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
    return maior

def verificar(matriz, valor):
    # vê se um valor está contido na matriz
    for linha in matriz:
        if valor in linha:
            return True
    return False

def diagonal(matriz):
    diagonal = []
    for i in range(6):
        diagonal.append(matriz[i][i])
    return diagonal

def exibir_menu():
    print("\n--- Menu ---")
    print("1. Calcular média da área assinalada em cinza")
    print("2. Encontrar o maior elemento na matriz")
    print("3. Verificar se um valor está na matriz")
    print("4. Mostrar elementos na diagonal principal")
    print("0. Sair")

# Leitura da matriz
matriz = ler_matriz()

while True:
    exibir_menu()
    escolha = input("Escolha uma opção (0-4): ")

    if escolha == "1":
        # Cálculo da média da área assinalada em cinza
        media = media_cinza(matriz)
        print(f"Média da área assinalada em cinza: {media}")

    elif escolha == "2":
        # Determinar o maior elemento contido na matriz
        maior = maior_elem(matriz)
        print(f"Maior elemento na matriz: {maior}")

    elif escolha == "3":
        # Verificar se um determinado valor está contido na matriz
        valor = float(input("Informe um valor para verificar se está na matriz: "))
        if verificar(matriz, valor):
            print(f"O valor {valor} está na matriz.")
        else:
            print(f"O valor {valor} não está na matriz.")

    elif escolha == "4":
        # Varredura da matriz e devolução dos elementos contidos na diagonal principal
        diagonal_elems = diagonal(matriz)
        print(f"Elementos na diagonal principal: {diagonal_elems}")

    elif escolha == "0":
        # Sair do programa
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")