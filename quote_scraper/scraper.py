from collections import Counter

import requests
from bs4 import BeautifulSoup


url = "http://quotes.toscrape.com/"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops. Something went wrong. Maybe check your connection. {e}")
else:
    response.encoding = 'utf-8'
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_divs = soup.select('div.quote span.text')
        print(f"Total number of quotes: {len(quotes_divs)}")

        authors_smalls = soup.select('div.quote small.author')
        authors = [author.text for author in authors_smalls]
        print(f"Number of unique authors: {len(set(authors))}")

        author_occurences = dict(Counter(authors))
        
        max_authors = []
        max_occurence = 0
        for author, occurence in author_occurences.items():
            if occurence > max_occurence:
                max_occurence = occurence
                max_authors = [author]
            elif occurence == max_occurence:
                max_authors.append(author)

        print(f"The authors with the most quotes are: {max_authors}")

        quotes = [quote.text for quote in quotes_divs if "is" in quote.text]
        print(f"Number of quotes containing is: {len(quotes)}")

        a_tags = soup.select('div.tags a.tag')
        tags = [tag.text for tag in a_tags]
        tags_occurences = dict(Counter(tags))
        for tag, occurence in tags_occurences.items():
            print(f"{tag}: {occurence}")

    else:
        print("That was not supposed to happen")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")


