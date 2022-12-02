vendedor: str
salario: float
vendas: float

vendedor = (input("Digite o nome do vendedor "))
salario = (float(input("Digite o valor do salario ")))
vendas = (float(input("Digite quanto ele vendeu no mes ")))

print(f"{vendedor} recebe {vendas*0.15+salario}")
