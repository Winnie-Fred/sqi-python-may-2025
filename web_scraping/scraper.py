import requests

from bs4 import BeautifulSoup

# url = "https://www.netflix.com/"
url = "https://www.fiverr.com/"


try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Hmmm....something went wrong. Are you connected to the internet?: {e}")
else:
    if response.status_code == 200:
        # print(response.text)
        # print(response.content)

        # print(response.status_code)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')

        # with open("netflix-home-page.html", "w", encoding="utf-8") as f:
        with open("fiverr-home-page.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        print("Scraping completed. Check \"netflix-home-page.html\" for the output.")
    else:
        print(f"""That was not supposed to happen. 
Response status code: {response.status_code}
Response: {response.text}
""")