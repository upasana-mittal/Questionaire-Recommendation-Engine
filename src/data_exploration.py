import pandas as pd

prob_data = pd.read_csv("data/train/problem_data.csv")
print(prob_data.head(5))
print(prob_data.info())
print(prob_data.level_type.unique())
print(prob_data.level_type.value_counts())
