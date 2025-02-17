#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10]

import matplotlib.pyplot as plt
top_10_items_sorted = sorted(items, key=lambda item:item[1])


for k,v in top_10_items_sorted:
    print(k,':',v)


# unpack items into separate lists for plotting
labels, values = zip(*top_10_items_sorted)

# graph the top 10 counts for the hashtag
plt.figure(figsize=(10,6))
plt.bar(labels, values, color='skyblue')
plt.tight_layout()
plt.savefig(f'top_10_{args.key}_country.png', format='png')
plt.close()
