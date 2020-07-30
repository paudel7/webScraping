from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tid=6663'
#opening up connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename,"w")
headers = "brands, product_name, shipping\n"
f.write(headers)

for container in containers:
    brand  = container.div.div.a.img["title"]
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    print("Brand: "+ brand)
    print("Product: "+ product_name)
    print("Shipping Charge: "+shipping)
    f.write(brand+","+product_name.replace(",","|")+","+shipping+"\n")
f.close()
    


