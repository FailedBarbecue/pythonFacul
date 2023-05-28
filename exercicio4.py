print("Bem vindo ao controle de estoque da biciletaria do Eduardo Schiavo") #identificador pessoal

codigo_peca = 0
lista_peca = []

def cadastrarPeca(codigo):
  print("Bem vindo ao menu de cadastrar pecas")
  print("Código da peça: {}".format((codigo_peca)))
  nome = input("Entre com o nome do peça: ")
  fabricante = input("Entre com o fabricante do peça: ")
  preco = int(input("Entre com o preco(R$) do peça: "))
  dicionario_peca = {
      "codigo" : codigo,
      "nome" : nome,  
      "fabricante" : fabricante,  
      "preco" : preco
      }
  lista_peca.append(dicionario_peca.copy())

def consultarPeca():
  print("Bem vindo ao menu de consultar pecas")

  while True:
   consultar_peca = input("\nEscolha a opção desejada:\n" +
                           "1 - Consultar TODAS os peças\n" +
                           "2 - Consultar peça por código\n" +
                           "3 - Consultar peça por fabricante\n" +
                           "4 - Retornar\n" +
                           ">>: ")
   if consultar_peca == '1':
     print("Você escolheu consultar TODAS os peças")
     for peca in lista_peca: 
       print("------------------------")
       for key, value in peca.items(): #pra cada chave e valor dentro de peca.items
         print("{}: {}".format(key, value)) #mostra chave e valor
       print("------------------------")
   elif consultar_peca == "2":
    print("Você escolheu consultar peça por código")
    codigo_desejado = int(input("Entre com o código desejado: "))
    for peca in lista_peca:
      if peca["codigo"] == codigo_desejado:
         print("------------------------")
         for key, value in peca.items(): #pra cada chave e valor dentro de peca.items
          print("{}: {}".format(key, value)) #mostra chave e valor
         print("------------------------")
   elif consultar_peca == "3":
    print("Você escolheu consultar peça por fabricante")
    fabricante_desejado = input("Entre com o fabricante desejado: ")
    for peca in lista_peca:
      if peca["fabricante"] == fabricante_desejado:
         print("------------------------")
         for key, value in peca.items(): #pra cada chave e valor dentro de peca.items
          print("{}: {}".format(key, value)) #mostra chave e valor
         print("------------------------")
   elif consultar_peca == "4":
    return #sai da funcao consultarPeca
   else: 
    print("Opcao invalida. Tente novamente")
    continue #Volta ao comeco do while 

def removerPeca():
  print("Bem-vindo ao menu de remover peça")
  codigo_desejado = int(input("Entre com o código do peça que deseja remover: "))
  for peca in lista_peca:
    if peca['codigo'] == codigo_desejado:
      lista_peca.remove(peca)
      print("Peça removida")
while True:
  primeira_opcao = input("\nEscolha a opção desejada:\n" +
                           "1 - Cadastrar peça\n" +
                           "2 - Consultar peça(s)\n" +
                           "3 - Remover peça\n" +
                           "4 - Sair\n" +
                           ">>: ")
  if primeira_opcao == '1':
    codigo_peca = codigo_peca + 1
    cadastrarPeca(codigo_peca)
  elif primeira_opcao == "2":
    consultarPeca()
  elif primeira_opcao == "3":
    removerPeca()
  elif primeira_opcao == "4":
    break #Fecha o programa
  else: 
    print("Opcao invalida. Tente novamente")
    continue #Volta ao comeco do while 
     
