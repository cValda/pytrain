#a convertor to convert us date format to eu date format, MM/DD/YYYY to DD/MM/YYYY
#supports: 11/19/2019 + November 19, 2019 + Nov 19, 2019

us_date = input()

def conv_date(dat):
    if '/' in us_date:
        split = us_date.split('/')
        d = split[1]
        m = split[0]
        split[0] = d
        split[1] = m
        eu_date = '/'.join(split)
    else:
        trimmed = us_date.replace(',', '')
        split = trimmed.split(' ')
        d = split[1]
        m = split[0]
        if 'Jan' in m:
            m = '1'
        elif 'Feb' in m:
            m = '2'
        elif 'Mar' in m:
            m = '3'
        elif 'Apr' in m:
            m = '4'
        elif 'May' in m:
            m = '5'
        elif 'Jun' in m:
            m = '6'
        elif 'Jul' in m:
            m = '7'
        elif 'Aug' in m:
            m = '8'
        elif 'Sep' in m:
            m = '9'
        elif 'Oct' in m:
            m = '10'
        elif 'Nov' in m:
            m = '11'
        elif 'Dec' in m:
            m = '12'
        split[0] = d
        split[1] = m
        eu_date = '/'.join(split)
    return eu_date

print(conv_date(us_date))