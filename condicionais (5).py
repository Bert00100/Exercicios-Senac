n_1 = int(input("Digite um numero entre 0 a 100 "))

if n_1 >= 101 or n_1 <= -1:
    print("Numero invalido")
elif n_1 <= 100 or n_1 >= 0:

    if n_1 % 2 == 0:
        print(f"{n_1} é par")
else:
    print(f"{n_1} é impar")
