from wsgiref import headers

import requests

try:
    print("Welcome to the BK News!")
    query = input("Enter a news topic what you want to search: ")
    api = "1c89173aa4784df09659ad4a2ef1b64c"

    url = f"https://newsapi.org/v2/everything?q={query}&from=2026-02-28&sortBy=publishedAt&apiKey={api}"

    r = requests.get(url)
    print(f"The status is: {r.status_code}")

    data = r.json()
    articles = data["articles"]

    for index, article in enumerate(articles):
        index = index + 1
        title = article["title"]
        description = article["description"]
        link = article["url"]
        print(f" News: {index} \n Title :{title} \n Description: {description} \n Link: {link}")
        print("\n*********************************************************************\n")
except Exception as e:
    print(e)