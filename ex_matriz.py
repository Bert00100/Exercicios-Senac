matriz = [[0, 0],
          [0, 0], ]
for c in range(0, 2):
    for l in range(0, 2):
        matriz[l][c] = int(input(f"Digite o valor da matriz: "))

soma = matriz[0][0] + matriz[0][1]
print(matriz)
print(soma)
