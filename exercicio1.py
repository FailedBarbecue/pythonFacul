print("Bem vindo a loja do Eduardo Schiavo")

valor_produto = float(input("Digite o valor do produto: "))
qtd_produto = int(input("Digite a quantidade desejada: "))
desconto_produto =  0
if qtd_produto < 9: #Se a quantidade de produto for menor que 9 = 0% de desconto
  desconto_produto = 0.00
elif qtd_produto >= 10 and qtd_produto < 100: #Se a quantidade de produto for maior ou igual a 10 e menor que 100 = 5% de desconto
  desconto_produto = 0.05
elif qtd_produto >= 100 and qtd_produto < 1000:
  desconto_produto = 0.10
else:
  desconto_produto = 0.15  #Se a quantidade de produto for maior que 1000 = 15% de desconto

total = valor_produto * qtd_produto

print("O valor total sem desconto e de: R${:.2f}".format(total))
total_com_desconto = total - total * desconto_produto
print("O valor total com desconto e de: R${:.2f}".format(total_com_desconto))
