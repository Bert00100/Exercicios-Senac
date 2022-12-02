m = float(input("Digite seu pesso "))
h = float(input("Digite sua altura "))

if m/h**2 < 14.5:
    print("Desnutrido")
elif m/h**2 >= 14.5 and m/h**2 < 20:
    print("Pesso abaixo do normal")
elif m/h**2 >= 20 and m/h**2 < 25:
    print("Pesso normal ")
elif m/h**2 >= 25 and m/h**2 < 30:
    print("Sobrepeso")
elif m/h**2 >= 30 and m/h**2 < 40:
    print("Obesidade")
elif m/h**2 >= 40:
    print("Obesidade morbida")
