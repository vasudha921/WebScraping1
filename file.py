from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import requests
import pandas as pd


stars_universal_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("//Users//krishnamoorthypatlashankaranarayana//Webscraping1//chromedriver")
browser.get(stars_universal_url)
time.sleep(10)



soup = bs(browser.text, 'html.parser')
star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

for i in range(1, len (temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('stars_universal')