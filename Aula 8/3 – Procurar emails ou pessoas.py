# Crie um dicionário com alguns nomes e respetivos emails, como por exemplo:
# Joao : joao@gmail.com,
# Joana : joana@gmail.com,
# Pedro : pedro@gmail.com
# O programa deve mostrar um menu onde o utilizador pode procurar o nome da pessoa e devolver o email e vice versa (deve ser acautelado o case sensitive).
# Faça a verificação da opção do menu e do nome/email e em caso de não existir dê uma mensagem de erro.

info_base = {   'João' : 'joao@gmail.com',
                'Joana' : 'joana@gmail.com',
                'Pedro' : 'pedro@gmail.com'}

print('========= Procurar emails ou pessoas =========')
print('[0] Digite o nome da pessoa:')
print('[1] Digite o email da pessoa:')
opcao = input('Digite a opção que quer: ')

if opcao == '0':
    nome = input('Digite o nome da pessoa: ').capitalize()
    if nome in info_base.keys():
        print(f'O email de {nome} é {info_base.get(nome)}')
    else:
        print(f'O {nome} não consta a lista de Pessoas')
elif opcao == '1':
    email = input('Digite o email da pessoa: ').lower()
    if email in info_base.values():
        for nome_base, email_base in info_base.items():
            if email_base == email:
                print(f'O nome de {email} é {nome_base}')
    else:
        print(f'O {email} não consta a lista de emails')
else: 
    print('Opção invalida')



