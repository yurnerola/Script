#!/usr/bin/python
ab={'Swaroop':'Swaroop@byteofpython.info',
	'Larry':'larry@wall.org',
	'Matsumoto':'matz@ruby-lang.org'}

print "Swaroop's email is %s"%ab['Swaroop']

ab['Guido']='guido@python.org'

del ab['Larry']

for name,address in ab.items():
	print 'Contact %s at %s'%(name,address)

print "\nGuido's address is %s"%ab['Guido']