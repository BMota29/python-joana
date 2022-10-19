# Dicionários são estruturas mutáveis formadas por um conjunto de chave - valor, onde:
# Chave: É única em cada objeto e serve para mapear o valor: funciona como um apontador.
# Valor: É um dado que pode ser de qualquer tipo: inteiro, lista, texto, real e até outros dicionários.
# Listas e outros dicionários não podem ser usados como chaves
# por serem de tipos mutáveis.
# Não existe início, fim ou ordem num dicionário.
# NOTA: A partir da versão 3.7 do Python, a ordem das chaves no dicionário é garantida
# como sendo a ordem de inserção.

# aluno = {
#     'nome': 'joana',
#     'idade': 17,
#     'inscrito': True
#     }
# print(aluno)
# print(aluno['nome'])
# print(aluno['idade'])
# print(aluno['ano'])
# print(aluno.get('nome')) # da o valor da chave se existe
# print(aluno.get('ano')) # retorna None se nao existir
# print(aluno.get('idade'))
# print(aluno.get('inscrito'))

# aluno['ano'] = 10
# print(aluno.get('ano')) 

# print(aluno.get('ano',9)) # se nao existir retorna 9
# print(aluno.get('ano','O ano não existe')) # se nao existir retorna 'Não existe'


# ************* Exemplos de declaração de um dicionário - Inicio ****************
# xpto = {} # dicionario vazio.
# print(type(xpto)) # <class 'dict'>

# coordenadas = {
    # 'Latitude': 41.189683,
    # 'Longitude': -8.705539
#     }
# print(type(coordenadas)) # <class 'dict'>
# print(coordenadas)

# Podemos também declarar um dicionário de forma explícita usando a função dict().
# dicionario = dict({}) # dicionario vazio.
# print(type(dicionario))

# coordenadas = ({
#     'Latitude': 41.189683,
#     'Longitude': -8.705539
#     })
# print(type(coordenadas)) # <class 'dict'>

# Existem outras formas de usar o dict(), nomeadamente com listas:
# lista0 = ['frutas', 'morango, maça, banana, abacaxi, pera, morango']   
# # print(lista0[0])        
# # print(lista0[1])        
# # print(lista0[2])        
# lista1 = ['legumes', 'couve, agrião']
# lista2 = ['doces', 'bolo-rei, pão-de-ló']
# listas = [lista0,lista1, lista2]
# # # print(type(listas))
# # # print(len(lista1))
# # print(listas)
# compras = dict(listas)
# # # print(type(compras))
# # print(compras)
# escolha = input('Quer ver as frutas, os legumes ou os doces? ')
# print(compras.get(escolha,f'Não existe "{escolha}" na lista de compras!'))

# Atribuindo os valores diretamente:
# constantes = dict(pi=3.14, e=2.7, iva=0.23)
# print(constantes)
# ************* Fim - Exemplos de declaração de um dicionário ****************

# ****** CHAVES *******
# Aceder a um determinado valor do dicionário através da chave:
# clubes = {'FCP': 'Futebol Clube do Porto',
#           'SLB': 'Sport Lisboa e Benfica',
#           'SCP': 'Sporting Clube de Portugal'
#         }
# x = clubes['SLB']
# print(x)
# print(clubes['SCP'])

# escolha = input('Introduza o clube que quer ver: ').upper()
# print(clubes[escolha])
# print(clubes.get(escolha,f'Não existe "{escolha}" na lista de clubes!'))

# Caso nao haja uma chave retornar outro
# escolha = input('Introduza o clube de Lisboa que quer ver: ').upper()
# print(clubes.get(escolha,clubes.get('SLB')))

# print(clubes['FCP'])
# print(clubes['SLB'])
# print(clubes['SCP'])

# **** outra forma de ver as chaves *******
# clubes = {'FCP': 'Futebol Clube do Porto',
#           'SLB': 'Sport Lisboa e Benfica',
#           'SCP': 'Sporting Clube de Portugal'
#         }
# print('As chaves do dicionário são: ')
# for chaves in clubes:
#     print(f'-> {chaves}')

# **** para ver so os valores *******
# print('Os valores do dicionário são: ')
# for valores in clubes.values():
#     print(f'-> {valores}')

# **** para ver as chaves e os valores --> retorna tupla*******
# print('As chaves e os valores do dicionário são: ')
# for items in clubes.items():
#     print(f'-> {items}')

# * outra forma para ver as chaves e os valores, mas sem retornar tuplas *******
# clubes = {'FCP': 'Futebol Clube do Porto',
#           'SLB': 'Sport Lisboa e Benfica',
#           'SCP': 'Sporting Clube de Portugal'
#         }
# print('As chaves e os valores do dicionário são: ')
# for chaves, valores in clubes.items():
#     print(f'-> {chaves} - {valores}')

# Podemos colocar todo tipo de dados nos valores e até mesmo outros dicionários:
# numeros = {'primos': '2, 3, 5', # string
#            'pares': [0, 2, 4], # lista
#            'impares': (1, 3, 5), # tupla
#            'negativos' : { '1': -1, '2':-2} # dicionário
#         }
# print(numeros['primos']) # 2, 3, 5
# print(numeros['pares']) # [0, 2, 4]
# print(numeros['impares']) # [1, 3, 5]
# print(numeros['negativos']) # {'1': -1, '2': -2}
# print(numeros['negativos']['1']) # -1

# Mesmo que os pares chave-valor estejam organizados na ordem que foram colocados,
# não podemos aceder por índices como fazemos em listas, logo a seguinte expressão:
# print(numeros[2]) # dá erro -> KeyError: 2

# Assim como os valores não precisam ser do tipo string, o mesmo vale para as chaves:
# Nota: Listas e outros dicionários não podem ser usados como chaves por serem de tipos mutáveis.
# numeros_por_extenso = {
#                           5: 'cinco',
#                         (2): 'dois',
#                        '1': 'um',
#                     #    {3}: 'três', # TypeError: unhashable type: 'set'
#                     #    [0]: 'zero'
#                     }    # TypeError: unhashable type: 'set'
# print(numeros_por_extenso[5]) # cinco
# print(numeros_por_extenso[2]) # dois
# print(numeros_por_extenso['1']) # um

# ***** inserir dicionario com loop ****
numeros_por_extenso = {}
numeros = int(input ('Quantos numeros vai introduzir: '))
for numero in range(1, numeros+1):    
    chave = input('Introduza a chave: ')
    valor = input('Introduza o valor: ')
    numeros_por_extenso[chave] = valor
print(numeros_por_extenso)
print('As chaves e os valores do dicionário são: ')
for chaves, valores in numeros_por_extenso.items():
    print(f'-> {chaves} - {valores}')