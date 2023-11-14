import time
idade = int(input('Qual a idade do seu filho?'))
if idade < 5:
    print('Ele já devia ter tomado as dose da vacinação')
elif idade == 5:
    print('Ele pode tomar as doses dele.')
else:
    print('Ele já não pode mais tomar as doses da vacina.')    