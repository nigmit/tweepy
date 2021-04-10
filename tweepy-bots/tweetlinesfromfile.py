import tweepy
import time
import sys
from datetime import datetime
from config import create_api

# create a text file with each line containing a sentence you want to tweet
#To run the bot do the following from command line:
#python tweetlinesfromfile.py

# == OAuth Authentication ==
api = create_api()

filename = open('campaign_tweets.txt', encoding="utf-8")
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    interval = 5  # Tweet every 5 minutes
    time.sleep(interval*60)
