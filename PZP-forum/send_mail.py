#-*- coding: utf-8 -*-
import smtplib, socket,sys,getpass
from funktion import hasloo
def maillll(adres):

	try:
		smtpserver=smtplib.SMTP('smtp.gmail.com',587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		print 'connected succesfull'
		try:

			gmail_user='' # username
			gmail_pwd='' # password
			smtpserver.login(gmail_user,gmail_pwd)
			print 'zalogowano'
		except smtplib.SMTPException:
			print 'problem przy logowaniu'
			smtpserver.close()
			
	except (socket.gaierror, socket.error, socket.herror,smtplib.SMTPException),e:
		print 'connected filed'
		


	to=str(adres)
	a='Check Password'
	subject=str(a)
	token=losuj()
	bodymsg='Your token: '+str(token)
	header= 'To:' +to + '\n' +'From: '+gmail_user+ '\n' +'subject: ' +subject+ '\n'
	
	msg =header+'\n' +bodymsg +'\n\n'

	try:
		smtpserver.sendmail(gmail_user,to,msg)
	except:
		print u'Nie mogę wysłac'
		smtpserver.close()
		
	return str(token)
def losuj():
	import random
	return	hasloo(str(random.randint(0,99999999999999999999999999999)))	



