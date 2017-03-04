from func import generatedatadictionary

#needed for latlon
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



#get the list of files
files = generatedatadictionary()
print(str(files))
print("\n")
for key in files:
	print(key)


	#get the associated lat/lon
	data = getlatlonforstation(key)
	print(str(data))
	latitude = data[2].replace("+","")
	longitude = data[3]
	print(latitude)
	print(longitude)

	#get the report for the day

	request = requests.get("http://marine.weather.gov/MapClick.php?lon=" + longitude + "&lat=" + latitude + "#.WLd5Yu2lvVM")
	data = request.text

	datas = data.split("\n")
	daytolookfor = "Saturday"
	for line in datas:
		if "forecast-label" in line:
			newdata = line.split('forecast-label')
			for newline in newdata:
				nohtml = html_to_text(newline)
				if nohtml[0:2] == '">':
					nohtml = nohtml[2:]

				if daytolookfor in nohtml:
					if not daytolookfor + " Night" in nohtml:
						nohtml = nohtml.replace(daytolookfor,daytolookfor + ": ")
						print(nohtml)
						#print(html_to_text(newline))
						#print("\n")
						#14

	print("---------------------------------------------------------------\n")



