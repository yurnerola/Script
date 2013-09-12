import re;

def usage():
	return  '''
	Usage:<br/>
		logger [options]<br/>

	Options:<br/>
		-h              Print this usage.<br/>
		-i <hallid><br/>
	Example:<br/>
		logger -i 447283
	'''


if __name__=="__main__":
	m=re.match(r'(\w+) (\w+)(?P<sign>.*)','hello world!')

	print "m.string:",m.string
	print "m.re:",m.re
	print "m.pos:",m.pos
	print "m.endpos:",m.endpos
	print "m.lastindex:",m.lastindex
	print "m.lastgroup:",m.lastgroup

	print "m.group(1):",m.group(1)
	print "m.group(1,2):",m.group(1,2)
	print "m.groups():",m.groups()
	print "m.groupdict():",m.groupdict()

	p=re.compile(r'\d+')
	print p.split('one1two2three3four4')
	print p.findall('one1two2three3four4')


	# for m in p.finditer('one1two2three3four4'):
	# 	print m.group()

	p=re.compile(r'(\w+) (\w+)')
	s='i say,hello world!'

	# print p.sub(r'\2 \1',s)

	def func(m):
	    return m.group(1).title() + ' ' + m.group(2).title()

	print p.sub(func, s)
