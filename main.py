import os
import sys
import time
import tweepy

def main(request):
  bt = os.environ.get('bearer_token')
  ck = os.environ.get('consumer_key')
  cs = os.environ.get('consumer_secret')
  at = os.environ.get('access_token')
  ats = os.environ.get('access_token_secret')
  
  api = tweepy.Client(bearer_token=bt,consumer_key=ck,consumer_secret=cs,access_token=at,access_token_secret=ats)
  tweet = api.create_tweet(text="Hello World Local.")

  return f"OK {bt},{ck},{cs},{at},{ats}"
