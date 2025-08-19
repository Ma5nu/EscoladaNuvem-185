print("Calculadora de Horas Trabalhadas")
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor pago por hora: "))
salario = horas_trabalhadas * valor_por_hora
print(f"O salário total é: R$ {salario:.2f}")