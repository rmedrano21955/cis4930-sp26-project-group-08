import requests
from django.conf import settings

def fetch_movies(query="john wick"):    # example to show it works
    url = "https://www.omdbapi.com/"

    params = {
        "apikey": settings.API_KEY,
        "s": query
    }

    response = requests.get(url, params=params)

    print("FINAL URL:", response.url)

    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    return response.json()

    # try:
    #     response =  requests.get(url, params={"q": query}, timeout=10)
    #     response.raise_for_status()
    #     return response.json()
    
    # except requests.exceptions.RequestException as e:
    #     print("API error:", e)
    #     return {"results": []}
