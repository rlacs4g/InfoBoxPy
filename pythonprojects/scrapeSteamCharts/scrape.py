import requests
from bs4 import BeautifulSoup

url = "https://steamcharts.com/app/570"

page = requests.get(url)

counter = 0

counterList = [1,2,3]

soup = BeautifulSoup(page.content, "html.parser")

number = soup.find(id="app-heading")
title = soup.find(id="app-title")

chartElements = number.find_all("span", class_="num")
titleElements =  title.find("a", href_="")

#add .text to a Beautiful Soup object to return only the text content of the HTML elements that the object contains
print(titleElements.text, " Steam Charts [Source: ", url, "]\n")
for chartElements in chartElements:

    counter += 1

    if counter == 1:
        print("1 hour ago    ", chartElements.text, end="\n"*2)
    elif counter == 2:
        print("24-hour peak  ", chartElements.text, end="\n"*2)
    elif counter == 3:
        print("all-time peak ", chartElements.text, end="\n"*2)

#------------------------------------------------------------------------
url = "https://steamcharts.com/app/1240440"

page = requests.get(url)

counter = 0

counterList = [1,2,3]

soup = BeautifulSoup(page.content, "html.parser")

number = soup.find(id="app-heading")
title = soup.find(id="app-title")

chartElements = number.find_all("span", class_="num")
titleElements =  title.find("a", href_="")

#add .text to a Beautiful Soup object to return only the text content of the HTML elements that the object contains
print(titleElements.text, " Steam Charts [Source: ", url, "]\n")
for chartElements in chartElements:

    counter += 1

    if counter == 1:
        print("1 hour ago    ", chartElements.text, end="\n"*2)
    elif counter == 2:
        print("24-hour peak  ", chartElements.text, end="\n"*2)
    elif counter == 3:
        print("all-time peak ", chartElements.text, end="\n"*2)
        
#-----------------------------------------------------------------------

url = "https://steamcharts.com/app/730"

page = requests.get(url)

counter = 0

soup = BeautifulSoup(page.content, "html.parser")

number = soup.find(id="app-heading")
title = soup.find(id="app-title")

chartElements = number.find_all("span", class_="num")
titleElements =  title.find("a", href_="")

#add .text to a Beautiful Soup object to return only the text content of the HTML elements that the object contains
print(titleElements.text, " Steam Charts [Source: ", url, "]\n")
for chartElements in chartElements:

    counter += 1

    if counter == 1:
        print("1 hour ago    ", chartElements.text, end="\n"*2)
    elif counter == 2:
        print("24-hour peak  ", chartElements.text, end="\n"*2)
    elif counter == 3:
        print("all-time peak ", chartElements.text, end="\n"*2)


       
input("enter to exit...")
