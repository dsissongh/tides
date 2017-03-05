import os
from datetime import timedelta
from datetime import datetime
import requests
from bs4 import BeautifulSoup

#needed for class
from html.parser import HTMLParser

class HTMLTextExtractor(HTMLParser):
	def __init__(self):
		#super().__init__()
		HTMLParser.__init__(self)
		self.result = [ ]

	def handle_data(self, d):
		self.result.append(d)

	def handle_charref(self, number):
		codepoint = int(number[1:], 16) if number[0] in (u'x', u'X') else int(number)
		self.result.append(unichr(codepoint))

	def handle_entityref(self, name):
		codepoint = htmlentitydefs.name2codepoint[name]
		self.result.append(unichr(codepoint))

	def get_text(self):
		return u''.join(self.result)

def html_to_text(html):
	s = HTMLTextExtractor()
	s.feed(html)
	return s.get_text()


def getlatlonforstation(stationname):
	#https://tidesandcurrents.noaa.gov/tide_predictions.html?gid=1415

	request = requests.get("https://tidesandcurrents.noaa.gov/tide_predictions.html?gid=1415")
	#print(request.text)

	data = request.text.split("\n")
	datas = []
	for line in data:
		if '<td class="stationname">' in line:
			if stationname.lower() in line.lower():
				texto = BeautifulSoup(line, "html.parser")
				for tag in texto.find_all('td'):
					datas.append(tag.text.strip())

	return datas

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

def getlatlonfromstation(station):
	#https://tidesandcurrents.noaa.gov/tide_predictions.html?gid=1415

	request = requests.get("https://tidesandcurrents.noaa.gov/tide_predictions.html?gid=1415")
	#print(request.text)

	data = request.text.split("\n")
	datas = []
	for line in data:
		if '<td class="stationname">' in line:
			if "PORT TOWNSEND" in line:
				texto = BeautifulSoup(line, "html.parser")
				for tag in texto.find_all('td'):
					datas.append(tag.text.strip())

	return datas


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