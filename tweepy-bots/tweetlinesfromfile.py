import tweepy
import time
import sys
from datetime import datetime
from config import create_api
import os
import utils
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# create a text file with each line containing a sentence you want to tweet
#To run the bot do the following from command line:
#python tweetlinesfromfile.py

# == OAuth Authentication ==
api = create_api()

f_name_read = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'campaign_tweets.txt'
f_name_write = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'streamed_tweets.txt'
tweet_no = 0
f = utils.read_from_file(f_name_read)
interval = 15
internal_interval = 2
tweet_bunch = 10
i = 1

for line in f:
    if utils.tweet_exists(f_name_write, line):
        continue
    try:
        logger.info(f"Tweeting: {line}")
        api.update_status(line)
        logger.info(f"Writing tweet {utils.increment(tweet_no)} to file")
        tweet_no = tweet_no + 1
        utils.write_to_file(f_name_write, line)
        if i == tweet_bunch:
            logger.info(f" waiting for {interval} minutes ...")
            time.sleep(interval*60)
            i = 1
        else:
            time.sleep(internal_interval*60)
        i += 1
    except tweepy.TweepError as e:
        logger.error(e.reason)
        pass
    except UnicodeEncodeError as e:
        logger.error(e.reason)
        pass
    except ConnectionResetError:
        logger.error("Error detected")
        pass