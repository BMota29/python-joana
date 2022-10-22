# clientes = {
#             '1':{'nome':'Luis', 'sobrenome':'Correia'},
#             '2':{'nome':'João', 'sobrenome':'Moreira'},
#             '3':{'nome':'Maria', 'sobrenome':'Jesus'}
#             }
# print (clientes)
# for clientes_chave, clientes_valor in clientes.items():
#     print (f'Dados do {clientes_chave}º cliente:')
#     for dados_chave, dados_valor in clientes_valor.items():
#         print(f'\t {dados_chave} = {dados_valor}')

# clientes = {}
# numero_clientes = int (input('Quantos clientes vai inserir:'))
# for numero in range(1,numero_clientes+1):
#     clientes[numero]={}
#     nome_escolhido = input(f'Nome do {numero}º cliente:').capitalize()
#     clientes[numero]['Nome'] = nome_escolhido
#     clientes[numero]['Sobrenome'] = input(f'Sobrenome do {nome_escolhido} cliente:').capitalize()
# print (clientes)
# for clientes_chave, clientes_valor in clientes.items():
#     print (f'Dados do {clientes_chave}º cliente:')
#     for dados_chave, dados_valor in clientes_valor.items():
#         print(f'\t {dados_chave} = {dados_valor}')

import numbers
import string


aluno = { '1' : {'nome' : 'Joana', 'idade' : 29,'inscrito': True},
          '2' : {'nome' : 'Marta', 'idade' : 29,'inscrito': True}}

# chave_a_procurar = input('Qual a chave a procurar:').capitalize()
# if (chave_a_procurar in aluno)==True:
#     print (f'A chave {chave_a_procurar} existe e tem valor {aluno.get(chave_a_procurar)}')
# else:
#     print (f'A chave {chave_a_procurar} não existe')

# if aluno.get(chave_a_procurar) is not None:
#      print (f'A chave {chave_a_procurar} existe e tem valor {aluno.get(chave_a_procurar)}')
# else:
#     print (f'A chave {chave_a_procurar} não existe')   

# valor_procurar = input('Qual o valor a procurar:')
# if valor_procurar in aluno.values():
#     for chave, valor in aluno.items():
#         if valor==valor_procurar:
#             print (f'O valor a procurar "{valor_procurar}" existe e tem a chave {chave}')
#         else : 
#             print (f'A chave {valor} não existe') 

#print (len (aluno)) #nr de chaves

#aluno ['1']['peso'] = 61
#aluno ['2']['peso'] = 71
#print (len (aluno)) #

#print (aluno)

def print_aluno(peso: string, field: string, value: numbers):
    aluno[peso][field] = value


print_aluno('1', 'peso', 67)
print_aluno('2', 'peso', 71)

print(aluno)