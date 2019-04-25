# See: https://www.codewars.com/kata/56eb0be52caf798c630013c0

def unlucky_days(y):    
    count = 0 # Clean & Pure Math Example without modules    
    for m in range(3,15):
        if m == 13: y-=1            
        if (y%100+(y%100//4)+(y//100)//4-2*(y//100)+26*(m+1)//10+12)%7==5:
            count += 1
    return count