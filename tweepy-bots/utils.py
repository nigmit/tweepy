import datetime
import logging

logger = logging.getLogger()


def increment(arg):
    return arg + 1


def write_to_file(file_name, tweet):
    logger.info(f"Writing a tweet to {file_name}")
    f = open(file_name, "a")
    f.write(f"{datetime.datetime.now()} {tweet}")
    f.write('\n')
    f.close()


def read_from_file(file_name):
    logger.info(f"Reading from {file_name}")
    file = open(file_name, encoding="utf-8")
    f = file.readlines()
    file.close()
    return f


def get_tweet_text(tweet):
    logger.info('Get the tweet text')
    if ': ' in tweet:
        tweet = tweet.split(': ', 1)[1]
    return tweet


# tweet = "RT @NeaminZeleke: Egypt snubbing the African Union and insisting on involving the EU &amp;
# USA in talks with #Ethiopia about the #GERD is as su…"
def tweet_exists(file_name, tweet):
    logger.info('Checking if tweet already handled')
    with open(file_name) as f:
        if get_tweet_text(tweet)[:70] in f.read():
            logger.info("Tweet already exists")
            return True
    return False


def is_quote_tweet(tweet):
    logger.info("Check if tweet is a quote tweet")
    if 'quoted_status' in str(tweet):
        logger.info('This is a quote tweet')
        return True
    return False


def is_retweeted_tweet(tweet):
    logger.info("Check if tweet is a retweet")
    if 'retweeted_status' in str(tweet):
        logger.info('This is a retweet tweet')
        return True
    return False
