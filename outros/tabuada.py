#!/usr/bin/env python3

# 1 - Perguntar se é multiplicação ou divisão
print('Qual a operação da tabuada?')
print(' [M] - Multiplicação')
print(' [D] - Divisão')
operacao = input()
if operacao.upper() not in ['M', 'D']:
    raise Exception('Operação inválida')

# 2 - Qual número da tabuada
print('Qual o número da tabuada?')
numero = input()

# 3 - Imprimir os valores da tabuada e perguntar a resposta
for i in range(1, 10):
    op = 'X' if operacao.upper() == 'M' else '%'
    print('{} {} {} = '.format(numero, op, i), end='')
    resposta = int(input())
    if resposta == (i * numero):
        print('V')
    else: 
        print('X')