import sys
import crypt
import string
import random
def hash(dane):
        a = 0
	for znak in dane:
                a += ord(znak)
        return a % 15485857 

def delay():
	a=random.randint(0,100)
	 
	for i in range(a):
         b=''


def hasloo(password):
	for i in range(10):
		salt = str(hash(password))
		haslo = crypt.crypt(password, salt)
		password=haslo
	haslo = crypt.crypt(haslo, 'po')
	return haslo 


def Entropy(text):
    import math
    log2=lambda x:math.log(x)/math.log(2)
    exr={}
    infoc=0
    for each in text:
        try:
            exr[each]+=1
        except:
            exr[each]=1
    textlen=len(text)
    for k,v in exr.items():
        freq  =  1.0*v/textlen
        infoc+=freq*log2(freq)
    infoc*=-1
    return infoc

#if __name__ == '__main__':
	#print Entropy(sys.argv[1])
