#!/usr/bin/env python3

nota = 0

print("1) Quem foi o primeiro astronauta a ir para o espaço?")
print("   [a] Neil Armstrong")
print("   [b] Gherman Titov")
print("   [c] Yuri Gagarin")
print("   [d] Alan Shepard")
resposta = input('Resposta: ')
if resposta == 'c':
    print('Bingo!')
    nota = nota + 1
else:
    print('Burro! A resposta correta é [a]')

print("\n")

print("2) Quem foi o primeiro astronauta a pisar na lua?")
print("   [a] Buzz Aldrin")
print("   [b] Yuri Gagarin")
print("   [c] Alan Shepard")
print("   [d] Neil Armstrong")
resposta = input('Resposta: ')
if resposta == 'd':
    nota = nota + 1
    print('Bingo!')
else:
    print('Burro! A resposta correta é [d]')


print("\n")

print("3) Qual foi o 1 animal qui foi pro espaço?")
print("   [a] Gato Felix")
print("   [b] Cadela Laika")
print("   [c] Macacos Ham e Enos")
print("   [d] Peixe Mummichog")
resposta = input('Resposta: ')
if resposta == 'b':
    print('Bingo!')
    nota = nota + 1    
else:
    print('Burro! A resposta correta é [b]')


print("\n")


print("4) Qual o ano em que o primeiro astronauta foi para o espaço?")
print("   [a] 1959")
print("   [b] 1960")
print("   [c] 1961")
print("   [d] 1962")
resposta = input('Resposta: ')
if resposta == 'c':
    print('Bingo!')
    nota = nota + 1    
else:
    print('Burro! A resposta correta é [c]')


print("\n")


print("5) Qual o foguete usado na missão do primeiro pouso na lua?")
print("   [a] Apollo 1")
print("   [b] Saturno V")
print("   [c] Houston 5")
print("   [d] Apollo 11")
resposta = input('Resposta: ')
if resposta == 'b':
    print('Bingo!')
    nota = nota + 1    
else:
    print('Burro! A resposta correta é [b]')


print("\n")
print("\n")

print("SUA NOTA FINAL DA PROVA FOI: %s/5" % nota)
print("FIM")


