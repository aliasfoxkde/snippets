# coding: utf-8 
import random

s = "0123456789ABCDEF"
 
def pause(): 
    return raw_input("Press any key to continue...") 
 
file = open("rndHex_8char.txt","w+") 

# Out of range error for value 4294967296
for a in range(64):
	for a in range(67108864):
		file.write(''.join(random.choice(s) for i in range(8))+"\n")

print("The script has completed!")
file.close()
pause()