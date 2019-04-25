# See: https://www.codewars.com/kata/51689e27fe9a00b126000004

def format_words(words):
    if words is not None:
        while not all(words): words.remove('')
        return ' and '.join(words).replace(' and', ',', len(words)-2) if words else ''
    return ''