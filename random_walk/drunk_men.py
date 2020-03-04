import random

class Drunk(object):
	def __init__(self, name = None):
		self.name = name
	def __str__(self):
		if self.name != None:
			return self.name
		else:
			return 'Anonymous'

class UsualDrunk1(Drunk):
	def takeStep(self):
		stepChoices = [(0,1),(0,-1),(1,0),(-1,0)]
		return random.choice(stepChoices)

class UsualDrunk2(Drunk):
	def takeStep(self):
		stepChoices = [(0,2),(0,-2),(2,0),(-2,0)]
		return random.choice(stepChoices)