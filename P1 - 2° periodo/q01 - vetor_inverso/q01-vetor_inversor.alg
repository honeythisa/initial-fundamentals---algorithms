algoritmo "Vetor_inversor"
var
   vetoriginal: vetor[0..9] de real
   vetinversor: vetor[0..9] de real
   i, j: inteiro
inicio
   Para i de 0 ate 9 faca
      Leia(vetoriginal[i])
   FimPara

   j <- 9
   Para i de 0 ate 9 faca
      vetinversor[j] <- vetoriginal[i]
      j <- j - 1
      i <- i + 1
   FimPara

   Para i de 0 ate 9 faca
      Escreva(vetinversor[i])
   FimPara
fimalgoritmo
