import requests

req = requests.get("http://tides.mobilegeographics.com/locations/5016.html?y=2017&m=2&d=15")

#print(str(req.text))
lines = req.text.split("\n")
printit = False
for line in lines:
	if '<pre class="predictions-table">' in line:
		printit = True
		
	if '</pre>' in line:
		printit = False
		
	if(printit):
		print(line)