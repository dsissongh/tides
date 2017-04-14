import os
import collections

def showmenu():
	''' 
		generates the menu based on the files for anual tide
		information found in the directory 
	'''

	order = {}
	menu = ''
	count = 1
	stations = generatedatadictionary()
	cstations = collections.OrderedDict(sorted(stations.items()))
	for key in cstations:
		order.update({count:cstations[key]})
		menu += str(count) + ". " + key + "\n"
		count += 1

	return menu, order


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

def setpropercase(title):
	newelements = []
	elements = title.split(" ")
	#print(str(elements))
	for word in elements:
		newelements.append(str(word).lower().title())

	#print(str(newelements))
	title = ' '.join(newelements)
	return title


def gethistory(history, order):
	#history = "../" + history
	choice = ''
	if os.path.exists(history):
		print("found")
		fh = open(history,"r")
		choice = fh.readline()
		fh.close()
		print("--" + choice)

	for key in order:
		print(order[key])
		if choice == order[key]:
			choice = str(key)

	else:
		choice = ''

	selection = input("\nWhat station would you like to use for source tide data? [" + choice + "]")
	return selection

def sethistory(history,text):
	print(history)
	print(text)
	fh = open(history,"w")
	fh.write(text)
	fh.close()