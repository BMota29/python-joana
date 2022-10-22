# aluno = {'nome': 'joao',
#          'idade': 17,
#          'inscrito': True}

#chave_a_apagar = input ('Qual a chave a apagar: ')

# O pop imprime a chave a apagar 

#apagado = aluno.pop(chave_a_apagar) - é uma variavel
#retorna o valor que foi retirado 

# print(aluno.pop(chave_a_apagar, f'Não existe a chave {chave_a_apagar}'))
# print(aluno)

#del aluno [chave_a_apagar]
#o metodo del não funciona se a chave não existir no dicionario 

#para contornar o problema do del não funcionar com chave inexistentes

# chave_a_apagar = input('Qual a chave a apagar:')
# if (chave_a_apagar in aluno) == True:
#     print(f'Foi apagada a chave {chave_a_apagar} com o valor', aluno.get(chave_a_apagar), "!")
#     del aluno [chave_a_apagar]
# else:
#     print(f'A chave {chave_a_apagar} não existe.')
# print('Dicionario:', aluno) 

# #popitem remove sempre o ultimo do dicionario, caso o dicionario esteja vazio devolve um erro 
# print (aluno.popitem())
# print(aluno)
# print (aluno.popitem())
# print(aluno)
# print (aluno.popitem())
# print(aluno)
# print (aluno.popitem())
# print(aluno)        
# #KeyError: 'popitem(): dictionary is empty'

# print('Dicionario:', aluno) 

# #aluno['nome'] = 'Joana'
# aluno.update({'nome': 'Joaquim'})
# print('Dicionario:', aluno) 

# aluno_velho = {
#     'nome': 'joana',
#     'idade': 17,
#     'inscrito': True,
#     'ano': 1993
#     }
# print('Aluno velho: ', aluno_velho) # {'nome': 'joana', 'idade': 17, 'inscrito': True}
# aluno_novo = {
#     'nome': 'joão',
#     'idade': 15,
#     'inscrito': False,
#     'sexo': 'M'
#     }
# aluno_velho.update(aluno_novo)
# print('Aluno novo: ',aluno_novo) # {'nome': 'joão', 'idade': 15, 'inscrito': False}
# print('Aluno velho depois do update do novo: ',aluno_velho) 

# # {'nome': 'joão', 'idade': 15, 'inscrito': False}

velho = {
    'a': 1,
    'b': 2
    }
print('velho: ',velho) # {'a': 1, 'b': 2}
novo = {
    'c': 5
    }
print('novo: ',novo)
velho.update(novo)
print('velho depois do update: ', velho) # {'a': 1, 'b': 2, 'c': 5}
print('novo: ', novo) #  {'c': 5}