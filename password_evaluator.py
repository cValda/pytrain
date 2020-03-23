#password evaluator - decides if a given passwords meets security criteria

password = str(input("Enter password: "))

def pass_check(p):

    #minimum length of password
    length = 7

    #acceptable special characters
    special = ['!', '@', '#', '$', '%', '&', '*']

    #minimum number of special characters
    min_special = 2

    #minimum number of digits
    min_digits = 2

    #pass message
    ok = 'Strong'

    #fail message
    fail = 'Weak'

    if len(p) < length:
        return fail
    else:
        chars = list(p)
        dig = 0
        for i in chars:
            if i.isdigit():
                dig += 1
        if dig < min_digits:
            return fail
        else:
            spec = 0
            for i in chars:
                if i in special:
                    spec += 1
            if spec < min_special:
                return fail
            else:
                return ok

print(pass_check(password))