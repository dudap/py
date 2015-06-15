#-*- coding:utf -*-
import string,sys
def NWD(liczba1,liczba2):


	a = liczba1
	b = liczba2

	while b != 0:
		c = a % b
		a = b
		b = c

	if a == 1:
		print u"(%d,%d) sa wzglednie pierwsze"%(liczba1,liczba2)
	else:
		print u"(%d,%d) nie sa wzglednie pierwsze"%(liczba1,liczba2)

if __name__ == '__main__':
	liczba1 = int(sys.argv[1])
	liczba2 = int(sys.argv[2])
	NWD(liczba1,liczba2)