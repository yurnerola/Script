class test:
	member=1
	def get(self):
		print self.member
	def set(self):
		self.member=8

a=test()

a.set()
a.get()

b=test()
b.get()