algoritmo "calculadora"
var
  opcao : inteiro

  
  // monta o menu de opções da calculadora na tela e aguarda o usuário escolher a opção desejada
  funcao menu() : inteiro
  var
     op : inteiro
  inicio
     escreval(".:: Calculadora ::.")
     escreval("    1. X + Y       ")
     escreval("    2. X - Y       ")
     escreval("    3. X * Y       ")
     escreval("    4. X / Y       ")
     escreval("    5. X!          ")
     escreval("    6. sen( x )    ")
     escreval("    7. cos( x )    ")
     escreval("    8. tan( x )    ")
     escreval("    9. f(x, y) = (x^2 + y^3)/(x - y)")
     escreval("   10. sair ")
     escreva(" opcao: ")
     leia( op )
     retorne op
  fimfuncao
  
  // pausa a execução, pedindo para o usuário pressionar qualquer tecla para prosseguir
  procedimento pausar()
  var
     v : caracter
  inicio
     escreva("Pressione uma tecla para continuar")
     leia(v)
  fimprocedimento
  
inicio
  // algoritmo principal
  
  
  repita
     opcao <- menu()
     
     // lista de operações disponíveis na calculadora
     escolha opcao
        caso 1
           escreval("[TESTE] opcao 1")
        caso 2
           escreval("[DEBUG] opcao 2")
        caso 3
           escreval("[DEBUG] opcao 3")
        caso 4
           escreval("[DEBUG] opcao 4")
        caso 5
           escreval("[DEBUG] opcao 5")
        caso 6
           escreval("[DEBUG] opcao 6")
        caso 7
           escreval("[DEBUG] opcao 7")
        caso 8
           escreval("[DEBUG] opcao 8")
        caso 9
           escreval("[DEBUG] opcao 9")
        caso 10
           escreval("[DEBUG] saindo da calculadora")
        outrocaso
            // opção para códigos inválidos digitados pelo usuário
            escreval("Opcao invalida")
     fimescolha
     pausar()
  ate opcao = 10
  
  escreval("Calculadora finalizada!")
fimalgoritmo
