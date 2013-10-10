from monster import *

class SillyMonster(Monster):
	def __init__(self):
		print "A SillyMonster is created."
		self.vitality=20
		self.intelligence=30

	def getVitality(self):
		return self.vitality

	def getIntelligence(self):
		return self.intelligence
