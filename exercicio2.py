print("Olá, bem vindo a lanchonete do Eduardo Schiavo") #identificadand pessoal

print("-----------------------------CARDÁPIO-----------------------------")
print("Codigo         |       Descriçao             |       Valor(R$)")
print(" 100           |    Cachorro-Quente          |         9,00    ")
print(" 101           |    Cachorro-Quente Duplo    |         11,00    ")
print(" 102           |    X-Egg                    |         12,00    ")
print(" 103           |    X-Salada                 |         13,00    ")
print(" 104           |    X-Bacon                  |         14,00    ")
print(" 105           |    X-Tudo                   |         17,00    ")
print(" 200           |    Refrigerante Lata        |         5,00    ")
print(" 201           |    Chá Gelado               |         4,00    ")

valor = 0

while True: 
  codigo = input("Entre com o codigo desejado: ")
  
  if codigo == "100":
    valor = valor + 9
    descricao = "Cachorro-Quente"
  elif codigo == "101":
      valor = valor + 11
      descricao = "Cachorro-Quente Duplo"
  elif codigo == "102":
     valor = valor + 12
     descricao = "X-Egg"
  elif codigo == "103":
     valor = valor + 13
     descricao = "X-Salada" 
  elif  codigo == "104":
     valor = valor + 14
     descricao = "X-Bacon"
  elif  codigo == "105":
     valor = valor + 17
     descricao = "X-Tudo" 
  elif codigo == "200":
     valor = valor + 5
     descricao = "Refrigerante Lata"
  elif codigo  =="201":
    valor = valor + 4
    descricao = "Chá Gelado"
  else:
    print("Opção invalida")
    continue # caso usuario coloque um valor que não seja valido retorna ao comeco do while
  print("Voce pediu um {} e o Valor total é {}".format(descricao, valor))
  print("Gostaria de mais alguma coisa?")
  print("1 - Sim")
  print("2 - Não")
  comprar_mais = input()
  if comprar_mais == "1":
      continue
  elif comprar_mais == "2": 
      print("O total a ser pago é {}".format(valor))
      break # Fecha o programa
  else:
     print("Opção invalida")
     continue
      
    