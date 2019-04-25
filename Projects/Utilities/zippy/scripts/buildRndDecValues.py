# coding: utf-8 
import random

s = "0123456789"

def pause(): 
    return raw_input("Press any key to continue...") 
 
file = open("rndDec_8char.txt","w+") 

for a in range(100000000):
	file.write(''.join(random.choice(s) for i in range(8))+"\n")

print("The script has completed!")
file.close()
pause()