from bokeh.plotting import figure, show, output_file
from bs4 import BeautifulSoup
import pandas
import requests


r = requests.get("https://finance.yahoo.com/quote/CSV/history?p=CSV")
c = r.content

soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("tr",{"class":"BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)"})

list_of_item = []
for item in all:
    dict_of_item = {}
    try:
        dict_of_item["Date"]=item.find("td",{"class":"Py(10px) Ta(start) Pend(10px)"}).text
    except:
        pass
    try:
        dict_of_item["Open"]=item.find_all("td", {"class":"Py(10px) Pstart(10px)"})[0].text
    except:
        pass
    try:
        dict_of_item["High"]=item.find_all("td", {"class":"Py(10px) Pstart(10px)"})[1].text
    except:
        pass
    try:
        dict_of_item["Low"]=item.find_all("td", {"class":"Py(10px) Pstart(10px)"})[2].text
    except:
        pass
    try:
        dict_of_item["Close*"]=item.find_all("td", {"class":"Py(10px) Pstart(10px)"})[3].text
    except:
        pass
    try:
        dict_of_item["Adj Close**"]=item.find_all("td", {"class":"Py(10px) Pstart(10px)"})[4].text
    except:
        pass
    try:
        dict_of_item["Volume"]=item.find_all("td", {"class":"Py(10px) Pstart(10px)"})[5].text
    except:
        pass
    list_of_item.append(dict_of_item)

df = pandas.DataFrame(list_of_item)
#print(df["Date"])
#df.to_csv("stock.csv")

x = pandas.to_datetime(df["Date"], format='%d%b%Y:%H:%M:%S.%f')
y1 = df["Open"]
y2 = df["High"]
y3 = df["Close*"]
f = figure()
f.line(x,y1, color="red")
f.line(x,y2, color="blue")
f.line(x,y3, color="Black")
#
#
output_file("Line.html")
show(f)
