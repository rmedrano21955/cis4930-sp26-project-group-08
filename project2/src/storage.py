import pandas as pd
import sqlite3
import os
from datetime import datetime


CSV_PATH = "data/processed/movies.csv"
DB_PATH = "data/processed/movies.db"

def clean_dataframe(df: pd.DataFrame, search_term: str = "") -> pd.DataFrame:
	df = df.rename(columns={
		"Title": "title",
		"Year": "year",
		"imdbID": "imdbID",
		"Type": "type",
		"Poster": "poster_url",
	})

	df["year"] = pd.to_numeric(df["year"].str.extract(r"(\d{4})", expand=False), errors="coerce")

	df["search_term"] = search_term
	df["fetched_at"] = datetime.now().isoformat()

	return df


def save_to_csv(records: list[dict], search_term: str = ""):
	df = clean_dataframe(pd.DataFrame(records), search_term)
	
	if os.path.exists(CSV_PATH):
		existing = pd.read_csv(CSV_PATH)
		df = df[~df["imdbID"].isin(existing["imdbID"])]
		if df.empty:
			print(f"No new records for '{search_term}'")
			return 0
		df.to_csv(CSV_PATH, mode="a", header=False, index=False)
	else:
		os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
		df.to_csv(CSV_PATH, index=False)

	return len(df)

def save_to_sqlite(records: list[dict], search_term: str = "") -> int:
	df = clean_dataframe(pd.DataFrame(records), search_term)

	os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
	conn = sqlite3.connect(DB_PATH)

	try:
		existing_ids = pd.read_sql("SELECT imdb_id FROM movies", conn)["imdb_id"]
		df = df[~df["imdb_id"].isin(existing_ids)]
	except pd.errors.DatabaseError:
		pass

	if df.empty:
		print(f"No new records for '{search_term}")
		conn.close()
		return 0

	df.to_sql("movies", conn, if_exists="append", index=False)
	conn.close()
	return len(df)
