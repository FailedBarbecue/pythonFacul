print("Bem vindo a companhia de logística do Eduardo Schiavo") # Identificador pessoal

def dimensoesObjeto():
  while True:
    try:
      altura = int(input("Qual a altura do objeto? (cm): "))
      comprimento = int(input("Qual a comprimento do objeto? (cm): "))
      largura = int(input("Qual a largura do objeto? (cm): "))
      volume = altura * largura * comprimento
      if volume < 1000:
        valor = 10
      elif volume >= 1000 and volume < 10000:
        valor = 20
      elif volume >= 10000 and volume < 30000: #  Verificando as dimensoes do objeto
        valor = 30
      elif volume >= 30000 and volume < 100000:
        valor = 50
      else:
        print("Não aceitamos objetos com dimensoes tão grandes")
        continue
    except ValueError:
        print("Você digitou alguma dimensão do objeto com um valor não numérico") #Caso o usuario digite uma dimensão inválida
        print("Por favor, digite o as dimensões novamente")
        continue
    print("O volume do objeto (em cm) é:", volume)
    return valor
       

def pesoObjeto():
  while True:
    try:
      peso = float(input("Qual o peso do objeto? (kg): "))
      if peso <= 0.1:
        multiplicador = 1
      elif peso >= 0.1 and peso < 1:
        multiplicador = 1.5
      elif peso >= 1 and peso < 10: #  Verificando o peso do objeto
        multiplicador = 2
      elif peso >= 10 and peso < 30:
        multiplicador = 3
      else:
        print("Não aceitamos objetos tão pesados")
        continue
    except ValueError:
      print("Você digitou o peso com um valor não numérico") #Caso o usuario digite um peso invalido
      print("Por favor, digite o peso novamente")
      continue
    return multiplicador
  

def rotaObjeto():
    while True:
      print("Digite a rota:")
      print("RS - De Rio de Janeiro até São Paulo")
      print("SR - De São Paulo até Rio de Janeiro")
      print("BS - De Brasília até São Paulo")
      print("SB - De São Paulo até Brasília")
      print("BR - De Brasília até Rio de Janeiro")
      print("RB - Rio de Janeiro até Brasília")
      rota = input()
      if rota == "RS" or rota == "rs":
        multiplicador = 1
      elif rota == "SR" or rota == "sr":
        multiplicador = 1
      elif rota == "BS" or rota == "bs": #  Verificando a rota de entrega
        multiplicador = 1.2
      elif rota == "SB" or rota == "sb":
        multiplicador = 1.2
      elif rota == "BR" or rota == "br":
        multiplicador = 1.5
      elif rota == "RB" or rota == "rb":
        multiplicador = 1.5
      else:
        print("Você digitou uma rota inexistente") #Caso o usuario digite uma rota invalida
        print("Por favor, digite a rota novamente") 
        continue
      return multiplicador

dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota
print("Total a pagar(R$): {:.2f} (dimensões: {} * multiplicador de peso: {} * multiplicador de rota: {})".format(total, dimensoes, peso, rota))