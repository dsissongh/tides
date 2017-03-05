import os
import argparse
import time
import datetime
import collections
import requests
from colorconsole import terminal
from func import resetcolor
from func import getdatefornextsaturday
from func import generatedatadictionary
from func import sethistory
from func import gethistory
from func import getstationnamefromfile
#from func import getlatlonfromstation
from func import getlatlonforstation
from func import html_to_text

history = "history.txt"


dow = datetime.datetime.today().weekday()
term = terminal.get_terminal(conEmu=False)
stations = generatedatadictionary()

cstations = collections.OrderedDict(sorted(stations.items()))

order = {}
count = 1
term.clear()
term.cprint(3, 0, '')
#print(str(cstations))
for key in cstations:
	order.update({count:cstations[key]})
	print("%s. %s" % (count, key))
	count += 1

#print(str(order))	
if os.path.exists(history):
	choice = gethistory(history)
	for key in order:
		if choice == order[key]:
			choice = str(key)

else:
	choice = ''

selection = input("\nWhat station would you like to use for source tide data? [" + choice + "]")

if selection == '':
	selection = int(choice)

tides = order[int(selection)]
choice = sethistory(history,order[int(selection)])
predate = time.strftime("%Y/%m/%d")
saturday = getdatefornextsaturday(predate, dow)
saturday = str(saturday).split(' ')
#print(str(saturday))
date = input("What date would you like H/L tide information for (yyyy/mm/dd)? [" + str(saturday[0].replace('-','/')) + "]")

if date == '':
	## yyyy/mm/dd format
	date = str(saturday[0].replace('-','/'))

#source: https://tidesandcurrents.noaa.gov


tidesfh = open(tides,'r')
sname = getstationnamefromfile(order[int(selection)])
term.cprint(14, 0, "Station: " + sname + " for " + date + "\n")

#get the associated lat/lon
data = getlatlonforstation(sname)
#print(str(data))
latitude = data[2].replace("+","")
longitude = data[3]

request = requests.get("http://marine.weather.gov/MapClick.php?lon=" + longitude + "&lat=" + latitude + "#.WLd5Yu2lvVM")
newdata = request.text

datas = newdata.split("\n")
daynottolookfor = "Saturday"
daytolookfor = "Saturday", "Today"

for line in datas:
	if "forecast-label" in line:
		newdata = line.split('forecast-label')
		for newline in newdata:
			nohtml = html_to_text(newline)
			if nohtml[0:2] == '">':
				nohtml = nohtml[2:]

			if any(s in nohtml for s in daytolookfor):
				if not daynottolookfor + " Night" in nohtml:
					nohtml = nohtml.replace(daynottolookfor,daynottolookfor + ": ")
					

for tide in tidesfh:
	if date in tide:
		elements = tide.split()
		if 'AM' in elements[3]:
			if 'L' in elements[6]:
				low = float(elements[4])
				term.cprint(4, 0, tide)
				#print("\n")
				
			if 'H' in elements[6]:
				high = float(elements[4])
				term.cprint(2, 0, tide)
				#print("\n")
				
			#print(tide.strip())	
			
				
			
resetcolor(term)			
exchange = high - low
#print(str(elements))
print("Exchange: %.2f" % exchange)
print(nohtml)
resetcolor(term)