# aluno = {
#     'nome' : 'Joana',
#     'idade' : 29,
#     'inscrito' : True
# }

# print (aluno)
# print (aluno ['nome'])
# print (aluno ['ano'])
# print (aluno ['inscrito']) 
# print (aluno.get('nome'))
# print (aluno.get('ano'))

from asyncio import constants


dic = {
    '1' : 'Um',
    '2' : 'Dois',
    '3' : 'Três',
    '4' : 'Quatro', 
    '5' : 'Cinco',
    '6' : 'Seis', 
    '7' : 'Sete',
    '8' : 'Oito',
    '9' : 'Nove',
    '0' : 'Zero'
}

# lista = []
# tamanho = int(input('Quanto elementos serão lidos?:'))
# n = 1
# while n < tamanho + 1 :
#     elemento = input(f'Entre {n}º elemento:')
#     lista.append(elemento) 
#     n = n + 1
# print (lista)

# lista_extenso = []
# m = 1
# while m < tamanho + 1 :
#     elemento_base = lista [m-1]
#     elemento = numero.get(elemento_base)
#     lista_extenso.append(elemento) 
#     m = m + 1

# print (lista_extenso)


# tamanho = int(input('Quanto elementos serão lidos?:'))

# lista_extenso = []
# m = 1
# frase=''
# while m < tamanho + 1 :
#     elemento = input(f'Entre {m}º elemento:')
#     elemento_base = numero.get(elemento)
#     frase = frase + ' ' + elemento_base
#     m = m + 1

# print (frase)

# numero = (input('Introduza um numero:'))

# frase=''
# for digito in numero :
#     elemento_base = dic.get((digito))
#     frase = frase + ' ' + elemento_base

# # print (frase)
# lista0 = ['frutas', 'morango, maça, banana, abacaxi']
# lista1 =['legumes','couve, agrião']
# lista2 = ['doces', 'bolo-rei, pão-de-ló']
# listas = [lista0, lista1, lista2]
# compras = dict(listas)
# escolha = input('Quer ver as frutas, legumes ou doces?:')
# print(compras.get(escolha, f'Não existe {escolha} na lista'))

# constantes = dict(pi=3.14, e=2.7, iva=0.23)
# print(constantes)

# clubes =    {'FCP': 'Futebol Clube do Porto',
#              'SLB': 'Sport Lisboa e Benfica',
#              'SCP': 'Sporting Clube de Portugal' }

# x = clubes ['SLB']
# print (x)
# print (clubes['SLB'])
# print (clubes)
# escolha = input ('introduza o clube que quer ver:').upper()
# print (clubes.get(escolha,f'Não existe "{escolha} na lista'))

# #print (clubes.get(escolha,clubes.get('SLB')))

# clubes = {'FCP': 'Porto', 'SLB': 'Benfica', 'SCP': 'Sporting'}
# escolha = input('Escolha o clube:').upper()
# print (clubes.get(escolha, f'xxxxx"{escolha}"kkkkk'))


# clubes = {'FCP' : 'Porto','SLB' : 'Benfica','SCP' : 'Sporting'}
# # x = clubes ['SLB']
# # print(x)
# # print(clubes['SLB'])

# # escolha = input('Escolha o clube: ').upper()
# # print (clubes.get(escolha, f'Não existe o "{escolha}" na lista'))

# print ('As chaves do dicionario são:')
# for chaves in clubes: #.keys
#     print (f'->{chaves}')

# print ('Os valores do dicionario são:')
# for chaves in clubes.values():
#     print (f'->{chaves}')

# print ('As chaves e os valores do dicionario são:')
# for chaves in clubes.items():
#     print (f'->{chaves}')
# #o output é um tupla 

# for chaves, valores in clubes.items():
#     print (f'->{chaves} - {valores}')

numeros_por_extenso = {}
numeros = int(input('Quantos numeros vai introduzir: '))
for numero in range(numeros):
    chave = input('Chave: ')
    valor = input ('Valor: ')
    numeros_por_extenso[chave] = valor
print(numeros_por_extenso)
print('As chaves e os valores do dicionario sao:')
for chave, valor in numeros_por_extenso.items():
    print(f'-> {chave} - {valor} ')
    
