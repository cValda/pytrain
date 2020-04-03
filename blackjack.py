from random import randrange

print('Vítejte ve hře Black Jack pro dva hráče. Cílem hry je mít více bodů, než soupeř.')
print('Každé kolo máte možnost si "líznout" kartu s náhodnou hodnotou 2-10.')
print('Kdo překročí 21 bodů, prohrává.')
print()

player1 = input('Jak se jmenuje první hráč? ')
player2 = input('Jak se jmenuje druhý hráč? ')
body1 = 0
body2 = 0

print('\n' + player1 + ' vs ' + player2)

while True:
    chce1 = input('Chce si ' + player1 + ' líznout kartu? (ano/ne) ')
    chce2 = input('Chce si ' + player2 + ' líznout kartu? (ano/ne) ')
    print()

# Chtějí lízat oba
    if chce1.casefold() == 'ano' and chce2.casefold() == 'ano':
        karta = randrange(2, 11)
        body1 = body1 + karta
        print(player1 + ' má ' + str(body1) + ' bodů.')

        karta = randrange(2, 11)
        body2 = body2 + karta
        print(player2 + ' má ' + str(body2) + ' bodů.')

# Chce lízat jen hráč 1
    if chce1.casefold() == 'ano' and chce2.casefold() != 'ano':
        print(player2 + ' končí na ' + str(body2) + ' bodech.')

        karta = randrange(2, 11)
        body1 = body1 + karta
        print(player1 + ' má ' + str(body1) + ' bodů.')
        if body1 > 21:
            break

        while True:
            chce1 = input('Chce si ' + player1 + ' líznout kartu? (ano/ne) ')
            print()
            if chce1.casefold() == 'ano':
                karta = randrange(2, 11)
                body1 = body1 + karta
                print(player1 + ' má ' + str(body1) + ' bodů.')
            else:
                break
            if body1 > 21:
                break

# Chce lízat jen hráč 2
    if chce1.casefold() != 'ano' and chce2.casefold() == 'ano':
        print(player1 + ' končí na ' + str(body1) + ' bodech.')

        karta = randrange(2, 11)
        body2 = body2 + karta
        print(player2 + ' má ' + str(body2) + ' bodů.')
        if body2 > 21:
            break

        while True:
            chce2 = input('Chce si ' + player2 + ' líznout kartu? (ano/ne) ')
            print()
            if chce2.casefold() == 'ano':
                karta = randrange(2, 11)
                body2 = body2 + karta
                print(player2 + ' má ' + str(body2) + ' bodů.')
            else:
                break
            if body2 > 21:
                break

# Nechce lízat nikdo
    if chce1.casefold() != 'ano' and chce2.casefold() != 'ano':
        break

    if body1 > 21:
        break

    if body2 > 21:
        break

print('\n' + 'Konečný výsledek je:' + '\n' + player1 + ': ' + str(body1) + ' bodů' + '\n' + player2 + ': ' + str(body2) + ' bodů' )
vitez = max(body1, body2)
print()
if body1 > 21 and body2 > 21:
    print('Je to nerozhodně!')
if body1 > 21 and body2 < 22:
    print('Vítězem je ' + player2)
if body1 < 22 and body2 > 21:
    print('Vítězem je ' + player1)
if body1 == body2:
    print('Je to nerozhodně!')
elif body1 < 22 and body2 < 22:
    if vitez == body1:
        print('Vítězem je ' + player1 + '!')
    else:
        print('Vítězem je ' + player2 + '!')
print()

input('Ukončete stisknutím Enter.')