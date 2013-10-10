from wisesoldier import *
from wisemonster import *
from abstractenemyfactory import *
class WiseEnemyFactory(AbstractEnemyFactory):
	def createSoldier(self):
		soldier = WiseSoldier()
		return soldier
	def createMonster(self):
		monster = WiseMonster()
		return monster
