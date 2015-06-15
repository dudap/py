import string
import fileinput
howMany = raw_input("Podaj przesuniecie: ")
howMany = int(howMany) % 26
i = 0
tmp = ""
for line in fileinput.input():
	if(int(howMany) > 0 and int(howMany) < 27):			
		line = line.rstrip()
		length = len(line)
		while(i < length):	
			if(ord(line[i]) > 96 and ord(line[i])<123):
				c = ord(line[i])
				c =(((c - 97) + howMany)%26)+97 		
			i = i+1
			tmp += chr(c)
		print tmp
		tmp = ""
		i=0
