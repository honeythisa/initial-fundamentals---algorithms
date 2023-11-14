#Construa um subprograma que, recebendo como parâmetros quatro números inteiros, devolva ao módulo que o chamou a soma dos três maiores números dentre os quatro recebidos.
#O programa principal deverá ler tantos conjuntos de quatro valores quantos o usuário deseje e que acione o subprograma para cada conjunto de valores, apresentando a cada vez a soma produzida.

def soma_tres_maiores(a, b, c, d):

    if a >= b and a >= c and a >= d: # verificando A
        return a + b + c
    elif b >= a and b >= c and b >= d: # verificando B
        return b + c + d
    elif c >= a and c >= b and c >= d: # verificando C
        return c + b + d
    else:
        return d + b + c # por fim D

# programa principal
qtdeConjuntos = int(input("Digite a quantidade de conjuntos de quatro valores: "))

for i in range(qtdeConjuntos): # a qtd vai somando até atingir a qtde conjuntos
    print("\nConjunto", i+1)
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    d = int(input("Digite o quarto valor: "))
    
    soma = soma_tres_maiores(a, b, c, d)
    print("A soma dos três maiores números é:", soma)