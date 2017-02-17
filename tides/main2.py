
tides = 'tides-dabob.txt'
tides = open(tides,'r')

for tide in tides:
	if '2017/02/18' in tide:
		elements = tide.split()
		if 'AM' in elements[3]:
			print(tide.strip())
			#print(str(elements))