#variaveis
produto = 0
quantidade = 0
preco = 0

print("Calculadora de Preço Total\n")
print("Digite o nome do produto: ")
produto = input()
print("Digite a quantidade do Produto: ")
quantidade = int(input())
print ("Digite o preço do Produto:")
preco = float(input())

#Calculo
total = quantidade * preco
print("\n O preço total do produto", produto, "é de R$ ", total)
print ("\n Obrigada por utilizar a Calculadora de Preço Total!")
                 
# Fim do código