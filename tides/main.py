import requests

req = requests.get("http://tides.mobilegeographics.com/locations/5016.html?y=2017&m=2&d=14")

print(str(req.text))