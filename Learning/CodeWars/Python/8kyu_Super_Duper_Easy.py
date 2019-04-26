# See: https://www.codewars.com/kata/55a5bfaa756cfede78000026

'''
# Long version
def problem(a):
    if type(a) == str:
        return "Error"
    return a*50+6
    '''

# Compact version  
def problem(a):
    return "Error" if type(a) == str else a*50+6
