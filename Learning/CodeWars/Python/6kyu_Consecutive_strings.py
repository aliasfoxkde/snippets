# See: https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(s, k):
    return max([''.join(i) for i in zip(*[s[i:] for i in range(k)])]+[''], key=len)
