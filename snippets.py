#! /usr/bin/env python

# coding: utf-8

metadata = dict(
    __author__="Aliasfox KDE",
    __version__="0.0.3",
    __license__="MIT License",
    __email__="aliasfox@cyopsys.com",
    __status__="Work in Progress",
    __url__="https://github.com/aliasfoxkde/snippets",
    __summary__="Simple but helpful library of snippets for python.",
    __keywords__="python, aliasfox, snippets"
)
globals().update(metadata)

__all__ = metadata.keys()

""" This is just a simple library of python "snippits" to either 
    1) make development simplier instead of having to rewrite 
    common or useful code over again, 2) or just clever code 
    I wanted to save while learning python. Also, it might be
    out of scope but I decided to organize my programming progress
    here as well.

    Useful Tools, Libraries, Learning Reference, and Links:
     * https://www.geeksforgeeks.org/10-essential-python-tips-tricks-programmers/
     * https://pythontips.com/2015/04/19/nifty-python-tricks/
     * https://bobbelderbos.com/2016/06/python-tips/
     * https://docs.sympy.org/latest/modules/simplify/simplify.html
     * https://www.w3schools.com/python/python_datetime.asp
     * https://docs.python.org/3/tutorial/modules.html
     * https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
     * https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script
     * https://www.blog.pythonlibrary.org/2014/03/20/python-102-how-to-profile-your-code/
     * https://docs.python.org/2/library/profile.html
     * https://pypi.org/project/about/
     * https://pymotw.com/2/profile/
     * https://passwordsgenerator.net
     * http://norvig.com/sudoku.html
     * https://github.com/vinta/awesome-python
     
    Useful Guides:
     * https://linuxhint.com/python_scripts_beginners_guide/     
    
    Useful Notes:
     * "from <module> import <function> as <abbreviation>
     * "from <module> import <function1>, <function2>, ...     
"""


def pause():
    return raw_input("Press Enter to continue...")


# --- Useful list comprehension tricks ---
def adv_map(func, *seqs):
    # Unzip an array of arrays or tuple
    return [func(*args) for args in zip(*seqs)]

    
def flatten(tuple):
    ''' Given an array of nested lists, produce a single flattened array. '''
    # Example: [[1,2,3],[1,2,3],[1,2,3]] --> [1, 2, 3, 1, 2, 3, 1, 2, 3]
    # https://github.com/keon/algorithms/blob/master/algorithms/arrays/flatten.py

    try:
        for _ in range(len(tuple)):
            array = sum(tuple, [])
    except TypeError:
        pass
    return tuple


def nth_dim_list(n, dims):
    # Creates a multi-dimensional list or tuple
    lst = [0] * n
    return [[lst for j in range(n)] if dims > 1 else lst for i in range(dims - 1)]


def deduplicate(array):
    # Removes Duplicates from a "flattened" list
    return sorted(set(array), key=array[::-1].index)[::-1]


def unzip(tuple):
    # Unzips a simple list or tuple
    return zip(*tuple)


# ----- Useful Math Functions -----
def cypher(cyper, key):
    # Simple Shift-Cyper function
    return ''.join(chr(i - int(b) + 96) for i, b in zip(cyper, str(key) * 29))


def decypher(cyper, key):
    # Simple Decypher for Cyper function (WIP)
    return


def dirty_mod(n, mod):
    """ "A Simple, Down and Dirty" Modulous Function that used the remainder
        decimal remainder and multiplies it by the mod value """
    return (n / float(mod) - n // mod + .001) // (1 / mod)


def factorial(n):
    # Down and Dirty factorial function
    return eval(str(range(1, n + 1))[1:-1].replace(', ', '*'))


def plus_one(array):
    ''' Adds +1 to the tail of a given array, alternative algorithm '''
    # https://github.com/keon/algorithms/blob/master/algorithms/arrays/plus_one.py
    array[-1] = array[-1]+1
    return array


def fib(n):
    """ Calculate the nth digit of Fibonacci
        0 1 1 2 3 5 8 13 21 34 ... """
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def get_integral(c, e):
    return "%sx^%s" % (c / (e + 1) if c % (e + 1) != 0 else c // (e + 1), e + 1)


def hamming(n):
    """ A *Hamming number* is a positive integer of the form 2i3j5k,
        See: https://en.wikipedia.org/wiki/Regular_number """
    h = sorted(2 ** i * 3 ** j * 5 ** k for i in range(33) for j in range(21) for k in range(15))
    return h[n - 1]


def longest_consecutive(string_array, n):
    return max([''.join(i) for i in zip(*[string_array[i:] for i in range(n)])] + [''], key=len)


def pi(precision):
    return sum(4 / (i + c) if i % 2 else -4 / (i + c) for c, i in enumerate(range(1, precision)))


def pi_by_ps(position, precision):
    # Script to get digit of pi without re-calculate from the begining
    return


def sqrt(n):
    return n ** .5


def multiple_of(number, value):
    n = (number - 1) // value
    return n * value * (n + 1) // 2


# ---- Econding Conversions ----
def ascii2bin(string):
    return


def ascii2hex(string):
    return


def bin2ascii(binary):
    from binascii import unhexlify
    return str(unhexlify('%x' % int(str(binary), 2)))[2:-1]


def bin2hex(n):
    return hex(int(str(bin), 2))[2:]


def bin2dec(binary):
    return int(str(binary), 2)


def alt_bin2dec(binary):
    """ Alternative binary calculator: I saw the formula one time for '111' as
        (1 x 2^2) + (1 x 2^1) + (1 x 2^0) = 7 and thought it was awesome, so I made a python
        function. Maybe not the most efficient but it adds a level of intuitiveness. """
    return sum(int(str(binary)[i]) * 2 ** i for i in range(len(str(bin))))


def hex2bin(hex_string):
    return ''.join(bin(ord(x))[2:].rjust(8, '0')[::-1] for x in hex_string)


# ----- "Fun" Functions I've written ----
def zodiac(month, day, year):
    zodiac_mm = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus",
                 "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
                 "Sagittarius"]
    cutoff = [22, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22]
    return zodiac_mm[month % 12] if day < cutoff[month] else zodiac_mm[month % 11]


def chinese_zodiac(year):
    zodiac_yy = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger",
                 "Rabbit", "Dragon", "Snake", "Horse", "Goat"]
    return zodiac_yy[year % 12]


def increment_string(string):
    # See: https://www.codewars.com/kata/string-incrementer
    for i in range(5, 0, -1):
        if len(string) > i - 1 and string[-i].isdigit():
            return string[:-i] + str(int(string[-i:]) + 1).zfill(i)
    return string + '1'


def numerology(month, day, year, name=''):
    n_list = name.lower().split()
    numbers = [sum(ord(j) - 96 for j in n_list[i]) % 9 for i in range(len(n_list))] + [(month + day + year) % 9]
    return numbers


def n_friday_the_13ths(y):
    # My CodWars @ https://www.codewars.com/kata/56eb0be52caf798c630013c0
    count = 0  # Clean & Pure Math Example
    for m in range(3, 15):
        if m == 13: y -= 1
        if (y % 100 + (y % 100 // 4) + (y // 100) // 4 - 2 * (y // 100) + 26 * (m + 1) // 10 + 12) % 7 == 5:
            count += 1
    return count


def luhn(card):
    """ Credit Card Validator with Mod 10, or Luhn algorithm
        referring to it's creator 'Hans Peter Luhn' """
    card = str(card).replace(' ', '')
    return (sum(map(int, card[1::2])) + sum(sum(map(int, str(i * 2))) for i in map(int, card[0::2]))) % 10 == 0


def pied_piper(town):
    """ How many rats are there?
        See: https://www.codewars.com/kata/598106cb34e205e074000031
        Example: ~O~O~O~OP~O~OO~ has 2 deaf rats """
    return town.replace(' ', '')[::2].count('O')


# ------ Puzzle and Game Related ---------
def minesweeper_solver():
    return


def baccarat_simulator():
    return


def sudoku_solver(grid):
    return


def nonogram_solver(grid):
    return


# -------- File tools --------
def strip_file(filename, seperator='\n'):
    # "Parse a file into a list of strings, separated by seperator."
    return file(filename).read().strip().split(seperator)


# ------ Sorting Algorithms ---------
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def is_turing_equation(s):
    # See https://www.codewars.com/kata/simple-fun-number-384-is-turings-equation
    return int(s[::-1].split('=')[0]) == sum(map(int, s[::-1].split('=')[1].split('+')))


# --------- Converting values ---------
def f2c(ferinheight=0):
    return ferinheight * 9 / 5 + 32  # celsius


def c2f(celsius=0):
    return (celsius - 32) * 5 / 9  # ferinheight


# --------- String evaluation ---------
def is_anagram(str1, str2):
    return all(i in str2 for i in map(str, str1))


def is_palindrome(string):
    return string == string[::-1]


# ------------- Debug & Testing -------------
def inspect(object):
    return dir(object)


def debug():
    from pdb import set_trace
    return set_trace()


def unit_tests(level):
    """ Automated Unit tests and script profiling """
    return


# -------------- Useful Tools ---------------
def wget(url):
    # Downloads content from web, similiar to wget on Linux
    from urllib import urlretrieve as retrieve
    retrieve(url + file, filename=file)


# ---------- Time & Date Libraries ----------
from datetime import datetime


def t_zone(Zone, Time=datetime.now()):
    return


def time_globals():
    global yy, mm, dd, hh, m, s, wDay, yDay, isDst, start
    yy, mm, dd, hh, m, s, wDay, yDay, isDst = datetime.today().timetuple()
    start = datetime.now()
    

# -------------- DSC Tools ------------------
def string_counter(string):
    lst = sum(map(list, string), [])
    return [(x, lst.count(x)) for x in set(lst)]


# --------- Useful Python 3.8 'Features' ---------
"""
# Commented out for Python 2x Compatibility
def mirror(list):
    # Assign and modify a variable in one line, usually this 
    # would lead to Variable is not defined error.
    return (s := sorted(list)) + s[-2::-1]


def mirrorAlgo(n):
    # Fun math pattern that results in repeating mirrored values
    return int("1"*n)**2


def int2bin(n):
    return int(f'{n:b}')
    """
