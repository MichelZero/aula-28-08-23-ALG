#
#
# autores: Cristiano e Michel
# data: 28/08/2023

# 3.	Em linguagem Python, faça um programa que leia um conjunto de 10 
# números inteiros, armazenando-o em uma lista (L1), calcular o 
# quadrado dos elementos dessa lista, armazenando o resultado em outra lista (L2), 
# imprimir todas as listas.

l1 = []
l2 = []

for i in range(10):
  valor = int(input(f"informe o valor[{i}]: "))
  l1.append(valor)
  l2.append(valor ** 2) # ** eleva ao quadrado
  
# saída
print(f"lista L1= {l1}")
print(f"lista L2= {l2}")