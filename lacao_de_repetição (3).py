altura_maior = 0
menor_altura = 0
media = 0
for altura in range(0, 3):
    altura = int(input("Digite tres alturas e mostrarei a maior:  "))

    if altura > altura_maior:
        altura_maior = altura
    elif altura > menor_altura and altura_maior > menor_altura:
        menor_altura = altura
    media = media + altura / 3

print(f"A maior altura é: {altura_maior}")
print(f"O menor numero é {menor_altura}")
print(f"media {media}")
