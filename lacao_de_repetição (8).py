n1 = int(input("Digite o começo do laço "))
n2 = int(input("Digite o fim do laço "))
soma_par = 0

for n2 in range(n1, n2):
    print(n2)
    if n2 % 2 == 0:
        soma_par = soma_par + n2

print(f"A soma dos pares são, {soma_par}")
