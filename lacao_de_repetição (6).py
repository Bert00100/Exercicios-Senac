soma = 0
numero = 0
maior_numero = 0
menor_numero = 0
numero_negativo = 0

while (numero >= 0):
    numero = int(input("Digite um numero "))
    if maior_numero < numero:
        maior_numero = numero
    elif maior_numero > numero and numero > menor_numero:
        menor_numero = numero

    if numero <= -1:
        numero_negativo = numero

    soma = soma + numero - numero_negativo


print(soma, "Soma")
print(maior_numero, "Maior numero")
print(menor_numero, "Menor numero")
