import pandas as pd

prob_data = pd.read_csv("data/train/problem_data.csv")
print(prob_data.head(5))
print(prob_data.info())

user_data = pd.read_csv("data/train/user_data.csv")
print(user_data.head(5))
print(user_data.info())

train_subs = pd.read_csv("data/train/train_submissions.csv")
print(train_subs.head(5))
print(train_subs.info())
print(train_subs.attempts_range.value_counts())
print(train_subs.user_id.value_counts())

# print(prob_data.level_type.unique())
# print(prob_data.level_type.value_counts())

# nan_data = prob_data[prob_data.level_type.isnull()]
# print(nan_data.points.value_counts())
# print(nan_data.tags.value_counts())
# print(nan_data.info())
#
# data = nan_data['tags'].str.split(',', expand=True)
# print(data.head(20))
#
# data1 = pd.get_dummies(data)
# print(data1.info())
