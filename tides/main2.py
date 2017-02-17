
tides = 'tides-dabob.txt'
tides = open(tides,'r')

for tide in tides:
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