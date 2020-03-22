#a function that translates the retarded time format (10:00 AM, 2:30 PM) to normal 24 hour time
#errors due to incorrect input are not accounted for yet

regular_time = input()

def correct_time(t):
    regular_list = list(t)
    if 'AM' in t:
        trimmed = [i for i in regular_list if i.isdigit() or i == ':']
        joined = ''.join(trimmed)
        if joined.startswith('0:') or joined.startswith ('1:') or joined.startswith ('2:') or joined.startswith ('3:') or joined.startswith ('4:') or joined.startswith ('5:') or joined.startswith ('6:') or joined.startswith ('7:') or joined.startswith ('8:') or joined.startswith ('9:'):
            fixed = '0' + joined
            return fixed
        else:
            return joined
    else:
        trimmed = t.replace(' PM', '')
        parted = trimmed.split(':')
        parted[0] = str(int(parted[0]) + 12)
        joined = ':'.join(parted)
        return joined

print(correct_time(regular_time))