import pandas as pd
df = pd.read_csv("data/df_relabeled.csv")
print(df[["name_home", "aces_home", "breakpoints_won_home", "service_games_won_home", "service_games_won_away","name_away", "aces_away","breakpoints_won_away"]].head())