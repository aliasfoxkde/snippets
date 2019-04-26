# See: https://www.codewars.com/kata/592edfda5be407b9640000b2

def decode(c, k):
    return ''.join(chr(i-int(j)+96) for i,j in zip(c,str(k)*len(c)))
