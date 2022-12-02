seg = int(input("Digite os segundos: "))
if seg < 60:
    print(F"{seg} segundos ")
elif seg >= 60 and seg < 3600:
    print(F"{seg/60} minutos ")
elif seg >= 3600 and seg < 86400:
    print(F"{seg/3600} horas ")
elif seg > 3600 and seg >= 86400:
    print(F"{seg/86400} dias")
