import argparse
import time
import datetime
import collections
from colorconsole import terminal
from func import resetcolor
from func import getdatefornextsaturday

dow = datetime.datetime.today().weekday()
term = terminal.get_terminal(conEmu=False)
stations = {}

stations.update({"Seattle":"9447130_annual.txt"})
stations.update({"Point Whitney":"9445246_annual.txt"})
stations.update({"Port Townsend":"9444900_annual.txt"})
stations.update({"Admiralty Head":"9447905_annual.txt"})
stations.update({"Marrowstone Point":"9444972_annual.txt"})
stations.update({"Mystery Bay, Marrowstone Island":"9444971_annual.txt"})
stations.update({"Triton Head":"9445326_annual.txt"})

cstations = collections.OrderedDict(sorted(stations.items()))

order = {}
count = 1
term.clear()
term.cprint(3, 0, '')
print(str(cstations))
for key in cstations:
	order.update({count:cstations[key]})
	print("%s. %s" % (count, key))
	count += 1

#print(str(order))	
	
selection = input("\nWhat station would you like to use for source tide data? ")
tides = order[int(selection)]
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
resetcolor(term)