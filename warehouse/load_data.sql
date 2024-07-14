COPY twitter_sentiment
FROM 's3://your-s3-bucket-name/data/sentiment/'
IAM_ROLE 'your-redshift-iam-role'
FORMAT AS JSON 'auto';
