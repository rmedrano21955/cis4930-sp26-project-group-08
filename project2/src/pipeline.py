from src.storage import save_to_csv, save_to_sqlite
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
				
			#JSON parsing
			for item in movies:
				record = {
					"title": item.get("Title),
					"year": item.get("Year"),
					"imdb_id": item.get("imdbID"),
					"type": item.get("Type"),
					"poster": item.get("Poster"),
					"search_term": search_term
				}

            all_movies.extend(movies)		
            page += 1
        except requests.exceptions.Timeout:
            print("Request timed out, will skip this run.")
        except requests.exceptions.RequestException as e:
            print("Request error:", e)

    return all_movies

def main():
    for term in SEARCH_TERMS:
        movies = fetch_movies(term)
        count_csv = save_to_csv(movies, search_term=term)
        count_db = save_to_sqlite(movies, search_term=term)
        print(f"Saved {count_csv} new to CSV, {count_db} new to SQLite for '{term}'")

if __name__ == "__main__":
    main()
