import boto3

def create_crawler():
    glue = boto3.client('glue')
    
    response = glue.create_crawler(
        Name='twitter-crawler',
        Role='your-glue-service-role',
        DatabaseName='twitter_db',
        Targets={'S3Targets': [{'Path': 's3://your-s3-bucket-name/data/raw/'}]}
    )
    
    return response

if __name__ == "__main__":
    create_crawler()
