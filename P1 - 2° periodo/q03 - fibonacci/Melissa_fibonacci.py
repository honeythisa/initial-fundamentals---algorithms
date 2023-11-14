#Construa um algoritmo que calcule o somatório dos N primeiros termos da sequencia de fibonacci.
#Exemplo:
#N = 5
#resultado: 12
#Obs.: seu algoritmo deve gerar a seguencia de fibonacci até o N-ésimo termo e, então, efetuar o somatório.
N = int(input())
def somatorio_fibonacci(N):
    if N <= 0:
        return 0
    a = 1
    b = 1
    soma = 1
    for i in range(1, N + 1): # aqui vai calcular os N primeiros termos da sequência
        soma = a + b
        a = b
        b = soma
        soma = soma - 1
    return soma
print(somatorio_fibonacci(N))