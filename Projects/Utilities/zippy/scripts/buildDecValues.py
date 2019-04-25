# coding: utf-8 
 
def pause(): 
    return raw_input("Press any key to continue...") 
 
file = open("dec_8char.txt","w+") 
for i in range(100000000):
	file.write("%08d\n" % (i)) 

print("The script has completed!")
file.close()
pause()