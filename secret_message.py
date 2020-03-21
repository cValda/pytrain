#secret message - replaces every letter with its corresponding letter in a backwards version of the alphabet

import string

sentence = str(input("Enter a sentence (letters only): ")).casefold()

def code(s):
    lst_sentence = list(s)
    alpha_list = list(string.ascii_lowercase)
    lst_coded = []

    for i in lst_sentence:
        try:
            lst_coded.append(alpha_list[(- alpha_list.index(i)) - 1])
        except ValueError:
            lst_coded.append(i)
    return ''.join(lst_coded)

print(code(sentence))