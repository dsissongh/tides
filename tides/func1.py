import os


def showmenu():
	return generatedatadictionary()


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