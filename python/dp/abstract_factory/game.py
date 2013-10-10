import sys

from sillyenemyfactory import *
from wiseenemyfactory import *

if __name__=="__main__":
	args=sys.argv
	if("silly" in args):
		factory=SillyEnemyFactory()
	elif("wise" in args):
		factory=WiseEnemyFactory()
	else:
		print "Usage:python game.py silly|wise"
		exit()

soldier=factory.createSoldier()
monster=factory.createMonster()


