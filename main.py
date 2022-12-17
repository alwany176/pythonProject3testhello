import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
mobile_names =[]
price=[]
locations_name =[]


result = requests.get ("https://www.olx.com.eg/mobile-phones-tablets-accessories-numbers/mobile-phones/")
src = result.content
#print(src)

soup = BeautifulSoup (src ,"lxml")
#print(soup)
mobile_name =soup.find_all ("div",{"class":"a5112ca8"})
#print(mobile_name)
mobile_price =soup.find_all ("div",{"class":"_52497c97"})
#print(mobile_price)
location_name = soup.find_all ("span",{"class":"_424bf2a8"})
#print(location_name)


for i in range(len(mobile_price)):
    mobile_names.append(mobile_name[i].text)
    price.append(mobile_price[i].text)
    locations_name.append(location_name[i].text)
#print(mobile_names,  price  , locations_name)
for mobile_names,price,locations_name in zip(mobile_names,price,locations_name):
      print("{} : {} : {}".format(mobile_names,price,locations_name))

