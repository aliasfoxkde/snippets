# See: https://www.codewars.com/kata/5ad0d8356165e63c140014d4

'''
# Long Version
def final_grade(exams, projects):
    if exams > 90 or projects > 10:
        return 100
    if exams > 75 and projects > 4:
        return 90
    if exams > 50 and projects > 1:
        return 75
    return 0
	'''

# Compact version
def final_grade(e, p):
    return [[0,75,90][(e>50 and p>1)+(e>75 and p>4)], 100][e>90 or p>10]
