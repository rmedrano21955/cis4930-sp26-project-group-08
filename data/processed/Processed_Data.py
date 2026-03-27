import pandas as pd

file_path = "data/raw/sample.csv"

df = pd.read_csv(file_path)

df.drop(['key', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'time_signature'], axis=1, inplace=True)

df.to_csv("data/processed/processed_sample.csv", index=False)
