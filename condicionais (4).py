a = float(input("Escreva um numero: "))
b = float(input("Escreva um numero: "))
c = float(input("Escreva um numero: "))

if a >= b and b >= c and c < b:
    print(f"A ordem decrescente é {a}, {b}, {c}")
elif a >= b and c >= c and b <= c:
    print(f"A ordem decrescente é {a}, {c}, {b}")
elif b >= a and c >= b and c >= a:
    print(f"A ordem decrescente é {c}, {b}, {a}")
elif b > a and c < b and a > b:
    print(f"A ordem decrescente é {b}, {a}, {c}")
elif b > c and c > a:
    print(f"A ordem decresente é {b}, {c}, {a}")
