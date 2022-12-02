rue: float = 1.50
cassio: float = 1.10
anos = 0

print(f"Inicio, Rue {rue}, Cassio {cassio}")

while (cassio < rue):
    rue += 0.2
    cassio += 0.3
    anos += 1


print(f"Tempo: {anos} anos, Rue {rue}, Cassio {cassio}")
