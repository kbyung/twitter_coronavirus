#!/bin/bash
for file in '/data/Twitter dataset/'geoTwitter20-*-*.zip; do
    if [ -f "$file" ]; then
        python3 map.py --input_path "$file" &
    else
        echo "Error: File '$file' does not exist"
    fi
done


