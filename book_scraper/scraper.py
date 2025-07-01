import requests

from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"


try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops. Something went wrong. Maybe check your internet connection? More details: {e}")
else:
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.prettify())
        # all_divs = soup.find_all('div')
        # for div in all_divs:
        #     print(div)
        #     print("==========================================")
        # first_p = soup.find('p', class_="star-rating Three")

        # print(first_p)
        # price_color_p = soup.select('div.product_price p.price_color')
        # print(price_color_p)
        # no_of_books = 
        article_books = soup.select('li article.product_pod')
        no_of_books = len(article_books)
        print(f"Number of books: {no_of_books}")

        p_prices = soup.select('article.product_pod div.product_price p.price_color')
        # print(p_prices)
        prices = [float(p_price.text[1:]) for p_price in p_prices]
        # print(prices)
        total_price = sum(prices)
        avg_price = round(total_price / no_of_books, 2)
        print(f"Average price: £{avg_price}")

        titles_a = soup.select('article.product_pod h3 a')
        titles = [title.text for title in titles_a]

        highest_price = prices[0]
        most_expensive_book = titles[0]
        
        for title, price in zip(titles, prices):
            if price > highest_price:
                highest_price = price
                most_expensive_book = title

        print(f"Most expensive book: {most_expensive_book}")


        books_in_stock = 0
        books_in_stock_p = soup.select("article.product_pod div.product_price p.instock")
        for p_book in books_in_stock_p:
            text = p_book.text
            if text.lower().strip() == "in stock":
                books_in_stock += 1

        print(f"Number of books in stock: {books_in_stock}")
    else:
        print("Request was unsuccessful.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

