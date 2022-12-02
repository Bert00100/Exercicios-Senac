cliente = input("Digite o nome do cliente ")
livros = int(input("Digite quantos livros o cliente retirou "))

if livros == 0:
    print(f"os {livros} livros, da 0 pontos para {cliente} ")
elif livros > 0 and livros <= 1:
    print(f"os {livros} livros, da 5 pontos para {cliente}  ")
elif livros > 1 and livros <= 2:
    print(f"os {livros} livros, da 15 pontos para {cliente}  ")
elif livros > 2 and livros <= 3:
    print(f"os {livros} livros, da 30 pontos para {cliente}  ")
elif livros > 3:
    print(f"os {livros} livros, da 60 pontos para {cliente}  ")
