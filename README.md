# Coronavirus twitter analysis

I scanned all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.

**Learning Objectives:**

1. work with large scale datasets
1. work with multilingual text
1. use the MapReduce divide-and-conquer paradigm to create parallel code

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
I analyzed about 1.1 billion tweets from 2020 that were geotagged.  

**About MapReduce:**

To speed up the computation, I followed the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets. The computations were done in parallel on a remote server with 80 processors, which made the computation time $O(n/80)$ where n is the number of tweets. 

MapReduce is a 3 step procedure summarized in the following image:

<img src=img/mapreduce.png width=100% />


For the split or partition step, the dataset of tweets was split into 366 zip files for each day of the year (2020 was a leap year). Each zip file contained 24 text files, one for each hour of the day. Each text file contains a single tweet per line in JSON format. For the map step, I wrote a Python script called `map.py` that counted the number of tweets that used specific hashtags for a single zip file. I created a shell script `run_maps.sh`that handled running `map.py` for every zip file in the background and ran it using `$ nohup run_maps.sh` to run the computation on the server overnight.  

For the reduce step, I created two different files to do this: `reduce.py` and `alternative_reduce.py`. `reduce.py` combined the outputs of `map.py` into two files: `country_combine` and `language_combine`. `alternative_reduce.py` combined the outputs of `map.py` and counted the number of tweets that used a specifc hashtag for every day of the year. After reducing the data, I used the Python library matplotlib to create visualizations of the data.  

## Visualizations

I ran `visualize.py` on the outputs of `reduce.py` to create bar charts of the top 10 countries and languages that tweeted using the hashtags '#coronavirus' and '#코로나바이러스'  ('#coronavirus' in Korean).

<img src="img/top_10_%23coronavirus_country.png" width="100%" />
<img src="img/top_10_%23coronavirus_language.png" width="100%" />
<img src="img/top_10_%23코로나바이러스_country.png" width="100%" />
<img src="img/top_10_%23코로나바이러스_language.png" width="100%" />


From these graphs, we can see that English tweets used the most number of '#coronavirus' and Korean tweets used the most number of '#코로나바이러스'. We can also see that the US sent out the most number of tweets using '#coronavirus' and Korea was the top country to use '#코로나바이러스'. 

I visualized the results of `alternative_reduce.py` by creating a line plot that showed the usage of the hashtags '#covid19', '#coronavirus', '#virus' for every day of the year.

<img src=src/daily_hashtag_usage.png width=100% />

Based on the graph above, we can see that the usage of all three hashtags peaked in the middle of March 2020, which was when the World Health Organization declared COVID-19 a pandemic. 
