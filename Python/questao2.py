# 2. Uma empresa decidiu dar bônus aos colaboradores baseada no tempo de serviço.
# • Tempo de serviço > 10 anos – 10 %
# • 6 anos <= Tempo de serviço <= 10 anos – 8 %
# • Tempo de serviço <= 10 anos – 5 %
# Apresente o valor líquido de aumento dado o tempo de serviço e salário do
# colaborador

temp_serv = int(input("Tempo de serviço (em anos): "))
salario = float(input("Valor do salário: "))

if temp_serv > 10:
    aumento = 0.10
elif 6 <= temp_serv <= 10:
    aumento = 0.08
else:
    aumento = 0.05

aumento_final = salario * aumento

salario_final = salario + aumento_final

print(f"Tempo de Serviço: {temp_serv} anos")
print(f"Salário Inicial: R${salario:.2f}")
print(f"Aumento Percentual: {aumento * 100:.0f}%")
print(f"Valor do Aumento: R${aumento_final:.2f}")
print(f"Salário Final: R${salario_final:.2f}")
