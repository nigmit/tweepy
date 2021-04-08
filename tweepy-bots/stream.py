import tweepy
import time
from datetime import datetime
from config import create_api
import key

# == OAuth Authentication ==
api = create_api()


class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api, nr_tweets=15, tweet_list=[], latest_tweet_id=1379936267610230789):
        self.api = api
        self.me = api.me()
        self.nr_tweets = nr_tweets
        self.tweet_list = tweet_list
        self.tweet_list.clear()
        self.latest_tweet_id = latest_tweet_id
        # self.f = f

    def increment(self):
        self.nr_tweets += 1
        return self.nr_tweets

    def set_tweet_id(self, tweet_id):
        self.latest_tweet_id = tweet_id

    def write_to_file(self, file_name, tweet_number, tweet):
        f = open(file_name, "a")
        user_name = tweet.user.name.encode("utf-8")
        f.write(f"{datetime.now()} Tweet {tweet_number} from {user_name} (@{tweet.user.screen_name}): ")
        f.write(tweet.text)
        f.write('\n\n')
        f.close()

    def on_status(self, tweet):
        try:
            print('***Got a tweet***')

            # pick the latest tweets
            tweet_set = set(self.tweet_list)
            skip_tweet = 'Tigray Police Man sexually attacked more than 50 women'
            if tweet.id > self.latest_tweet_id and \
                    tweet.text not in tweet_set and \
                    skip_tweet not in tweet.text and \
                    tweet.in_reply_to_status_id is None:  # Skip reply tweets
                tweet.retweet()
                print('Tweet Retweeted')
                self.tweet_list.append(tweet.text)
                # tweepy.utils.convert_to_utf8_str(tweet.user.name)
                user_name = tweet.user.name.encode("utf-8")
                tweet_number = self.increment()
                print(tweet.id)
                file_name = "C:\\Users\\enigdan\\Documents\\Tweepy\\streamed_tweets_nigmitdan.txt"
                self.write_to_file(file_name, tweet_number, tweet)
                print(self.tweet_list)
                wait_minutes = 3
                print(
                    f"{datetime.now()} Tweet {tweet_number} from {user_name}(@{tweet.user.screen_name}): "
                    f"{tweet.text}")
                # tweet.favorite()
                # print('Tweet Liked')
                if not tweet.user.following:
                    print('Follow user', user_name)
                    tweet.user.follow()

                # api.update_status(
                #     status="#EthiopiaPrevails",
                #     in_reply_to_status_id=tweet.id,
                # )
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
