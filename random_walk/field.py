class Field(object):
	def __init__(self):
		self.drunks = {}

	def addDrunk(self, drunk, location):
		if drunk in self.drunks:
			raise ValueError("Duplicate Drunk")
		else:
			self.drunks[drunk] = location

	def moveDrunk(self, drunk):
		if drunk not in self.drunks:
			raise ValueError("Drunk not in field")
		xDist, yDist = drunk.takeStep()
		print("\n\n>>>>xDist, yDist",xDist,'-',yDist)
		currentLocation = self.drunks[drunk]
		self.drunks[drunk] = currentLocation.move(xDist, yDist)

	def getLoc(self, drunk):
		if drunk not in self.drunks:
			raise ValueError('Drunk not in field')
		return self.drunks[drunk]