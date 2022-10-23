# Imagine que queria traduzir uma palavra em código morse.
# Faça um programa que leia a palavra a traduzir e que no final imprima a palavra em morse.

morse ={'A' : '.-', 
        'B' : '-...', 
        'C' : '-.-.', 
        'D' : '-..', 
        'E' : '.', 
        'F' : '..-.', 
        'G' : '--.', 
        'H' : '....', 
        'I' : '..', 
        'J' : '.---', 
        'K' : '-.-', 
        'L' : '.-..', 
        'M' : '--', 
        'N' : '-.', 
        'O' : '---', 
        'P' : '.--.', 
        'Q' : '--.-', 
        'R' : '.-.', 
        'S' : '...', 
        'T' : '-', 
        'U' : '..-', 
        'V' : '...-', 
        'W' : '.--', 
        'X' : '-..-', 
        'Y' : '-.--', 
        'Z' : '--..'}

palavra = input('Qual a palavra?:').upper()
tupla = tuple(palavra)
traduz = ''
for letra in tupla:
    traduz = traduz + ' ' + morse.get(letra)

print (f'A palavra {palavra} em morse fica: {traduz}')
