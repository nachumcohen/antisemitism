import pandas as pd
import json
from src.DataAnalyzer import DataAnalyzer
from src.ReportBuilder import DataCleaner

# df = DataAnalyzer()
# data = {}
# data.update(df.average_length())
# data.update(df.mount_tweets_per_category_from_target())
# data.update(df.max_ten_word())
#
# with open("result/results.json" , 'w') as f:
#              json.dump(data , f)

df = pd.read_csv("data/tweets_dataset.csv")
df_clean = pd.read_csv("result/cleaned_dataset_tweets.csv")
text = df['Text']
biased = df['Biased']
text = DataCleaner.clean_unctuation_marks(text)
text = DataCleaner.convert_to_lower(text)
biased = DataCleaner.remove_nan(biased)

df_clean['Text'] = text
df_clean['Biased'] = biased