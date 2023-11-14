vetoriginal = [0]*10

for i in range(10):
    vetoriginal[i] = float(input())
def inversor(vet):
    vetInversor = vet[::-1] # esse [::-1] é um metodo que inverte o conteudo
    return vetInversor

vetInvertido = inversor(vetoriginal)
print("Vetor invertido:", vetInvertido)