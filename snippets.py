""" This is just a simple library of python "snippits" to either 
    1) make development simplier instead of having to rewrite 
    common or useful code over again, 2) or just clever code 
    I wanted to save while learning python.

    Useful Tools, Libraries, Learning Reference, and Links:
     * https://docs.sympy.org/latest/modules/simplify/simplify.html
	 * https://passwordsgenerator.net
	 * http://norvig.com/sudoku.html
	
"""
    
def pause():
    return raw_input("Press Enter to continue...")

""" --- Useful list comprehension tricks --- """
def flatten(tuple):
    return sum(tuple, [])
            
""" ----- Useful Math Functions ----- """
def factorial(n):
    return eval(str(range(1,n+1))[1:-1].replace(', ','*'))
    
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

""" ---- Econding Conversions ---- """
def ascii2bin(string):
    return

def ascii2hex(string):
    return
    
def bin2Ascii(n):
    return
    
def bin2hex(n):
    return
    
def int2bin(n):
    return ''.join(str((n & (1 << i)) and 1) for i in range(len(str(n))*8,-1,-1)).lstrip('0')

def hex2bin(hex_string):
    return ''.join(bin(ord(x))[2:].rjust(8,'0')[::-1] for x in hex_string)

""" ----- "Fun" Functions I've written ---- """
def zodiac(month, day, year):
    zodiac = [ "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", 
               "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
               "Sagittarius" ]
    cutoff = [22, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22]
    
    if day < cutoff[month]: 
        month -= 1
    
    return zodiac[month%12]

def chinese_zodiac(year):
    zodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", 
              "Rabbit", "Dragon", "Snake", "Horse", "Goat" ]
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
    # Credit Card Validator or Mod 10, or Luhn algorithm
	# refering to it's creator 'Hans Peter Luhn'
    return (sum(map(int, str(input)[1::2])) + \
            sum(sum(map(int, str(i*2))) for i in \
            map(int, str(input)[0::2]))) % 10 == 0
            
def nthDimList(n):
    lst = [0] * 3
    if n >= 2:
        for i in range(n-1):
            lst = [lst for j in xrange(3)]
    return lst

def piCross_solver(grid):
    return
	
def baccarat_simulator():
    return
	
def suduko_solver(grid):
    return
	
""" ---- File tools ---- """
def stripFile(filename, seperator='\n'):
    "Parse a file into a list of strings, separated by seperator."
    return file(filename).read().strip().split(seperator)
	
