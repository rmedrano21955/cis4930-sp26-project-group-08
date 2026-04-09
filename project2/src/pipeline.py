import requests
import pandas as pd
import sqlite3

API_KEY = "5589e759"
API_URL = "https://www.omdbapi.com/"

SEARCH_TERMS = ["sherlock holmes", "james bond", "godzilla"]
MAX_PAGES = 3

def fetch_movies(search_term):
    all_movies = []
    page = 1

    while page <= MAX_PAGES:
        params = {
            "apikey": API_KEY,
            "s": search_term,
            "page": page
        }

        try:        #page-based pagination
            response = requests.get(API_URL, params=params, timeout=10)
            print("Status:", response.status_code)

            response.raise_for_status()

            data = response.json()

            #failure handling
            if data.get("Response") == "False":
                print("No results:", data.get("Error"))
                break

            movies = data.get("Search", [])

            if not movies:
                break

            page += 1
        except requests.exceptions.Timeout:
            print("Request timed out, will skip this run.")
        except requests.exceptions.RequestException as e:
            print("Request error:", e)

    return all_movies

def main():
    #output record collection and save results

if __name__ == "__main__":
    main()