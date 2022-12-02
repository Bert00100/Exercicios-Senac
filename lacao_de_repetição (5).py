n = int(input("Digite um numero "))
z = int(input("Digite o intervalo entre os numeros "))

for n in range(0, n+1, z):
    if n % 5 == 0:
        print(f"{n} mutiplo de 5")
