# See: https://www.codewars.com/kata/58bfa1ea43fadb41840000b4

'''
def folding(a,b, count = 0):
    while a > 0 and b > 0:
        a, b, count = max(a-b, b), min(a-b, b), count+1
    return count
    '''

# Compact version  
def folding(a, b, c=0):          
    return folding(b, a%b, c+a//b) if b else c
