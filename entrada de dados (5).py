aluno: str
n1: int
n2: int
n3: int

aluno = input("Digite o nome do aluno ")
n1 = (int(input("Nota do primeiro bimestre ")))
n2 = (int(input("Nota do segundo bimestre ")))
n3 = (int(input("Nota do terceiro bimestre ")))

print(f"{aluno}, tem a media de {n1+n2+n3//3}")
