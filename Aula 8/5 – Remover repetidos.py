# Escreva um programa que, dado um conjunto de informações (nome, NIF e idade) de n pessoas, a definir pelo utilizador, remova as chaves repetidas (utilize a chave NIF).
# No fim, o programa deve imprimir a lista de pessoas sem repetições.
# Mantenha sempre a 1ª chave do registo da pessoa repetida como referência.

info_base ={}

n = 1

number_p = int(input('Quantas pessoas pretente introduzir?'))

while n <= number_p:
    info_p =[]
    name_p = input('Qual o nome?').capitalize()
    nif_p = input('Qual o numero de contribuinte?')
    age_p = input('Qual é a idade?')
    if nif_p not in info_base:
        info_p=[name_p, age_p]
        info_base[nif_p]=info_p
        n=n+1
    else:
        n=n+1

print(info_base)

for nif in info_base:
    print(f'Nome: {info_base[nif][0]} - Nif {nif} e idade {info_base[nif][1]}')
    
