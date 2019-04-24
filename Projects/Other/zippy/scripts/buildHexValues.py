# coding: utf-8 
 
def pause(): 
    return raw_input("Press any key to continue...") 
 
hex = "0123456789ABCDEF" 
file = open("hex_8char.txt","w+") 
 
for a in hex: 
	for b in hex: 
		for c in hex: 
			for d in hex: 
				for e in hex: 
					for f in hex: 
						for g in hex: 
							for h in hex: 
								file.write("%s%s%s%s%s%s%s%s\n" % (a,b,c,d,e,f,g,h)) 

print("The script has completed!")
file.close()
pause()