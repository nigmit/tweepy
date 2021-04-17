import tweepy
import time
import sys
from datetime import datetime
from config import create_api
import os
import utils
import logging

logger = logging.getLogger()

# create a text file with each line containing a sentence you want to tweet
#To run the bot do the following from command line:
#python tweetlinesfromfile.py

# == OAuth Authentication ==
api = create_api()

f_name_read = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'campaign_tweets.txt'
f_name_write = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'streamed_tweets_nigmitdan.txt'
tweet_no = 0
f = utils.read_from_file(f_name_read)

for line in f:
    interval = 15  # Tweet every 15 minutes
    if utils.tweet_exists(f_name_write, line) is False:
        logger.info(f"Tweeting: {line}")
        api.update_status(line)
        logger.info(f"Writing tweet {utils.increment(tweet_no)} to file")
        tweet_no = tweet_no + 1
        utils.write_to_file(f_name_write, line)
    logger.info(f" waiting for {interval} minutes ...")
    time.sleep(interval*60)

exit()
