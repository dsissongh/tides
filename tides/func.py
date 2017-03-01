import os
from datetime import timedelta
from datetime import datetime

def sethistory(history,text):
	fh = open(history,"w")
	fh.write(text)
	fh.close()

def gethistory(history):
	fh = open(history,"r")
	text = fh.readline()
	fh.close()
	return text

def setpropercase(title):
	newelements = []
	elements = title.split(" ")
	#print(str(elements))
	for word in elements:
		newelements.append(str(word).lower().title())

	#print(str(newelements))
	title = ' '.join(newelements)
	return title

def generatedatadictionary():
	stations = {}

	dh = os.listdir(".")
	for file in dh:
		if "annual" in file:
			#print(file)
			fh = open("./" + file, "r")
			name=""
			for line in fh:
				#print(line)

				if "StationName:" in line:
					#print(line)
					elements = line.split("StationName:")
					if not(name == "found"):
						#print(file, elements[1])
						stationname = setpropercase(elements[1].strip())
						stations.update({stationname:file})
						name = "found"

	return stations

def getstationnamefromfile(file):
	fh = open("./" + file, "r")
	for line in fh:
		#print(line)

		if "StationName:" in line:
			#print(line)
			elements = line.split("StationName:")
			stationname = setpropercase(elements[1].strip())
			break

	return stationname

def getdatefornextsaturday(cdate, dow):
	saturday = 5-dow
	if saturday > -1:
		saturdaydate = datetime.now() + timedelta(days=int(saturday))
		return saturdaydate
	else:
		return cdate
	
def resetcolor(term):
	#term.reset does not appear to be resetting the color correctly
	#set the terminal back to lt grey on black
	term.cprint(7,0,'')
	
	#colors
	'''
			  "BLACK": 0,
			  "BLUE": 1,
			  "GREEN": 2,
			  "CYAN": 3,
			  "RED": 4,
			  "PURPLE": 5,
			  "BROWN": 6,
			  "LGREY": 7,
			  "DGRAY": 8,
			  "LBLUE": 9,
			  "LGREEN": 10,
			  "LCYAN": 11,
			  "LRED": 12,
			  "LPURPLE": 13,
			  "YELLOW": 14,
			  "WHITE": 15
	 '''