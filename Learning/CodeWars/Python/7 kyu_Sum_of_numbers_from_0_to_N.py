# See: https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763

def show_sequence(n):
    if n == 0:
        return '0=0'
    elif n < 0:
        return str(n) + '<0'
    return str(range(n+1))[1:-1].replace(', ','+') + ' = ' + str(sum(range(1,n+1)))
