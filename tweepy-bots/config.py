# bots/config.py
import tweepy
import logging
import key

logger = logging.getLogger()

def create_api():
    auth = tweepy.OAuthHandler(key.consumer_key_nigmitdan, key.consumer_secret_nigmitdan)
    auth.set_access_token(key.access_token_nigmitdan, key.access_token_secret_nigmitdan)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api