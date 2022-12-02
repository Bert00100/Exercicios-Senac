n_1 = int(input("Digite um numero "))

for n_1 in range(0, n_1):
    if n_1 == 0:
        print(f"{n_1} nulo")

    if n_1 % 2 == 0:
        print(f"{n_1} par")
    else:
        print(f"{n_1} impar")
