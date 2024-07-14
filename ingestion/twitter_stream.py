import tweepy
import boto3
import json
from datetime import datetime

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# AWS S3 credentials
s3_bucket = "your-s3-bucket-name"
s3_prefix = "data/raw/"

# Set up Twitter API client
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# S3 client
s3 = boto3.client('s3')

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        data = {
            'created_at': str(status.created_at),
            'text': status.text,
            'user': status.user.screen_name
        }
        filename = f"{s3_prefix}{datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')}.json"
        s3.put_object(Bucket=s3_bucket, Key=filename, Body=json.dumps(data))
        print(f"Stored tweet to {filename}")
    
    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == "__main__":
    listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=listener)
    stream.filter(track=['keyword1', 'keyword2'], languages=['en'])
