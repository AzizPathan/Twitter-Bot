import tweepy
import time

api_key = "S6T18y8YfFybAFw1T6AIWnZkC"
api_secret = "TjbEWgi1HcB5gIVAF1FmrFr1JxxZ95GyJD9JcAsq6nWhW4NwF8"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAL9dtwEAAAAA%2FSOI7zKbPjgN7bWk7luxZQY1tBQ%3DemuJzgac3Cbb1vcyBluAhu9twAGki4XxbEGwPDIW90Wqqh9DI6"
access_token = "1791411030675140608-tDtlc5rFZPFRrTLaDWvT7fmS3KEQdG"
access_token_secret = "AwbwshMKK1GPi2d6c1wKWAy8TD072eWoTd9lbpWmNWeNP"
# App_id="1791411030675140608"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.like(tweet.id)

        except Exception as error:
            print(error)

        time.sleep(1)


stream = MyStream(bearer_token = bearer_token)

rule = tweepy.StreamRule("(Royal_pathan OR #python)(-is:retweet -is:reply)")

stream.add_rules(rule)

stream.filter()