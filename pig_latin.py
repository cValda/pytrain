#translates a sentence in english to pig latin
#pig latin moves first letter of a word to the end and then adds "ay", eg. road -> oadray
#currently only supports words with no special symbols or capitalization (maybe later)

english = str(input())
english_lst = english.split()

def latinize(word):
    letters = list(word)
    letters.append(letters[0])
    letters.remove(letters[0])
    letters.append('ay')
    latin = ''.join(letters)
    return (latin)

latin_lst = list(map(latinize, english_lst))
pig_latin = ' '.join(latin_lst)
print(pig_latin)