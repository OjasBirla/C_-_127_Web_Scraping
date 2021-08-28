from bs4.element import TemplateString
from selenium import webdriver
from bs4 import BeautifulSoup

import time
import csv

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("./chromedriver.exe")
browser.get(url)

def Scrape():
    Headers = ["Name", "Distance", "Mass" "Radius"]
    Planet_data = []

    Soup = BeautifulSoup(browser.page_source, "html.parser")
    
    for trTags in Soup.find_all("tr"):
        tdTags = trTags.find_all("td")
        tempList = []
        
        for index, row in enumerate(tdTags):
            try:
                if index == 1:
                    name = row.find_all("a")[0].contents[0]
                    tempList.append(name)
            
            except:
                tempList.append("")
        
        Planet_data.append(tempList)
    
    with open("Output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(Headers)
        writer.writerows(Planet_data)

Scrape()