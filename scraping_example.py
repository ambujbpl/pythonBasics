# pip install beautifulsoup4
# pip install requests    // --user
# pip install pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd
#page = requests.get("https://forecast.weather.gov/MapClick.php?lat=44.9055&lon=-122.8107&lg=english&FcstType=text#.XjUM82gzZPY");
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=36.3741&lon=-119.2702#.XjUcwWgzZPY");
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.find_all('a'))
day7 = soup.find(id="seven-day-forecast-container");
#print(day7)
#print(day7.find_all('li'))
#print(day7.find_all(class_="forecast-tombstone"))
items = day7.find_all(class_="tombstone-container");
#print(items[0])
# for item in items:
#     print("\n\n")
#     print(item.find(class_="period-name").getText())
#     print(item.find(class_="short-desc").getText())
#     print(item.find(class_="temp").getText())
#     print("\n\n")

pName = [item.find(class_="period-name").getText() for item in items]
sDesc = [item.find(class_="short-desc").getText() for item in items]
temp = [item.find(class_="temp").getText() for item in items]


#
# print(pName)
# print(sDesc)
# print(temp)

weather_stuff = pd.DataFrame({
    "period":pName,
    "short description":sDesc,
    "temprature":temp
})

print(weather_stuff)
weather_stuff.to_csv("weather_stuff1.csv") # make csv for you