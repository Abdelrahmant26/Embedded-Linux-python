import requests
x=requests.get("https://api.ipify.org/?format=json")
ip=x.json()["ip"]
print(ip)
y=requests.get("https://ipinfo.io/"+ip+"/geo").json()
print(y)
