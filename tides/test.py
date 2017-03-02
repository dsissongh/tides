#http://marine.weather.gov/MapClick.php?lon=-122.89559&lat=47.67598#.WLd5Yu2lvVM

import requests

from html.parser import HTMLParser
#import htmlentitydefs

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


request = requests.get("http://marine.weather.gov/MapClick.php?lon=-122.89559&lat=47.67598#.WLd5Yu2lvVM")
data = request.text

datas = data.split("\n")
daytolookfor = "Saturday"
for line in datas:
	if "forecast-label" in line:
		newdata = line.split('forecast-label')
		for newline in newdata:

			print(html_to_text(newline))
			print("\n")