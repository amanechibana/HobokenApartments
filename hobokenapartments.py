# web scrapping hoboken apartment price
from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.apartmentlist.com/nj/hoboken")
soup = BeautifulSoup(page.text,'html.parser')

titles = soup.findAll('a', attrs={'class':'group-loading:loading-darker text-subheading-medium no-underline truncate'})
address = soup.findAll('div', class_='flex flex-wrap gap-x-1')
p_price = soup.findAll('div', attrs={'class':'flex w-full flex-row justify-between gap-4'})
prices = []

for p_text in p_price:
    price = p_text.find('div', class_='css-131gjbf e170khe30')
    if price:
        prices.append(price)

apartment_listings = []


for title,add,price in zip(titles, address, prices):
    apartment_listings.append([title.text,add.text,int(price.text.translate({ord(i): None for i in '$,+'}))])

apartment_listings.sort(key=lambda tup: tup[2])

for apartment in apartment_listings:
    print(apartment)


