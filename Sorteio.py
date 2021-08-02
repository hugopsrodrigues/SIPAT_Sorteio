import datetime
import random
from time import sleep
import emoji

date = datetime.date
print('=-=' * 9)
print('SORTEIO SIPAT - ' + str(date.today()) + "!" + 5 * emoji.emojize(':trophy:', use_aliases=True))
print('=-=' * 9)
controle = bool(1)
opcoes = [1,2]

file = open('ListaDePresenca-2021-08-02.txt')
lista = file.readlines()

while(controle):
    print('Selecione uma opção:\n 1 - Sortear\n 2 - Passar a lista\n')
    print('R: ', end='')
    num = int(input())

    while(num not in opcoes):
        print('Opção inválida, tente novamente...')
        sleep(2)
        print('\n\n')
        break
    if num == 1:
        resultado = random.choice(lista)
        print('Sorteando...')
        for j in range (0,5,1):
            print(emoji.emojize(':hourglass_flowing_sand:', use_aliases=True), end=' ')
            sleep(1)
            print(emoji.emojize(':hourglass:', use_aliases=True), end=' ')
            sleep(1)
        print('\n\n')
        print('Lá vai... ' + emoji.emojize(':laughing:', use_aliases=True))
        print('\n\n')
        print('O ganhador(a) é ' + resultado + 'CONGRATS!!! ' + 5 * emoji.emojize(':clap:', use_aliases=True))
        print('\n\n')
        break
    if num == 2:
        for i in lista:
            print(i)
            sleep(0.3)
        print('===== Lista finalizada =====')
print('Sorteio encerrado!')
