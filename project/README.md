This is a system that investigates data of tweets, some of which are anti-Semitic and some of which are not, and conducts an investigation on them

The first class is "Loader file" where it loads the csv file and returns it as a pandas file,


The second class called "data Investigate" is responsible for investigating the data,

In its constructor it receives it as 3 separate data types, 1. The entire file, 2. The file is sorted only by anti-Semites, 3. The file is sorted only by non-anti-Semites.

The first function "toral_tweets" returns how many anti-Semitic tweets there are and how many non-anti-Semitic and how many there are in total.

The second function "average_length" returns what is the average length of the tweets also sorted by anti-Semitic and non-anti-Semitic and in general what is the average.

The third function "longest_3_tweets" returns the 3 longest tweets in all categories (anti-Semitic and non-anti-Semitic).

The third function "common_words" returns the 10 most common words from all tweets.

The fifth function "uppercase_words" returns the number of words that are in uppercase letters.