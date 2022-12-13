import requests
import bs4
import os

file = open("mina.txt", "w")
url = "https://www.jumia.com.eg/?gclid=Cj0KCQiAnNacBhDvARIsABnDa69F7AyZyRvMBazTtdQmOHuuKzRGdh5978_K4fZrKkk8bCzncjrwHxsaAre5EALw_wcB"
page = requests.get(url)

if page.status_code == 200:
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    product = soup.find_all("div", {"class": "name"})
    price = soup.find_all('div', {"class": "prc"})
    file.write("Index\tPrice\t\t\t\tProduct\n")
    for i, j in enumerate(product):
        file.write(str(i+1))
        file.write("\t")
        file.write(str(price[i].get_text()))
        file.write("\t\t\t")
        file.write(j.get_text())
        file.write("\n")
else:
    file.write(page.status_code)

file = open("mina.txt", "r")
print(file.read())
file.close()
#os.remove("mina.txt")