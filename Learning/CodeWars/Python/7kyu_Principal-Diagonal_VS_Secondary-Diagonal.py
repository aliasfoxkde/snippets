# See: https://www.codewars.com/kata/5a8c1b06fd5777d4c00000dd

'''
# Long Version
def diagonal(matrix):
    x, y, c = 0, 0, len(matrix)
    for i in range(c):
        x += matrix[i][i]
        y += matrix[c-i-1][i]

    if x == y:
        return "Draw!"
    elif x < y:
        return "Secondary Diagonal win!"
    return "Principal Diagonal win!"

'''

'''
# Clever 'unpacked' version
def diagonal(m):
    a,b = zip(*[(m[i][-i-1], m[i][i]) for i in range(len(m))])
    return [["Principal","Secondary"][sum(a)>sum(b)]+" Diagonal win!","Draw!"][sum(a)==sum(b)]
    '''

# Compact version
def diagonal(m):
    t = sum([(m[i][-i-1]-m[i][i]) for i in range(len(m))])
    return [["Principal","Secondary"][t>0]+" Diagonal win!","Draw!"][t==0]
