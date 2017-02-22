import argparse
import time
from colorconsole import terminal
from func import resetcolor

term = terminal.get_terminal(conEmu=False)
stations = {}

stations.update({"Seattle":"9447130_annual.txt"})
stations.update({"Point Whitney":"9445246_annual.txt"})
stations.update({"Port Townsend":"9444900_annual.txt"})
stations.update({"Admiralty Head":"9447905_annual.txt"})
stations.update({"Marrowstone Point":"9444972_annual.txt"})
stations.update({"Mystery Bay, Marrowstone Island":"9444971_annual.txt"})

order = {}
count = 1
term.clear()
term.cprint(3, 0, '')
for key in stations:
	order.update({count:stations[key]})
	print("%s. %s" % (count, key))
	count += 1

#print(str(order))	
	
selection = input("\nWhat station would you like to use for source tide data? ")
tides = order[int(selection)]
predate = time.strftime("%Y/%m/%d")
date = input("What date would you like H/L tide information for (yyyy/mm/dd)? [" + predate + "]")

if date == '':
	## yyyy/mm/dd format
	date = time.strftime("%Y/%m/%d")

#source: https://tidesandcurrents.noaa.gov

#tides = 'tides-dabob.txt'
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