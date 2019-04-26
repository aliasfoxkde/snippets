# See: https://www.codewars.com/kata/5a1e6323ffe75f71ae000026

'''
# Long version
def is_turing_equation(s):
    _op, start = '+-/*', 0
    val0, val1, eq, op = '', '', '', ''
    
    for i in range(len(s)):
        if s[i] in _op:
            op = s[i]
            val0 = s[:i][::-1]
            start = i+1
            
        if s[i] == '=':
            eq = s[i+1::][::-1]           
            val1 = s[start:i][::-1]
            
        if len(eq) > 1: eq = eq.lstrip('0')
        if len(val0) > 1: val0 = val0.lstrip('0')
        if len(val1) > 1: val1 = val1.lstrip('0')

    return eval(val0 + op + val1 + ' == ' + eq)
    '''

# Compact version  
def is_turing_equation(s):
    return int(s[::-1].split('=')[0]) == sum(map(int, s[::-1].split('=')[1].split('+')))
