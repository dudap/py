import datetime

import time

def czas():
	today = datetime.date.today() 
	czas = time.localtime()
	return str(today)+' '+str(czas[3]) +':'+ str(czas[4])
