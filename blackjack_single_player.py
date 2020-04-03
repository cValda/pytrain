from random import randrange

print('Vítej ve hře Black Jack pro jednoho hráče. Cílem hry je mít více bodů, než krupiér.')
print('Každé kolo máš možnost si "líznout" kartu s náhodnou hodnotou 2-10. Následně hraje krupiér.')
print('Pokud překročíš 21 bodů, prohráváš.')
print()

body = 0
krupier = 0

print('Hra proti krupiérovi.')
print()

while True:
    chce = input('Chceš si líznout kartu? (ano/ne) ')

    # Líže hráč i krupiér
    if chce.casefold() == 'ano' and krupier < 17:
        karta = randrange(2, 11)
        body = body + karta
        print('Máš ' + str(body) + ' bodů.')

        karta = randrange(2, 11)
        krupier = krupier + karta
        print('Krupiér má ' + str(krupier) + ' bodů.')

        print()

    # Líže jen hráč
    if chce.casefold() == 'ano' and krupier > 16:
        print('Krupiér končí na ' + str(krupier) + ' bodech.')
        print('Máš ' + str(body) + ' bodů.')
        
        while True:
            chce = input('Chceš si líznout kartu? (ano/ne) ')
            if chce.casefold() == 'ano':
                karta = randrange(2, 11)
                body = body + karta
                print('Máš ' + str(body) + ' bodů.')
            else:
                break
            if body > 21:
                break

    # Líže jen krupiér
    if chce.casefold() != 'ano' and krupier < 17:
        karta = randrange(2, 11)
        krupier = krupier + karta
        print('Končíš na ' + str(body) + ' bodech.')
        print('Krupiér má ' + str(krupier) + ' bodů.')

        while True:
            input('Pokračuj stisknutím Enter.')
            karta = randrange(2, 11)
            krupier = krupier + karta
            print('Krupiér má ' + str(krupier) + ' bodů.')
            if krupier > 16:
                break

    # Nelíže nikdo
    if chce.casefold() != 'ano' and krupier > 16:
        break

    if body > 21:
        break
    if krupier > 21:
        break

print('\n' + 'Konečný výsledek je:' + '\n' 'Ty: ' + str(body) + ' bodů' + '\n' 'Krupiér: ' + str(krupier) + ' bodů' )
vitez = max(body, krupier)
print()
if body > 21 and krupier > 21:
    print('Je to nerozhodně!')
if body > 21 and krupier < 22:
    print('Prohrál jsi!')
if body < 22 and krupier > 21:
    print('Vyhrál jsi!')
if body == krupier:
    print('Je to nerozhodně!')
elif body < 22 and krupier < 22:
    if vitez == body:
        print('Vyhrál jsi!')
    else:
        print('Prohrál jsi!')
print()

input('Ukončete stisknutím libovolné klávesy.')