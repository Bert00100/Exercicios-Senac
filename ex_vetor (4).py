import os
os.system("cls")
vet = []
while True:
    n = int(input("Digite o valor do vetor  "))
    if n not in vet:
        vet.append(n)
        print("Numeor add")
    else:
        print("Valor duplicado")
    stop = int(input("digite 0 se quiser finalizar e 1 se quiser continuar  "))
    if stop == 0:
        break
    os.system("cls")
    vet.sort()
    print(vet)
os.system('cls')
vet.sort()
print(vet)
