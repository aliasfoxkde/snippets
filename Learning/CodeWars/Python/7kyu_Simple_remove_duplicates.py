# See: https://www.codewars.com/kata/5ba38ba180824a86850000f7

'''
# Long version:
def solve(l, i=[]):
    for x in l[::-1]:
        i=[x]*(x not in i)+i
    return i
	'''

# Compact version
def solve(l): 
    return sorted(set(l), key=l[::-1].index)[::-1]
