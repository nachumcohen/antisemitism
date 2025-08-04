import pandas as pd
class DataAnalyzer:

    def __init__(self , df = 'data/tweets_dataset.csv'):
        self.df = pd.read_csv(df)

    def mount_tweets_per_category_from_target(self , target = 'Biased'):
        df_mount = {}
        df = self.df
        df_mount["total_tweets"] = df[target].value_counts().to_dict()
        df_mount["total_tweets"]["total"] = len(df)

        return df_mount
        # with open("result/results.json" , 'a') as f:
        #     json.dump(df_mount , f)

    def average_length(self):
        average = {}
        df = self.df

        average["average_length"] = df.groupby('Biased').Text.apply(lambda x: x.str.split().str.len().mean()).to_dict()
        average["average_length"]["total"] = float(df.Text.str.split().str.len().mean())

        return average
        # with open("result/results.json", 'w') as f:
        #     json.dump(average, f)

    def three_max_tweets(self):
        max_len = {}
        df = self.df
        max_len["max_length"] = df.loc[df.groupby('Biased').Text.apply(lambda x: x.str.len().nlargest(3).idxmax()), 'Text']
        return max_len

    def max_ten_word(self):
        common_words = {}
        df = self.df

        common_words["total"] = pd.Series(' '.join(df['Text']).split()).value_counts()[:10].index.to_list()
        return common_words

    # def

