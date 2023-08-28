#
#
# autores: Cristiano e Michel
# data: 28/08/2023


alunos = (("João", 8.5), ("Maria", 9.2), ("José", 7.1), ("Ana", 8.7), ("Carlos", 6.5))

# Encontra o aluno com a maior nota
maior_nota = float('-inf') # -infinito (menor valor possível) para que qualquer nota seja 
#                             maior que ele na primeira iteração
nome_maior_nota = ""
for nome, nota in alunos:
    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome

# Encontra o aluno com a menor nota
menor_nota = float('inf') # +infinito (maior valor possível) para que qualquer nota seja 
#                            menor que ele na primeira iteração
nome_menor_nota = ""
for nome, nota in alunos:
    if nota < menor_nota:
        menor_nota = nota
        nome_menor_nota = nome

# Imprime os resultados
print(f"Aluno com a maior nota: {nome_maior_nota} (Nota: {maior_nota})")
print(f"Aluno com a menor nota: {nome_menor_nota} (Nota: {menor_nota})")
