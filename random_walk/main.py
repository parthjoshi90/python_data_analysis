from location import Location
from field import Field
from drunk_men import Drunk, UsualDrunk1, UsualDrunk2

def walk(f, d, numstep):
	start = f.getLoc(d)
	for s in range(numstep):
		f.moveDrunk(d)
	return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
	DrunkMen = dClass()
	origin = Location(0, 0)
	distances = []
	for t in range(numTrials):
		f = Field()
		f.addDrunk(DrunkMen, origin)
		distances.append(round(walk(f, DrunkMen, numSteps), 1))
	return distances

def drunkTest(walkLengths, numTrials, dClass):
	for numSteps in walkLengths:
		distances = simWalks(numSteps, numTrials, dClass)
		print(dClass.__name__, 'random walk of', numSteps, 'steps')
		print('Mean = ', round(sum(distances)/len(distances), 4))
		print('Max = ',max(distances), 'Min =', min(distances))

drunkTest((10,), 100, UsualDrunk1)
# drunkTest((10, 100, 1000), 100, UsualDrunk2)