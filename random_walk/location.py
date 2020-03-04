class Location(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def move(self, destX, destY):
		return Location(self.x + destX, self.y + destY)

	def distFrom(self, other):
		xDist, yDist = self.x - other.x, self.y - other.y
		return (xDist ** 2 + yDist ** 2) ** 0.5