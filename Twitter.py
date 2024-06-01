import tweepy

api_key = "S6T18y8YfFybAFw1T6AIWnZkC"
api_secret = "TjbEWgi1HcB5gIVAF1FmrFr1JxxZ95GyJD9JcAsq6nWhW4NwF8"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAL9dtwEAAAAA%2FSOI7zKbPjgN7bWk7luxZQY1tBQ%3DemuJzgac3Cbb1vcyBluAhu9twAGki4XxbEGwPDIW90Wqqh9DI6"
access_token = "1791411030675140608-tDtlc5rFZPFRrTLaDWvT7fmS3KEQdG"
access_token_secret = "AwbwshMKK1GPi2d6c1wKWAy8TD072eWoTd9lbpWmNWeNP"
# App_id="1791411030675140608"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
# client.create_tweet(text="os")
client.create_tweet(text="Hey this is aziz writing my tweet from terminal")  
# client.like("1791468208354160703")
# client.like("1791456339157569616")

# client.like("1791413834017886614")

# client.create_tweet(in_reply_to_tweet_id="1795033389726056909", text = "hello world")  


# client.retweet("1791468208354160703")

# for tweet in api.home_timeline():
#     print(tweet.text)

# person = client.get_user(username = "Salman Khan").data.id

# for tweet in client.get_user_tweets(person).data:
#     print(tweet.text)






