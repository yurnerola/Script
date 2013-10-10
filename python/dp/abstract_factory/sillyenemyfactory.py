from sillysoldier import *
from sillymonster import *
from abstractenemyfactory import *
class SillyEnemyFactory(AbstractEnemyFactory):
	def createSoldier(self):
		soldier = SillySoldier()
		return soldier
	def createMonster(self):
		monster = SillyMonster()
		return monster
