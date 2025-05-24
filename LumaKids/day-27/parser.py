# pip install requests beautifulsoup4
# https://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup

def parser_quotes():
    try:
        res = requests.get("https://quotes.toscrape.com")
        soup = BeautifulSoup(res.text, "html.parser")
        # print(soup)
        quotes = soup.find_all("div", class_="quote")
        # print(quotes)

        for q in quotes:
            text = q.find("span", class_="text").get_text()
            print(f"Text: {text}")

            autor = q.find("small", class_="author").get_text()
            print(f"Author: {autor}\n")
    except Exception as e:
        print("error", e)


# parser_quotes()

def parser_book():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    res = requests.get(url)
    # print(res)
    soup = BeautifulSoup(res.text, "html.parser")
    # print(soup)
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        print(f"{title} - {price}\n")

parser_book()