import tweepy

def postMap():
    # credentials
    bearer_token = 'xxxxxxxxxxxxxxxxxx'
    consumer_key = 'xxxxxxxxxxxxxxxxxx'
    consumer_secret = 'xxxxxxxxxxxxxxx'
    access_token = 'xxxxxxxxxxxxxxxxxx'
    access_token_secret = 'xxxxxxxxxxx'

    # v1 Auth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True)

    # v2 Auth
    client = tweepy.Client(
        bearer_token,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        wait_on_rate_limit=True
    )

    # upload media
    media_id = api.media_upload(filename="mapExport.jpg").media_id_string

    # text content
    tweet = "Mentions of Ukrainian oblasts in top 100 articles about The Ukraine War: \n\n\nArcpy coding project demonstration"
    client.create_tweet(text=tweet, media_ids=[media_id])