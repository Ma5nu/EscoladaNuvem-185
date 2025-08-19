print("Conversor de Moedas online")
moeda = float(input("Digite o valor em reais que deseja converter: "))
destino = input("Digite a moeda de destino: [1] Dólar [2] Euro ")

if destino == '1':
    convertido = moeda * 5.60
    print(f"O valor convertido em dólar é: ${convertido:.2f}")
elif destino == '2':
    convertido = moeda * 6.60
    print(f"O valor convertido em euro é: €{convertido:.2f}")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")