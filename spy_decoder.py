#a short code that removes any non-alphabetical symbols from a string and reverses it

code = str(input())
lst_code = list(code)
alpha = [i for i in lst_code if i.isalpha() or i == ' ']
alpha.reverse()
print(''.join(alpha))