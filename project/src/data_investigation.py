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

    def longest_3_tweets(self):
        # This function returns the three longest tweets in each category.
        self.antisemite['char_count'] = self.antisemite['Text'].apply(len)
        self.no_antisemite['char_count'] = self.no_antisemite['Text'].apply(len)

        # Sort the DataFrame by character count and get the top 3 tweets
        anti_long = self.antisemite.sort_values(by='char_count', ascending=False).head(3)['Text'].tolist()
        non_anti_long = self.no_antisemite.sort_values(by='char_count', ascending=False).head(3)['Text'].tolist()

        return {
            "antisemitic": anti_long,
            "non_antisemitic": non_anti_long
        }

    def common_words(self):
        # This function returns the ten most common words in the tweets.
        full_data = ''.join(self.df['Text'].tolist()).lower().split()
        word_counter = pd.Series(full_data).value_counts()
        return {"total": word_counter.head(10).index.to_list()}

    def uppercase_words(self):
        # This function returns the all common uppercase words in the tweets.
        def count_uppercase_words(text):
            full_data = ''.join(text.tolist()).split()
            uppercase_words = [word for word in full_data if word.isupper() and word.isalpha()]
            word_counter = pd.Series(uppercase_words).value_counts()
            return  len(word_counter)
        return {
            "antisemite": count_uppercase_words(self.antisemite['Text']),
            "no_antisemite": count_uppercase_words(self.no_antisemite['Text']),
            "total": count_uppercase_words(self.df['Text'])
        }






investigate = Investigate_data(file)
# investigate = investigate.toral_tweets()
# investigate = investigate.average_length( )
# investigate = investigate.longest_3_tweets()
# investigate = investigate.common_words()
investigate = investigate.uppercase_words()

print(investigate)