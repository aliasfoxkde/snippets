# See: https://www.codewars.com/kata/5be7f613f59e0355ee00000f

'''
# Long version
from datetime import *

def solve(a,b):
	ans = []
	for i in range(a, b+1):
		for j in (1, 3, 5, 7, 8, 10, 12):
			start = date(i, j, 1)
			if start.strftime("%a") == "Fri":
				ans.append(start.strftime("%b"))
	return (ans[0], ans[-1], len(ans))  
    '''

# Compact version  
from calendar import month_abbr as abr
from datetime import *

def solve(a,b):
    ans = [abr[m] for y in range(a,b+1) for m in (1,3,5,7,8,10,12) if date(y, m, 1).weekday() == 4]
    return (ans[0], ans[-1], len(ans))
