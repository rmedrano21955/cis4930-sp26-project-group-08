# cis4930-sp26-project-group-08
## Group Members
| Name | FSU ID |
| ---- | ------ |
| Alejandra McLetchie	| am23ga |
| Raul Medrano |	rem22r |
| Jake Serwe |	js23g |
| Charlie Bleeze	| cfb22 |
## Project Description
 In this project we explore a dataset of Spotify tracks and their audio features to understand what characteristics are associated with popular music. Using attributes like danceability, energy, tempo, and genre, we investigate patterns in listener preferences and how audio features vary across categories and time.
## Dataset: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
## Dataset Justification
- Format: CSV
- Size: First 500 entries (raw dataset was too large)
- Numeric Columns: popularity, danceability, energy, tempo, loudness, duration_mmss, valence, liveness
- Categorical Columns: track_genre, explicit (True/False), popularity_level
## Research Questions
1. Which genres tend to have the highest average popularity?
2. What is the danceability of explicit songs compared to non-explicit songs?
3. Do high-tempo songs perform better than low-tempo songs?
## Repository Structure
```
cis4930-sp26-project-group-08/
|--README.md
|--CONTRIBUTING.md
|--data
|   |--raw/
|   |  |--dataset.csv.zip
|   |  |--sample.csv
|   |--processed/
|      |--processed_sample.csv
|--notebooks/
|  |--analysis.ipynb
|--figures/
|--src/
```
## Work Division
See CONTRIBUTING.md
