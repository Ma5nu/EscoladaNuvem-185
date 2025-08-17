#variaveis
import math

comprimento = 0
largura = 0
altura = 0

#Recebimento dos dados
print("Calculadora de Volume\n")
print("Digite o comprimento em cm: ")
comprimento = float(input())
print("Digite a largura em cm: ")
largura = float(input())
print("Digite a altura em cm: ")
altura = float(input())

#Calculo
volume = comprimento * largura * altura
print("\n O Volume total é: ", volume, "cm")
