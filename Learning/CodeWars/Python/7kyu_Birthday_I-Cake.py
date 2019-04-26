# See: https://www.codewars.com/kata/5805ed25c2799821cb000005

'''
# Long version:
def cake(candles,debris):
    y = 0
    for i, c in enumerate(debris):
        if i % 2 == 1:
            y += ord(c)-ord('a')+1
        else:
            y += ord(c)
    if y > 0.7 * candles: 
        return "Fire!"
    return "That was close!"
    '''

# Compact version
def cake(candles,debris):
    return ['That was close!','Fire!'][candles<=sum(map(ord, debris))]