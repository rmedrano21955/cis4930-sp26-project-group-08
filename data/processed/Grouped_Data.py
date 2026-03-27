import pandas as pd

file_path = "data/processed/processed_sample.csv"

df = pd.read_csv(file_path)


explicit_danceability = df.groupby(['explicit'])['danceability'].mean()
print(explicit_danceability)

explicit_popularity = df.groupby(['explicit'])['popularity'].mean()
print(explicit_popularity)

genre_popularity = df.groupby(['track_genre'])['popularity'].mean()
print(genre_popularity)

tempo_performance = df.groupby(['tempo', 'energy'])['popularity'].mean()
print(tempo_performance)
