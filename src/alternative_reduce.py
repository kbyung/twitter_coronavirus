#!/usr/bin/env python3

# imports
import argparse
import os
import json
from collections import Counter,defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True, help='Paths to input files')
parser.add_argument('--output_path', required=True, help='Path to output JSON file')
parser.add_argument('--hashtags', required=True, help='Comma-separated list of hashtags')
args=parser.parse_args()

# Initialize dictionaries
hashtags = [h.strip() for h in args.hashtags.split(',')]
daily_counts = {hashtag: defaultdict(int) for hashtag in hashtags}

# load each of the input paths
for path in args.input_paths:
# extract date from filename
    filename = os.path.basename(path)
    date = filename[13:18]

    # Convert MM-DD to day of the year
    month, day = map(int, date.split('-'))
    day_of_year = datetime(2020, month, day).timetuple().tm_yday 

    with open(path) as f:
        data = json.load(f)
# count tweets for each hashtag
        for hashtag in hashtags:
            if hashtag in data:
                daily_counts[hashtag][day_of_year] = sum(data[hashtag].values())


# Create the line plot

fig, ax = plt.subplots(figsize=(14,7))

for hashtag, counts in daily_counts.items():
    days = sorted(counts.keys()) 
    values = [counts[day] for day in days]
    ax.plot(days, values, label=hashtag)

ax.set_xlabel('Day of the Year')
ax.set_ylabel('Number of Tweets')
ax.set_title('Daily Hashtag Usage in 2020')
ax.legend(loc='upper right')
ax.grid(False)

ax.xaxis.set_major_locator(MaxNLocator(nbins=15))
plt.xticks(rotation=45)
plt.savefig('daily_hashtag_usage.png')
