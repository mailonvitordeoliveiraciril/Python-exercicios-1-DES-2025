dias = 3
dia01 = int(input("dias para a atividade 01"))
dias02 = int(input("dias para a atividade 02"))
dias03 = int(input("dias para a atividade o3"))

soma = dia01 + dia02 + dias03
if dia01 < 0 or dia02 < o or dia03 < 0:
    print("erro numero negativo")
else:
    soma = dia01 + dia02 + dias03
    print(f"tempo total do projeto: {soma} dias")