from soldier import *

class SillySoldier(Soldier):
	def __init__(self):
		print "A SillySoldier is created."
		self.speed=10
		self.weapon="saber"

	def getSpeed(self):
		return self.speed
	
	def getWeapon(self):
		return self.weapon


