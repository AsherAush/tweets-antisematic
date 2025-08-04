import pandas as pd
from loader_file import File_loader

file = File_loader()
file = file.load("C:/pycharm/tweets-antisematic/project/data/tweets_dataset.csv")


class Investigate_data:
    def __init__(self, df):
        self.df = df

    def toral_tweets(self):
        #This function returns the number of tweets in each category.
        counts = self.df['Biased'].value_counts()
        return {
            "antisemitic": int(counts.get(0)),
            "non_antisemitic": int(counts.get(1)),
            "total": len(self.df)}

investigate = Investigate_data(file)
investigate = investigate.toral_tweets()
print(investigate)