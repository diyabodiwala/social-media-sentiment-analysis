import boto3
import pandas as pd
from io import StringIO
import json

def transform_data():
    s3_client = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'
    
    # List all raw data files
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='data/raw/')
    
    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith('.json'):
            # Read raw data from S3
            raw_obj = s3_client.get_object(Bucket=bucket_name, Key=key)
            raw_data = json.loads(raw_obj['Body'].read().decode('utf-8'))
            
            # Transform data
            transformed_data = pd.json_normalize(raw_data)
            
            # Save transformed data back to S3
            csv_buffer = StringIO()
            transformed_data.to_csv(csv_buffer, index=False)
            transformed_key = key.replace('raw', 'transformed').replace('.json', '.csv')
            s3_client.put_object(Bucket=bucket_name, Key=transformed_key, Body=csv_buffer.getvalue())

if __name__ == '__main__':
    transform_data()
