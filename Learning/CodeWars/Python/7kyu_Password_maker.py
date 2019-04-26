# See: https://www.codewars.com/kata/5637b03c6be7e01d99000046

def make_password(phrase):
    return ''.join(dict(zip('iIoOsS','110055')).get(i[0],i[0]) for i in phrase.split())