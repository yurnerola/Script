#!/usr/bin/python

#python using_sys.py we are arguments
import  sys
print 'The command line argument are:'
for i in sys.argv:
	print i
print '\n\nThe PYTHONPATH is ',sys.path,'\n'

print sys.argv[0]
print sys.argv[1]
print sys.argv[2]
print sys.argv[3]
