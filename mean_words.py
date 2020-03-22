#this function calculates the mean number of letters (rounded up) in a given text. Ignores punctuation.

essay = input()

def mean_words(t):
    import math
    chars = list(t)
    depunct = [i for i in chars if i.isalpha() or i == ' ']
    joined = ''.join(depunct)
    split = joined.split(' ')
    a = 0
    b = 0
    for i in split:
        a += len(i)
        b += 1
        mean = math.ceil(a / b)
    return mean

print(mean_words(essay))