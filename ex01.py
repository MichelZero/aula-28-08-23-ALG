#
#
# autores: Cristiano e Michel
# data: 28/08/2023

# 1. Ler uma lista de 4 notas e em seguida mostra as notas e a média. 

# entrada de dados
lista = []

for i in range(4):
  valor = int(input(f"informe o valor[{i}]: "))
  lista.append(valor)

# processamento
media = sum(lista)/len(lista)

# saída
print(f"a média da lista é: {media}")
print(f"lista = {lista}")