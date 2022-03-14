from os import urandom
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'
uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "item-container"})

file_name = "C:\\test\product.csv"
f = open(file_name, "w")

headers = "brand , shipping , price \n"
f.write(headers)

for container in containers:
    brand = container.a.img["title"]
    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    price_list = container.findAll("li", {"class":"price-current"})
    price = price_list[0].text.strip().replace("|","").replace('\r', '').replace('\n', '')
    print("brand : " + brand)
    print("shipping : " + shipping)
    print("price : " + price)
    print("______________________________________________________")


    f.write(brand.replace(",","|") + "," + shipping + "," + price.replace(",",".") + "\n" )

f.close()
