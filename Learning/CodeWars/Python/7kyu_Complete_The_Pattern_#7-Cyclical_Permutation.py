# See: https://www.codewars.com/kata/557592fcdfc2220bed000042

def pattern(n):
    return '\n'.join(''.join(map(str, range(1,n+1)[i:n]+range(1,n+1)[:i])) for i in range(n))
