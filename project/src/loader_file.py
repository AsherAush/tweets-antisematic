import pandas as pd

class File_loader:
    # A function that reads the file and returns it as a Pandas file.
    def load(self , file_path):
        df = pd.read_csv(file_path)
        return df

# a = loader_file()
# b = a.load("C:/pycharm/tweets/data/tweets_dataset.csv")
# c = a.load("data.tweets_dataset.csv")
# print(b.shape)
# print(b.head())