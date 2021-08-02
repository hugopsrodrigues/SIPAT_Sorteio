import random

file = open('nomes.txt')

text = file.read().rsplit('class="name"') # </div></div><div class="info">

lista = []

for word in text:
    if word.__contains__('</div></div><div class="info">'):
        trecho = word[1:word.index('</div></div><div class="info">')]
        lista.append(trecho)

lista_sorted = sorted(lista)

with open('ListaDePresenca-2021-08-03.txt', 'w', encoding='utf-8') as arq:
    for i in lista_sorted:
        arq.write(i + '\n')
    arq.close()