from monster import *

class WiseMonster(Monster):
	def __init__(self):
		print "A WiseMonster is created."
		self.vitality=90
		self.intelligence=80

	def getVitality(self):
		return self.vitaliy

	def getIntelligence(self):
		return self.intelligence
