# See: https://www.codewars.com/kata/5809b62808ad92e31b000031

def calculate(s):
    return str(eval(s.replace("plus","+").replace("minus","-")))