import os
vet_list = []
maior = 0
menor = 0
for c in range(0, 5):
    vet_list.append(int(input(f"Digite o valor do vetor  {c} :")))
    if c == 0:
        maior = vet_list[0]
        menor = vet_list[0]
    else:
        if vet_list[c] > maior:
            maior = vet_list[c]
        if vet_list[c] < menor:
            menor = vet_list[c]

os.system("cls")

print(f"os numeros digitados são: {vet_list}")
print(f"O maior numero é: {maior}")
print(f"O menor numero é: {menor}")
