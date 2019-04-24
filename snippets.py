""" This is just a simple library of python "snippits" 
    to either 1) make development simplier instead of 
    having to rewrite common or useful code over again,
    2) or just clever code I wanted to save while 
    learning python. """
    
def pause():
    return raw_input("Press Enter to continue...")

def zodiac(month, day, year):
    zodiac = [ "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]
    cutoff = [22, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22]
    
    if day < cutoff[month]: 
        month -= 1
    
    return zodiac[month%12]

def chinese_zodiac(year):
    zodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]    
    return zodiac[year%12]
    
def numerology(month, day, year, name=''):     
    nList = name.lower().split()
	numbers = [sum(ord(j)-96 for j in nList[i])%9 for i in range(len(nList))]+[(month+day+year)%9]
    return numbers
    
def n_friday_the_13ths(y):    
    # My CodWars @ https://www.codewars.com/kata/56eb0be52caf798c630013c0
    count = 0 # Clean & Pure Math Example      
    for m in range(3,15):
        if m == 13: y-=1            
        if (y%100+(y%100//4)+(y//100)//4-2*(y//100)+26*(m+1)//10+12)%7==5:
            count += 1
    return count

def luhn(input=0):
    # Credit Card Validator Luhn algorithm
    return (sum(map(int, str(input)[1::2])) + \
            sum(sum(map(int, str(i*2))) for i in \
            map(int, str(input)[0::2]))) % 10 == 0

""" Useful list comprehension tricks """
def flatten(tuple):
	return sum(tuple, [])
			
""" Useful Math Functions """
def fib(n):
    """ Calculate the nth digit of Fibonacci
        0 1 1 2 3 5 8 13 21 34 ... """
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

def pi(position, precision):
    return
    
def sqrt(n):
    return n**.5
    
def factorial(n):
    return eval(str(range(1,n+1))[1:-1].replace(', ','*'))