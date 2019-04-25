# See: https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    l = list(set(arr))
    if arr.count(l[0]) > 1:
        return l[1]
    return l[0]