import sys
import hashlib
def hash(password)
	md5  = hashlib.md5(password  )
	print md5.digest()
	print md5.hexdigest()
if __name__ == '__main__':
	hash(sys.argv[1])
