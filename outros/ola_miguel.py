#!/usr/bin/env python3

print("Qual o seu nome?")

nome_da_pessoa = input()
nome_da_pessoa = nome_da_pessoa.lower().strip()

if nome_da_pessoa == "miguel":
    print("Olá %s. Você é muito bonito!" % nome_da_pessoa)

elif nome_da_pessoa == "papai":
    print("Olá %s. Você é muito fortão!" % nome_da_pessoa)

elif nome_da_pessoa == "clara":
    print("Olá %s. Você é muito cagona!" % nome_da_pessoa)

elif nome_da_pessoa == "rubia" or nome_da_pessoa == "mamae":
    print("Olá %s. Você é muito cagona!" % nome_da_pessoa)

elif nome_da_pessoa == "bruna":
    print("Olá %s. Você é muito doida!" % nome_da_pessoa)    

else:
    print("Olá %s. Não te conheço" % nome_da_pessoa)    