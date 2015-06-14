import sys, string, crypt
def uncode(file):
	passwd = open(file).read()
	chars = string.ascii_letters
	for a in chars:
			for b in chars:
					for c in chars:
				for d in chars:
					for e in chars:
									trial = a+b+c
									crypted = crypt.crypt( trial, passwd)
									if crypted == passwd:
										break
					if crypted==passwd:
						break
					if crypted == passwd:
					  break
				if crypted == passwd:
					break
		if crypted ==passwd:
			break
	if crypted == passwd:
		print "Hasło złamane: " + trail
	else:
		print "Nie złamano hasła"

if __name__ == '__main__':
	uncode(sys.argv[1])
