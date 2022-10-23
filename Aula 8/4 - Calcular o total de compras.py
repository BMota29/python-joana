# Crie um programa que contenha uma série de compras:
# leite : quantidade 2, preco 0.70,
# pao : quantidade: 5, preco: 0.2,
# carne: quantidade: 2, preco: 5,
# peixe: quantidade: 1, preco: 9,
# macas: quantidade: 5, preco: 1.15,
# laranjas: quantidade: 4, preco: 1.1,
# bananas: quantidade: 5, preco: 1.29
# No final o programa deve imprimir o total de produtos comprados e a fatura das compras (quantidade * preco)

shop_list ={'leite': [2,  0.70],
            'pao': [5, 0.2],
            'carne': [2, 5],
            'peixe': [1, 9],
            'peras': [5, 1.15],
            'laranjas': [4, 1.1],
            'bananas': [5, 1.29]
            }


total_qtd = 0
total_value = 0.0

for item in shop_list:
    item_qtd = shop_list[item][0]
    item_value = shop_list[item][0] * shop_list[item][1]
    print(f'Foi comprado {item_qtd} {item}, sendo o total {item_value}€')
    total_qtd = total_qtd + item_qtd
    total_value = total_value + item_value

print(f'No total foram comprados {total_qtd} produtos, sendo o total da compra {total_value}€')

