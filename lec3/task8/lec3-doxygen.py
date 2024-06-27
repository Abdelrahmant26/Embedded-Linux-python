import bs4
import csv
import openpyxl
with open("lec3/task8/docs/html/main_8c.html", 'r') as file:
    html=file.read()
    soup=bs4.BeautifulSoup(html, 'lxml')
    #print(soup)
    Left=soup.find_all("td", ["memItemLeft"])
    Right=soup.find_all("td", ["memItemRight"])
    print(len(Left))
    print(len(Right))
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = "type"
    sheet['B1'] = "signature"
    for i in range(0, len(Left)):
        print(
            Left[i].text+" "+ Right[i].text
        )
        sheet.append([str(Left[i].text), str(Right[i].text)])
    workbook.save('example.xlsx')