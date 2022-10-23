# Crie um dicionário que guarde a distância de Lisboa a algumas cidades, por exemplo:
# Porto: 315
# Faro: 250
# Coimbra: 197
# Braga: 360
# Evora: 135
# O programa deve pedir a cidade de destino e imprimir a respetiva distância. 
# Caso não exista a cidade destino deve perguntar ao utilizador se quer adicionar a distância. 
# Em caso afirmativo deve inserir e, no final, mostrar o dicionário para verificar se a cidade foi inserida corretamente.

print ('Este programa fornece a distância de Lisboa às principais cidades')
cidades = { 'Porto': 315,
            'Faro': 250,
            'Coimbra': 197,
            'Braga': 360,
            'Evora': 135}
destino = input('Qual a cidade destino:').capitalize()

if destino in cidades:
    print(f'A distância de Lisboa a {destino} são {cidades.get(destino)} km')
else:
    resposta = input(f'A distância à cidade {destino} não se encontra disponivel. Pretende adiciona-la? [S/N]').upper()
    if resposta == 'S':
        distancia = input(f'Qual a distância de Lisboa a {destino}, em km?')
        if distancia.isnumeric():
            cidades[destino]= distancia
            for cidade, km in cidades.items():
                print(cidade, km, 'km')
        else:
           print('Distância não válida. Tente mais tarde!') 
    else:
        print('Até à próxima!')



