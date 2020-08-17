from selenium import webdriver
import pandas as pd
import time

# Covid 19 Webscrapper

browser = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')

# opening sites

browser.get("https://www.worldometers.info/coronavirus/")
time.sleep(15)

#creating Data Frame

df = pd.DataFrame(columns=['Rank','Country','Total Cases','New Cases','Deaths','New Deaths','Recovered','Active Cases','Critical'])

# finding xpath and info

for i in browser.find_elements_by_xpath("//*[@id='main_table_countries_today']/tbody/tr"):
    td_list = i.find_elements_by_tag_name('td')
    row = []
    for td in td_list:
        row.append(td.text)
    data={}
    for j in range(len(df.columns)):
        data[df.columns[j]] = row[j]
    
    df.append(data, ignore_index=True)
print(df)