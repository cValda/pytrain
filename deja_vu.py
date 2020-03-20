#takes a string of characters as input and returns 'Deja Vu' if there are duplicit characters
#returns 'Unique' if there are no duplicit characters

rnd_letters = str(input())
lst_letters = list(rnd_letters)

for i in lst_letters:
    count = lst_letters.count(i)
    if count > 1:
        x = 0
        print('Deja Vu')
        break
    else:
        x = 1
        continue

if x == 1:
    print('Unique') 