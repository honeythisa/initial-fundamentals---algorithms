algoritmo "Matrizes"
var
   M1, M2, matSoma, matProduto: vetor [1..3, 1..3] de Real
   i, j, k: inteiro
inicio
      escreval("MATRIZ M1")
   para i de 1 ate 3 faca
      para j de 1 ate 3 faca
         escreva("Informe o valor da posição para Linha e Coluna [", i, ",", j, "]: ")
         leia(M1[i, j])
      fimpara
   fimpara

   escreval("MATRIZ M2")
   para i de 1 ate 3 faca
      para j de 1 ate 3 faca
         escreva("Informe o valor da posição para Linha e Coluna [", i, ",", j, "]: ")
         leia(M2[i, j])
      fimpara
   fimpara

   para i de 1 ate 3 faca
      para j de 1 ate 3 faca
         matSoma[i, j] <- M1[i, j] + M2[i, j]
      fimpara
   fimpara

   para i de 1 ate 3 faca
      para j de 1 ate 3 faca
         matProduto[i, j] <- 0
         para k de 1 ate 3 faca
            matProduto[i, j] <- matProduto[i, j] + (M1[i, k] * M2[k, j])
         fimpara
      fimpara
   fimpara

escreval("soma das matrizes")
   para i de 1 ate 3 faca
      para j de 1 ate 3 faca
         escreva(matSoma[i, j], " ")
      fimpara
      escreval("")
   fimpara

escreval("produto das matrizes")
   para i de 1 ate 3 faca
      para j de 1 ate 3 faca
         escreva(matProduto[i, j], " ")
      fimpara
      escreval("")
   fimpara
fimalgoritmo

