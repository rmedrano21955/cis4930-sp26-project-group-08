# cis4930-sp26-project-group-08
## Group Members
| Name | FSU ID | Responsibility |
| ---- | ------ | -------------- |
| Alejandra McLetchie	| am23ga | Error Checking|
| Raul Medrano |	rem22r | HTTP, params, pagination |
| Jake Serwe |	js23g | Handled documentation
| Charlie Bleeze	| cfb22 | DataFrame, CSV/SQLite |



# Project: Movie Data Tracker
A pipeline for acquiring movie data from the OMDb API based on specific search terms
- Supports storage of data in CSV and a SQLite database
- EDA support via notebook

API Documentation available at [https://www.omdbapi.com/](https://www.omdbapi.com/)
This API was chosen as it provides thorough movie querying for free.
Its main constraint is a rate limit of 1000 requests per day for unpaid API keys.

DB Schema:
```sql
CREATE TABLE "movies" (
  "title" TEXT,
  "year" INTEGER,
  "imdbID" TEXT,
  "Type" TEXT,
  "poster_url" TEXT,
  "search_term" TEXT,
  "fetched_at" TEXT
);
```                    

Data Pipeline Goals
- Fetch movie/TV series data from the OMDb API for 3 search terms (sherlock holmes, james bond, godzilla) with pagination
- Accumulate results into a single CSV file and SQLite database adding new records per run
- Handle failures gracefully with logging
- Prevent duplicate entries via imdbID check
- Enable exploratory analysis via jupyter notebook

Example usage:
```
python -m src.pipeline
Status: 200
Status: 200
Status: 200
Saved 30 new to CSV, 30 new to SQLite for 'sherlock holmes'
Status: 200
Status: 200
Status: 200
Saved 30 new to CSV, 30 new to SQLite for 'james bond'
Status: 200
Status: 200
Status: 200
Saved 30 new to CSV, 30 new to SQLite for 'godzilla'
```
