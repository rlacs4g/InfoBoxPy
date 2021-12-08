from enum import auto
import requests
from bs4 import BeautifulSoup

        
#------------------------------------------------------------------------

url = "https://steamcharts.com/app/730"

page = requests.get(url)

counter = 0

soup = BeautifulSoup(page.content, "html.parser")

number = soup.find(id="app-heading")
title = soup.find(id="app-title")

chartElements = number.find_all("span", class_="num")
titleElements =  title.find("a", href_="")

#add .text to a Beautiful Soup object to return only the text content of the HTML elements that the object contains
header = titleElements.text, " | Steam Charts Source: ", url, "]\n"
for chartElements in chartElements:

    counter += 1

    if counter == 1:
        oneHour = ("\n1 hour ago    ", chartElements.text)
    elif counter == 2:
        tfPeak = ("\n24-hour peak  ", chartElements.text)
    elif counter == 3:
        atPeak = ("\nall-time peak ", chartElements.text )


print(header[0] + header[1] + header[2])
print(oneHour[0] + oneHour[1])
print(tfPeak[0] + tfPeak[1]) 
print(atPeak[0] + atPeak[1])

       
#input("enter to exit...")
