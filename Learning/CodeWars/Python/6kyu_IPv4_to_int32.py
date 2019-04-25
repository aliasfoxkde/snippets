# See: https://www.codewars.com/kata/52ea928a1ef5cfec800003ee

def ip_to_int32(ip):
    i, m = map(int, ip.split('.')), 256
    return m**3 * i[0] | m**2 * i[1] | m * i[2] | i[3]