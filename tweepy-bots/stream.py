import tweepy
import time
from datetime import datetime
from config import create_api
import os

# == OAuth Authentication ==
api = create_api()


class MyStreamListener(tweepy.StreamListener):

    #
    def __init__(self, api, nr_tweets=0, latest_tweet_id=1380539222357110786,
                 file_name=os.path.dirname(os.path.realpath(__file__)) + os.sep + "stream_tweets.txt"):
        self.api = api
        self.me = api.me()
        self.nr_tweets = nr_tweets
        self.latest_tweet_id = latest_tweet_id
        self.file_name = file_name

    def increment(self):
        self.nr_tweets += 1
        return self.nr_tweets

    def set_tweet_id(self, tweet_id):
        self.latest_tweet_id = tweet_id

    def write_to_file(self, file_name, tweet_number, tweet):
        print("Writing a tweet to file")
        f = open(file_name, "a")
        user_name = tweet.user.name.encode("utf-8")
        f.write(f"{datetime.now()} Tweet {tweet_number} from {user_name} (@{tweet.user.screen_name}): ")
        f.write(tweet.text)
        f.write('\n\n')
        f.close()

    def get_tweet_text(self, tweet):
        print('Get the tweet text')
        print(tweet)
        if ': ' in tweet:
            tweet = tweet.split(': ', 1)[1]
        return tweet

    #tweet = "RT @NeaminZeleke: Egypt snubbing the African Union and insisting on involving the EU &amp;
    # USA in talks with #Ethiopia about the #GERD is as su…"
    def tweet_exists(self, file_name, tweet):
        print('Checking if tweet already handled')
        print(tweet)
        with open(file_name) as f:
            if self.get_tweet_text(tweet)[:70] in f.read():
                return True
        return False

    def is_quote_tweet(self, tweet):
        print("Check if tweet is a quote tweet")
        if 'quoted_status' in str(tweet):
            print('This is a quote tweet')
            return True
        return False

    def is_retweeted_tweet(self, tweet):
        print("Check if tweet is a retweet")
        if 'retweeted_status' in str(tweet):
            print('This is a retweet tweet')
            return True
        return False

    def on_status(self, tweet):
        try:
            if self.is_quote_tweet(tweet) is False and \
                    tweet.id > self.latest_tweet_id and \
                    self.tweet_exists(self.file_name, tweet.text) is False and \
                    tweet.id > self.latest_tweet_id:
                print('*** Got a tweet to retweet ***')
                tweet.retweet()
                print('Tweet Retweeted')

                tweet_number = self.increment()
                print(tweet.id)
                self.write_to_file(self.file_name, tweet_number, tweet)
                wait_minutes = 3
                print(
                    f"{datetime.now()} Tweet {tweet_number}: "
                    f"{tweet.text}")
                # tweet.favorite()
                if not tweet.user.following:
                    print('Follow user', tweet.user.name.encode("utf-8"))
                    tweet.user.follow()
                if self.is_retweeted_tweet(tweet):
                    print('Follow user', tweet.retweeted_status.user.name.encode("utf-8"))
                    tweet.retweeted_status.user.follow()

                self.set_tweet_id(tweet.id)
                print(f" waiting for {wait_minutes} minutes ...")
                time.sleep(wait_minutes * 60)
        except tweepy.TweepError as e:
            print(e.reason)
        except UnicodeEncodeError as e:
            print(e.reason)
            pass
        except ConnectionResetError:
            print("Error detected")
            pass

    def on_error(self, status):
        print("Error detected")


def main(t_keyword, f_keyword):
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=t_keyword, follow=f_keyword, languages=["en", "am"], is_async=False)


if __name__ == "__main__":
    string_pattern_to_track = ["AhmaraGenocide", "EthiopiaPrevails", "EthioEritreaPrevail", "StandWithEthiopia",
                               "SupportEthiopia", "UNSCsupportEthiopia", "UnityForEthiopia", "GleanEthiopia",
                               "TplfLies", "TPLFLies", "FakeAxumMassacre", "DeliverTheAid", "TPLFisaTerroristGroup",
                               "TPLFisTheCause", "TPLFCrimes", "TPLFcrimes", "MaiKadraMassacre", "AxumFiction",
                               "TPLF_Junta", "FillTheDam", "EthiopianLivesMatter", "ItsMyDam",
                               "DisarmTPLF", "StopScapegoatingEritrea", "RisingEthiopia",
                               "AbiyMustLead", "TPLFisDEAD"]

    followers_to_track = ["4077439067",  # @neaminzeleke
                          "1357188308242169856",  # @gleanethiopian
                          "276370580",  # @dejene_2011
                          "1345123740603047936"  # @unityforethio
                          ]

    main(string_pattern_to_track, followers_to_track)
