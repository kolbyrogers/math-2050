import pandas as pd
from scipy.stats import poisson

df = pd.read_csv("./soccer_results.csv")
homeScore = df["home_score"]
awayScore = df["away_score"]
totalGoals = homeScore + awayScore
df['date'] = pd.to_datetime(df['date'])
df = df.set_index(df['date'])
df = df.sort_index()