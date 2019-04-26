# See: https://www.codewars.com/kata/57e3f79c9cb119374600046b

'''
# Long version
def hello(*name):
    if name:
        name = name[0]
        if name == '': name = "World"
        return ("Hello, %s!" % name.capitalize())
    return ("Hello, World!")
    '''

# Compact version  
def hello(name=''):
    return "Hello, %s!" % ['World',name.title()][name!='']
