import json
import boto3

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend')
    s3 = boto3.client('s3')
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket_name, Key=key)
    text = response['Body'].read().decode('utf-8')
    
    sentiment = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    
    sentiment_key = key.replace('transformed', 'sentiment').replace('.csv', '.json')
    s3.put_object(Bucket=bucket_name, Key=sentiment_key, Body=json.dumps(sentiment))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Sentiment analysis completed')
    }
