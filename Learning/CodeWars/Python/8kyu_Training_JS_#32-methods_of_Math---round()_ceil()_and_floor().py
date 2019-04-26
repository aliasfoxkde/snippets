# See: https://www.codewars.com/kata/5732d3c9791aafb0e4001236

'''
# Long version
def round_it(n):   
    l, r = [len(i) for i in str(n).split('.')]
    
    if l < r:
        return int(n+.9) # ceil
    elif l > r:
        return int(n-.1) # floor
    return round(n,0) # round
    '''

# Compact version  
def round_it(n):
    l, r = map(len, str(n).split('.'))
    return [int(n+1),int(n),int(n+.5)][[l<r,l>r,r==l].index(True)]