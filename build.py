import datetime
import sys
import copy
import random

timestamp = sys.argv[1]
dedication = sys.argv[2]

print timestamp
lilyNoteNames = ['c','cis','d','ees','e','f','fis','g','gis','a','bes','b']

def toLilyName(noteNumber):
	pitchClass = noteNumber%12
	numberOfUpTicks = 1 + int(noteNumber/12)
	return lilyNoteNames[pitchClass] + "'"*numberOfUpTicks

notes = [2,4,7,9,10,11,12,14,15,16,17,19]
theseNotes = []
while theseNotes == []:
	theseNotes = random.sample(notes,3)
	theseNotes = sorted(theseNotes)
	if theseNotes[1] - theseNotes[0] < 2:
		theseNotes = []
	elif theseNotes[2] - theseNotes[1] < 2:
		theseNotes = []
	elif theseNotes[2] - theseNotes[0] < 5:
		theseNotes = []
	elif theseNotes[0] == theseNotes[2]%12:
		theseNotes = []
	elif theseNotes[2] -theseNotes[0] == 7 and (theseNotes[1]-theseNotes[0] == 3 or theseNotes[1]-theseNotes[0] == 4):
		theseNotes = []

print theseNotes
goodToGo = False
allStates = []
while not goodToGo:
	state = [1,1,1]
	length = 200#random.randint(30,40)
	allStates = [state]
	changes = []
	for i in range(length):
		newState = [0,0,0]
		while sum(newState) == 0:
			newState = copy.deepcopy(state)
			itemInStateToChange = random.randint(0,2)
			changes.append(itemInStateToChange)
			newState[itemInStateToChange] = 1-state[itemInStateToChange]

		allStates.append(newState)
		state = newState

	goodToGo = True
	#check there is always a note who plays
	for i in range(length):
		if sum(allStates[i]) == 0:
			print "someone doesn't play"
			goodToGo = False
	
	#check we don't turn one note on off a lot
	doesBreakCycle = False
	for i in range(length-5):
		for j in range(3):
			if changes[i] != changes[i+j]:
				doesBreakCycle = True
	if not doesBreakCycle:
		print "one note constant"
		goodToGo = False

	permutations = [[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1]]
	maxIndex = -1
	for p in permutations:
		try:
			index = allStates.index(p)
			maxIndex = max(index,maxIndex)
		except:
			goodToGo = False
	allStates = allStates[:maxIndex+1]
	allStates.append([1,1,1])
	if len(allStates)> 25 or len(allStates) < 13:
		goodToGo=False

lilyBits = ["c'","f'","d''"]
lilyPrint = []
for i in range(len(allStates)):
	bit = "<"
	for j in range(len(allStates[i])):
		if allStates[i][j] == 1:
			bit = bit +' '+toLilyName(theseNotes[j])
	bit = bit + '>1 ~'
	lilyPrint.append(bit)

fd = open('score.ly','r')
out = open('out/out_'+str(timestamp)+'.ly','w')
for l in fd.readlines():
	toWrite = l
	if "part" in l:
		toWrite = " ".join(lilyPrint)
	if "name" in l:
		today = datetime.date.today()
		toWrite = "Generated for " + dedication + " on "+today.strftime('%b. %d, %Y')
	out.write(toWrite+'\n')
out.close()
fd.close()
print " ".join(lilyPrint)
print allStates
print len(allStates)





