# See: https://www.codewars.com/kata/51689e27fe9a00b126000004

'''
# Long version
def format_words(words):
    if words is not None:
        while not all(words): 
            words.remove('')

        if len(words) == 1:
            return str(words[0])
        elif len(words) == 2:
            return " and ".join(words)
        elif len(words) > 2:
            return ", ".join(words[:-1]) + " and " + str(words[-1])
    return ''
    '''

# Compact version  
def format_words(words):
    if words is not None:
        while not all(words): words.remove('')
        return ' and '.join(words).replace(' and', ',', len(words)-2) if words else ''
    return ''
