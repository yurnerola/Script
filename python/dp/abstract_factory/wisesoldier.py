from soldier import *

class WiseSoldier(Soldier):
	def __init__(self):
		print "A WiseSoldier is created."
		self.speed=100
		self.weapon="gun"
	
	def getSpeed(self):
		return self.speed

	def getWeapon(self):
		return self.weapon
