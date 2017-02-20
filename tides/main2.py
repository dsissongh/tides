import argparse


stations = {"Seattle":"9447130_annual.txt", "Whitney":"9445246_annual.txt"}


parser = argparse.ArgumentParser()
#parser.parse_args()

parser.add_argument("--station", help="specify station data")
args = parser.parse_args()
if args.station:
	print("station called")
	print(args.station)
	tides = stations[args.station]
else:
	print("Be sure to include one of the stations below:")
	print("Seattle")
	print("Point Whitney")
	exit()
	
#source: https://tidesandcurrents.noaa.gov

#tides = 'tides-dabob.txt'
tidesfh = open(tides,'r')

for tide in tidesfh:
	if '2017/02/19' in tide:
		elements = tide.split()
		if 'AM' in elements[3]:
			if 'L' in elements[6]:
				low = float(elements[4])
				
			if 'H' in elements[6]:
				high = float(elements[4])
				
			print(tide.strip())	
				
			
				
exchange = high - low
#print(str(elements))
print("Exchange: %.2f" % exchange)