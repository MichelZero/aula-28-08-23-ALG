#
#
# autores: Cristiano e Michel
# data: 28/08/2023

#2.	Ler uma lista de 5 números e imprimir o menor e maior valor.

# entrada de dados
lista = []
maior = float('-inf')
menor = float('inf')

for i in range(4):
  valor = int(input(f"informe o valor[{i}]: "))
  lista.append(valor)
  if valor > maior:
    maior = valor
  elif valor < menor:
    menor = valor
    
# saída
print(f"o maior é: {maior}")
print(f"o menor é: {menor}")

