# See: https://www.codewars.com/kata/5886d65e427c27afeb0000c1

'''
# Long version
def square_digits_sequence(n):
    l = []
    while n not in l[1:]:
        next = sum(i**2 for i in map(int, str(n)))
        if next in l or n==1:
            return len(l)+2
        else:
            l.append(n)
            n = next
    return len(l)
    '''

# Compact version  
def square_digits_sequence(n):
    seq = [0]
    while n not in seq:
        seq.append(n)
        n = sum(int(i)**2 for i in str(n))
    return len(seq)
