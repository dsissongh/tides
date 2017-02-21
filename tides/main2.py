import argparse
from colorconsole import terminal
from func import resetcolor


term = terminal.get_terminal(conEmu=False)
stations = {"Seattle":"9447130_annual.txt", "Whitney":"9445246_annual.txt"}


parser = argparse.ArgumentParser()
#parser.parse_args()

parser.add_argument("--station", help="specify station data")
parser.add_argument("--date", help="specify data as yyyy/mm/dd")
args = parser.parse_args()

if args.station:
	print("station called")
	print(args.station)
	tides = stations[args.station]
else:
	print("Be sure to include one of the stations below:")
	print("Seattle")
	print("Whitney")
	exit()
	
if args.date:
	print("For date: %s" % args.date)
	date = args.date
else:
	print("Dont forget to specify date.")
	exit()
	
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