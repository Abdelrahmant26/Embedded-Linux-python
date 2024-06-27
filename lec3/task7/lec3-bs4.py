import bs4
import requests
import csv
x=requests.get("https://www.yallakora.com/")
#print(x.content)
y = bs4.BeautifulSoup(x.content, 'lxml')
divs = y.find_all("div", {"class": "soon"})
with open("out.csv", 'w') as file:
    wr=csv.writer(file)
    wr.writerow(["Tour", "Time", "TeamA", "TeamB"])
    for i in divs:
        Tour=i.find_all("div", ["tourName"])[0].text
        Time=" ".join(i.find_all("span", ["time"])[0].text.split())
        TeamA=" ".join(i.find_all("div", ["teamA"])[0].text.split())
        TeamB=" ".join(i.find_all("div", ["teamB"])[0].text.split())
        print("TourName : "+Tour)
        print(
            TeamA+
            " vs "+
            #i.find_all("div", ["teamB"])[0].text+
            TeamB+"\n"+
            Time+
            "\n---------------------"
        )
        wr.writerow([
            Tour,
            Time,
            TeamA,
            TeamB
        ])
#print(divs[0].text.split())
#print([divs[0]])
#t=divs[0].find_all("div", ["tourName"])
#print(t)