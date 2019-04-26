# See: https://www.codewars.com/kata/5bb904724c47249b10000131

'''
# Long version
def points(games):
    pnts, lst = 0, [i for i in games]
    
    for j in range(len(lst)):
        if lst[j][0] > lst[j][2]:
            pnts += 3
        if lst[j][0] == lst[j][2]:
            pnts += 1

    return pnts
    '''

# Compact version  
def points(games):
    return sum(sum([i[0]>i[2]]*3+[i[0]==i[2]]) for i in games)
