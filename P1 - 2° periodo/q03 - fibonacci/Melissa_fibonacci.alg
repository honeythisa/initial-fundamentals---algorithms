algoritmo "Fibonacci"
var
   n, i, a, b, soma: inteiro
inicio
      leia(n)
      a <- 1
      b <- 1
      soma <- 1
      para i de 1 ate n faca
        soma <- a + b
        a <- b
        b <- soma
        soma <- soma - 1
        escreva(soma)
    fimPara
fimalgoritmo
