# instagram profile pic downloader

from selenium import webdriver
import urllib.request

# taking the user input

profile = input("Enter the profile handler :- ")

# webdriver object and opening chrome

browser = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')

# opening the instagram page of that profile handle

url = "https://www.instagram.com/"+profile+"/"
browser.get(url)

# getting the picture

try:
    x = "//img[@class='_6q-tv']"
    source = browser.find_element_by_xpath(x).get_attribute("src")
except:
    x = "//img[@class='be6sR']"
    source = browser.find_element_by_xpath(x).get_attribute("src")

#browser.get(source)

# path to download the image at loacal

path = "E:\\igPhoto\\" + profile + ".jpg"
 
# saving the photo at local

urllib.request.urlretrieve(source,path)

print("Image Downloaded")