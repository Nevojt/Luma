# pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

def load_quotes():
    try:
        res = requests.get("https://quotes.toscrape.com")
        soup = BeautifulSoup(res.text, "html.parser")
        # print(soup)
        quotes = soup.find_all("div", class_="quote")
        # print(quotes)

        for q in quotes:
            # print(q)
            text = q.find("span", class_="text").get_text()
            print(f"Text: {text}")
            author = q.find("small", class_="author").get_text()
            print(f"Author: {author}\n")

    except Exception as e:
      print("error", e)

    return



def parse_book():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    # print(books)

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        print(f"{title} - {price}")


# load_quotes()

parse_book()
