import pandas as pd
from loader_file import File_loader

file = File_loader()
file = file.load("C:/pycharm/tweets-antisematic/project/data/tweets_dataset.csv")


class Investigate_data:
    def __init__(self, df):
        self.df = df
        self.antisemite = df[df['Biased'] == 1].copy()
        self.no_antisemite = df[df['Biased'] == 0].copy()

    def toral_tweets(self):
        #This function returns the number of tweets in each category.
        counts = self.df['Biased'].value_counts()
        return {
            "antisemitic": int(counts.get(1)),
            "non_antisemitic": int(counts.get(0)),
            "total": len(self.df)}

    def average_length(self):
        #This function returns the average length of the tweets at katagoryus.
        self.antisemite['lengthyas'] = self.antisemite['Text'].apply(lambda x: len(x.split()))
        self.no_antisemite['lengthno'] = self.no_antisemite['Text'].apply(lambda x: len(x.split()))
        self.df['length'] = self.df['Text'].apply(lambda x: len(x.split()))
        return {
            "antisemitic": float(self.antisemite['lengthyas'].mean()),
            "non_antisemitic": float(self.no_antisemite['lengthno'].mean()),
            "total": float(self.df['length'].mean())
        }





investigate = Investigate_data(file)
# investigate = investigate.toral_tweets()
investigate = investigate.average_length()
print(investigate)